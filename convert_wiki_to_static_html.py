import argparse
import glob
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from xml.sax.saxutils import escape as xml_escape

# wiki page names may contain characters outside the console codepage (e.g. u+2010
# in RSopen); never let a diagnostic print kill the build over that
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(errors="replace")

SITE_URL = "https://www.geodms.nl"

# The sites that together form geodms.nl. The first entry is deployed at the
# domain root, the others in the subdirectory named by their baseurl.
# To add a wiki: add an entry here, create template/_config_<name>.yml with its
# title and baseurl, extend keep_files in template/_config.yml and (optionally)
# add a nav_external_links entry there so the main site links to it.
SITES = {
    "geodms": {
        "title": "GeoDMS",
        "wiki_git_url": "https://github.com/ObjectVision/GeoDMS.wiki.git",
        "baseurl": "",
    },
    "rsopen": {
        "title": "RSopen",
        "wiki_git_url": "https://github.com/ObjectVision/RSopen.wiki.git",
        "baseurl": "/rsopen",
    },
    "networkmodel_pbl": {
        "title": "NetworkModel PBL",
        "wiki_git_url": "https://github.com/ObjectVision/NetworkModel_PBL.wiki.git",
        "baseurl": "/networkmodel_pbl",
    },
    "crisp": {
        "title": "CRISP",
        "wiki_git_url": "https://github.com/ObjectVision/CRISP.wiki.git",
        "baseurl": "/crisp",
    },
    "academy": {
        "title": "GeoDMS Academy",
        "wiki_git_url": "https://github.com/ObjectVision/GeoDMS_Academy.wiki.git",
        "baseurl": "/academy",
    },
}

OUT_ROOT = "_out"
TEMPLATE_DIR = "template"

# IndexNow (https://www.indexnow.org/) lets us tell Bing, Yandex, Seznam and Naver which
# pages changed, without an account anywhere. The key is public by design: it is served at
# SITE_URL/<key>.txt to prove we control the site. Google does not use IndexNow.
INDEXNOW_KEY = "25c546cdc37b205474a8170f224fca70"
INDEXNOW_PAYLOAD_FILE = "indexnow-payload.json"  # outside _out, so it is not deployed

# where security researchers should report an issue, most preferred first (RFC 9116).
# Deliberately a url and not a mailto: the github security policy already routes to the
# right mailbox, and publishing an address here mostly attracts bounty-beggar spam.
SECURITY_CONTACTS = [
    "https://github.com/ObjectVision/GeoDMS/security/policy",
]

# github repo name -> site name, e.g. "RSopen" -> "rsopen", derived from the wiki urls
REPO_TO_SITE = {}
for _site_name, _site in SITES.items():
    _repo = _site["wiki_git_url"].rsplit("/", 1)[-1]
    if _repo.endswith(".wiki.git"):
        _repo = _repo[:-len(".wiki.git")]
    REPO_TO_SITE[_repo] = _site_name

CROSS_WIKI_LINK_RE = re.compile(
    r"https://github\.com/ObjectVision/("
    + "|".join(re.escape(r) for r in REPO_TO_SITE)
    + r")/wiki(?:/([^)\s\]]*))?"
)

def rewrite_cross_wiki_links(text:str, file_dicts_by_site:dict) -> str:
    # links to the github wiki of any site in SITES become links inside geodms.nl,
    # so the wikis can reference each other (and themselves) by their github url
    def replace(match):
        site_name = REPO_TO_SITE[match.group(1)]
        baseurl = SITES[site_name]["baseurl"]
        page = urllib.parse.unquote(match.group(2) or "").strip("/")
        if not page:
            return f"{SITE_URL}{baseurl}/"
        page_part, _, anchor_part = page.partition("#")
        anchor = f"#{anchor_part}" if anchor_part else ""
        key = page_part.replace(" ", "-").lower().replace("...", "-")
        if key == "home":
            return f"{SITE_URL}{baseurl}/{anchor}"
        if key not in file_dicts_by_site[site_name]:
            return match.group(0)  # page unknown in that wiki: keep the github link
        return f"{SITE_URL}{baseurl}/docs/{key}.html{anchor}"
    return CROSS_WIKI_LINK_RE.sub(replace, text)

# Images pasted straight into the github wiki editor end up on github's attachment CDN
# instead of in the wiki's images/ folder. Serving those from geodms.nl instead keeps the
# site self-contained: no dependency on github staying reachable and on its (signed,
# short-lived) urls, no visitor data leaking to github, and a strict img-src CSP can hold.
EXTERNAL_IMAGE_RE = re.compile(r"https://github\.com/user-attachments/assets/[0-9a-fA-F-]+")
EXTERNAL_IMAGE_DIR = "_external_images"   # download cache, outside template/
EXTERNAL_IMAGE_SUBDIR = "external"        # lands in assets/img/external/
CONTENT_TYPE_EXTENSIONS = {
    "image/png": ".png", "image/jpeg": ".jpg", "image/gif": ".gif",
    "image/webp": ".webp", "image/svg+xml": ".svg", "image/bmp": ".bmp",
}

def localize_external_images(text:str, baseurl:str) -> str:
    # download each external image once into EXTERNAL_IMAGE_DIR and point the markdown at
    # our own copy; on any failure the original url is kept so the page still renders
    def replace(match):
        url = match.group(0)
        image_id = url.rsplit("/", 1)[-1]
        existing = glob.glob(f"{EXTERNAL_IMAGE_DIR}/{image_id}.*")
        if existing:
            name = os.path.basename(existing[0])
            return f"{baseurl}/assets/img/{EXTERNAL_IMAGE_SUBDIR}/{name}"

        try:
            request = urllib.request.Request(url, headers={"User-Agent": "GeoDmsWikiToStaticHtml"})
            with urllib.request.urlopen(request, timeout=60) as response:
                content_type = (response.headers.get("Content-Type") or "").split(";")[0].strip()
                data = response.read()
        except Exception as e:
            print(f"external image {url} could not be downloaded ({e}), keeping the github url")
            return url

        extension = CONTENT_TYPE_EXTENSIONS.get(content_type)
        if not extension:
            print(f"external image {url} has unexpected type {content_type!r}, keeping the github url")
            return url

        os.makedirs(EXTERNAL_IMAGE_DIR, exist_ok=True)
        name = f"{image_id}{extension}"
        with open(f"{EXTERNAL_IMAGE_DIR}/{name}", "wb") as fn:
            fn.write(data)
        return f"{baseurl}/assets/img/{EXTERNAL_IMAGE_SUBDIR}/{name}"

    return EXTERNAL_IMAGE_RE.sub(replace, text)

INLINE_MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
WIKI_MD_LINK_RE = re.compile(r"\[\[(?:([^\]|]*)\|)?([^\]]*)\]\]")
HTML_TAG_RE = re.compile(r"<[^>]+>")

def extract_description(md_text:str, max_length:int=160) -> str:
    # first real paragraph of the page, markdown stripped: becomes the meta
    # description (the snippet text search engines show). A leading breadcrumb
    # line ("Network functions > Impedance functions > ...") is skipped in
    # favour of the paragraph after it.
    paragraphs = []
    current = []
    in_code_fence = False
    for line in md_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_code_fence = not in_code_fence
        skip = (not stripped or in_code_fence
                or stripped.startswith(("#", "|", "!", "```", "~~~", "---", "<", ">", "- ", "* ")))
        if skip:
            if current:
                paragraphs.append(" ".join(current))
                current = []
                if len(paragraphs) >= 3:
                    break
            continue
        current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))

    def strip_markdown(text):
        text = INLINE_MD_LINK_RE.sub(lambda m: m.group(1), text)
        text = WIKI_MD_LINK_RE.sub(lambda m: m.group(1) or m.group(2), text)
        text = HTML_TAG_RE.sub("", text)
        text = text.replace("`", "").replace("**", "").replace("*", "")
        return " ".join(text.split())

    cleaned = [p for p in (strip_markdown(p) for p in paragraphs) if p]
    text = ""
    for candidate in cleaned:
        is_breadcrumb = "." not in candidate and (" > " in candidate or len(candidate) < 30)
        if not is_breadcrumb:
            text = candidate
            break
    if not text and cleaned:
        text = cleaned[0]
    if len(text) > max_length:
        text = text[:max_length].rsplit(" ", 1)[0] + "…"
    return text

def is_table_delimiter_row(line:str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) <= set("|-: ") and "-" in stripped and "|" in stripped

def insert_blank_line_before_tables(text:str) -> str:
    # github renders a table that directly follows a paragraph, kramdown needs a
    # blank line in between (otherwise the table collapses into the paragraph)
    lines = text.split("\n")
    out = []
    in_code_fence = False
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_fence = not in_code_fence
        if (not in_code_fence and i + 1 < len(lines)
                and "|" in line and not is_table_delimiter_row(line)
                and is_table_delimiter_row(lines[i + 1])
                and out and out[-1].strip() and "|" not in out[-1]):
            out.append("")
        out.append(line)
    return "\n".join(out)

def rmtree_force(path):
    # git clones contain read-only files that a plain rmtree cannot delete on Windows
    def make_writable(func, p, exc_info):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    if not os.path.isdir(path):
        return
    try:
        shutil.rmtree(path, onexc=lambda func, p, exc: make_writable(func, p, exc))
    except TypeError:  # Python < 3.12 has onerror instead of onexc
        shutil.rmtree(path, onerror=make_writable)

def lowercase_tree(root):
    # rename all files and directories below root to lowercase, deepest first
    for dir_path, dir_names, file_names in os.walk(root, topdown=False):
        for name in file_names + dir_names:
            lower_name = name.lower()
            if name != lower_name:
                os.rename(os.path.join(dir_path, name), os.path.join(dir_path, lower_name))

def make_key_from_md_filename(filename):
    base_filename =os.path.splitext(os.path.basename(filename))[0]
    key_filename = os.path.splitext(os.path.basename(filename).replace(" ", "-"))[0].lower()
    key_filename = key_filename.replace("...", "-")
    dir_name = os.path.dirname(filename)
    dir_name = dir_name.replace("\\", "/")
    dir_name = dir_name.replace("_site", "")
    return (base_filename, key_filename, dir_name)

def get_filename_key_from_md_link(md_link:str, link_open:str="[[", link_close:str="]]") -> str:
    new_md_link = md_link.replace(link_open, "")
    new_md_link = new_md_link.replace(link_close, "")
    new_md_link = new_md_link.replace("++", "--")
    new_md_link = new_md_link.replace(" + ", "---")

    split_md_link = new_md_link.split("|")
    link_alias = ""
    if len(split_md_link) > 1:
        link_alias = split_md_link[0]

    final_link = split_md_link[-1]

    key_raw = final_link
    key = final_link.replace(" ", "-")
    key = key.lower().replace("...", "-")  # same munging as make_key_from_md_filename

    if link_alias and link_alias[-1] == "\\":
        link_alias = link_alias[0:-1]

    return link_alias, key_raw, key

def find_all_internal_markdown_links(text:str):
    return re.findall(r"\[\[[^\[\]\v]+\]\]",text)

def find_all_external_markdown_links(text:str):
    return re.findall(r"\[[^\[\]\v]+\]",text)

def generate_md_header(base_name:str, name:str, parent, level:int, has_children:bool, is_in_navigation:bool, description:str=""):
    display_name = base_name.replace("-", " ")

    header  = "---\n"
    header += f"title: {display_name}\n"
    header += f"layout: default\n"
    if description:
        header += f"description: {json.dumps(description, ensure_ascii=False)}\n"

    if has_children:
        header += "has_children: true\n"
        header += "nav_fold : true\n"

    if (parent):
        display_parent_name = parent[1].replace("-", " ")
        header += f"parent: {display_parent_name}\n"

    if not is_in_navigation and not "home" in name:
        header += "nav_exclude: true\n"
    else:
        header += f"nav_order: {level}\n"


    header += "---\n"

    return header

def clean_md_file(md_fn_raw, md_fldr_out, wiki_file_dict, wiki_image_dict, navigation_structure, baseurl="", all_file_dicts=None):
    base_name, name, dir_name = make_key_from_md_filename(md_fn_raw)
    display_name = base_name.replace("-", " ")
    is_in_navigation = name in navigation_structure
    parent, level, has_children = ["", 0, False]
    if (is_in_navigation):
        parent, level, has_children = navigation_structure[name]

    with open(md_fn_raw, "r", encoding="utf-8") as fn:
        names_with_big_tables_and_sup = {"value-type":True, "null":True}

        text = fn.read()

        cleaned_text = insert_blank_line_before_tables(text)
        cleaned_text = localize_external_images(cleaned_text, baseurl)
        if all_file_dicts:
            cleaned_text = rewrite_cross_wiki_links(cleaned_text, all_file_dicts)

        links = find_all_internal_markdown_links(cleaned_text)

        if (name in names_with_big_tables_and_sup):
            cleaned_text = cleaned_text.replace("<sup>", "")
            cleaned_text = cleaned_text.replace("</sup>", "")

        for link in links:
            link_alias, key_raw, key = get_filename_key_from_md_link(link)
            # [[alias|page#section]] links to a heading; keys STARTING with '#'
            # (the geodms '#' operator page) are kept whole
            page_key, _, anchor_part = key.partition("#")
            anchor = ""
            if page_key:
                key = page_key
                if anchor_part:
                    anchor = f"#{anchor_part}"
            key_is_in_files = key in wiki_file_dict
            key_is_in_images = key in wiki_image_dict

            if key_is_in_files:
                # [[attribute]] -> [attribute](docs/attribute)
                if not link_alias:
                    link_alias = key
                if "home" in name:
                    key = f"docs/{key}"
                cleaned_text = cleaned_text.replace(link, f"[{link_alias}]({key}.html{anchor})")
            elif key_is_in_images:
                # [[images/GUI/qt.png]] -> ![qt](<baseurl>/assets/img/GUI/qt.png)
                filename, ext = os.path.splitext(key)
                image_name = pathlib.Path(filename).stem + ext

                mid_path = key.replace("images/", "")
                mid_path = mid_path.replace(image_name, "")

                cleaned_text = cleaned_text.replace(link, f"![{link_alias}]({baseurl}/assets/img/{mid_path}{image_name})")
            else:
                print(f"{link} {key} {md_fn_raw} is not in dict")
    description = extract_description(cleaned_text)
    header = generate_md_header(base_name, name, parent, level, has_children, is_in_navigation, description)
    cleaned_text = f"{header}# **{display_name}**\n{cleaned_text}"
    output_filename = f"{md_fldr_out}/{name}.md"
    with open(output_filename, "w", encoding="utf8") as f:
        f.write(cleaned_text)


    return {"output_filename": output_filename, "key": name, "title": display_name, "description": description}

def clean_html_files(html_folder:str, baseurl:str=""):
    html_files = glob.glob(f"{html_folder}/**/*.html", recursive=True)
    for html_file in html_files:
        clean_html_file(html_file, baseurl=baseurl)

def clean_html_file(html_fn_raw:str, set_nav_tabs_open:bool=True, convert_paths_for_local_use:bool=False, remove_jekyll_header_part=False, baseurl:str=""):
    text = ""
    with open(html_fn_raw, "r", encoding="utf-8") as fn:
        text = fn.read()

    prefix = "../"
    is_index_page = os.path.basename(html_fn_raw) == "index.html"
    if is_index_page:
        prefix = ""

    if (convert_paths_for_local_use):
        text = text.replace('<a href="/"', f'<a href="{prefix}index.html"')
        text = text.replace("/assets", f"{prefix}assets")
        text = text.replace("..../assets", f"../assets")
        text = text.replace("/docs", f"docs")
        if not is_index_page:
            text = text.replace("docs/", f"")

    if (set_nav_tabs_open):
        text = text.replace('<li class="nav-list-item">', '<li class="nav-list-item active">')
        text = text.replace('aria-pressed="false"', 'aria-pressed="true"')
        text = text.replace(f'{baseurl}/favicon.ico', f'{prefix}favicon.ico')

    if remove_jekyll_header_part:
        # note: this drops the canonical url and meta description, which search
        # engines use; the deployed site keeps them (remove_jekyll_header_part=False)
        jekyll_header_start = text.find("<!-- Begin Jekyll SEO tag v2.8.0 -->")
        jekyll_header_end = text.find("<!-- End Jekyll SEO tag -->")

        if not jekyll_header_start == -1 and not jekyll_header_end == -1:
            text = text[0:jekyll_header_start] + text[jekyll_header_end+28:]

    with open(html_fn_raw, "w", encoding="utf-8") as fn:
        fn.write(text)

def get_number_of_leading_spaces(line:str) -> int:
    number_of_spaces = 0
    for c in line:
        if c != " ":
            break
        number_of_spaces+=1
    return number_of_spaces

def get_navigation_structure_from_sidebar(sidebar_fn:str):
    navigation_structure = {}
    previous_level = -1
    previous_parent = None
    parent_stack = []
    with open(sidebar_fn, encoding="utf-8") as f:
        lines = f.readlines()
        for level, line in enumerate(lines):
            level+=1
            if not line:
                continue
            if not "*" in line and not "-" in line:
                continue

            leading_spaces = get_number_of_leading_spaces(line)
            internal_links = find_all_internal_markdown_links(line)
            external_links = find_all_external_markdown_links(line)

            if not internal_links and not external_links:
                continue

            key = None
            if internal_links:
                link_alias, raw_key, key = get_filename_key_from_md_link(internal_links[0])
            else:
                # [text](target): a wiki page link takes its key from the target,
                # so text and page name may differ; http links keep the old
                # text-derived key (they have no page anyway)
                md_page_link = re.match(r".*\[([^\]\v]+)\]\(([^)\s]+)\)", line)
                if md_page_link and not md_page_link.group(2).startswith("http"):
                    target = md_page_link.group(2)
                    raw_key = target
                    key = target.replace(" ", "-").lower().replace("...", "-")
                else:
                    link_alias, raw_key, key = get_filename_key_from_md_link(external_links[0], "[", "]")

            parent = None
            if len(parent_stack):
                parent = parent_stack[-1][0]

            if leading_spaces < previous_level: # next parent
                parent = parent_stack.pop()[0]
                if not len(parent_stack):
                    parent = None

            if leading_spaces > previous_level:
                if previous_parent:
                    parent_stack.append([previous_parent, leading_spaces])
                    parent = previous_parent

            navigation_structure[key] = [parent, level, False]
            if parent:
                navigation_structure[parent[0]][2] = True

            previous_parent = [key,raw_key]
            previous_level = leading_spaces

    return navigation_structure

def generate_sitemap(output_fn):
    site_html_files = sorted(glob.glob(f"{OUT_ROOT}/**/*.html", recursive=True))
    with open(output_fn, "w", encoding="utf-8") as fn:
        for f in site_html_files:
            rel_page = os.path.relpath(f, OUT_ROOT).replace("\\", "/")
            fn.write(f"{SITE_URL}/{rel_page}\n")
    return

def generate_sitemap_xml(pages, output_fn):
    # like sitemap.txt but with the last wiki-commit date per page, so crawlers
    # can prioritize what to recrawl
    with open(output_fn, "w", encoding="utf-8") as fn:
        fn.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fn.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for page in sorted(pages, key=lambda p: p["url"]):
            fn.write(f"  <url>\n    <loc>{xml_escape(page['url'])}</loc>\n")
            if page.get("lastmod"):
                fn.write(f"    <lastmod>{page['lastmod']}</lastmod>\n")
            fn.write("  </url>\n")
        fn.write("</urlset>\n")

def generate_indexnow(pages, out_root:str, changed_within_days:int, submit_all:bool):
    # key file, served from the site root, and the payload the workflow posts after deploy
    with open(f"{out_root}/{INDEXNOW_KEY}.txt", "w", encoding="utf-8") as fn:
        fn.write(INDEXNOW_KEY)

    if submit_all:
        urls = [p["url"] for p in pages]
    else:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=changed_within_days)).strftime("%Y-%m-%d")
        urls = [p["url"] for p in pages if p.get("lastmod") and p["lastmod"] >= cutoff]

    payload = {
        "host": SITE_URL.split("//", 1)[-1],
        "key": INDEXNOW_KEY,
        "keyLocation": f"{SITE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": sorted(urls),
    }
    with open(INDEXNOW_PAYLOAD_FILE, "w", encoding="utf-8") as fn:
        json.dump(payload, fn, indent=1)
    print(f"indexnow: {len(urls)} url(s) queued in {INDEXNOW_PAYLOAD_FILE}")

def generate_security_txt(output_fn):
    # https://www.rfc-editor.org/rfc/rfc9116 — Expires is mandatory; it is refreshed on
    # every build, so it cannot go stale while the site is still being rebuilt.
    expires = datetime.now(timezone.utc).replace(microsecond=0) + timedelta(days=365)
    os.makedirs(os.path.dirname(output_fn), exist_ok=True)
    with open(output_fn, "w", encoding="utf-8") as fn:
        for contact in SECURITY_CONTACTS:
            fn.write(f"Contact: {contact}\n")
        fn.write(f"Expires: {expires.strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
        fn.write("Preferred-Languages: nl, en\n")
        fn.write(f"Canonical: {SITE_URL}/.well-known/security.txt\n")

def generate_llms_txt(pages, output_fn):
    # https://llmstxt.org/: a markdown index of the documentation, as a clean
    # entry point for llm crawlers
    with open(output_fn, "w", encoding="utf-8") as fn:
        fn.write("# geodms.nl documentation\n\n")
        fn.write("> GeoDMS is an open-source platform for building large, fast and transparent "
                 "spatial models. This site documents GeoDMS itself and models built with it. "
                 "The content is converted from the project github wikis; every page listed "
                 "below is plain static html.\n")
        for site_name, site in SITES.items():
            site_pages = [p for p in pages if p["site"] == site_name]
            if not site_pages:
                continue
            fn.write(f"\n## {site['title']}\n\n")
            for page in sorted(site_pages, key=lambda p: p["url"]):
                description = f": {page['description']}" if page["description"] else ""
                fn.write(f"- [{page['title']}]({page['url']}){description}\n")

def ensure_wiki(site_name:str, reclone_wiki:bool=True):
    wiki_dir = f"wikis/{site_name}"
    if reclone_wiki:
        rmtree_force(wiki_dir)
    if not os.path.isdir(wiki_dir):
        os.makedirs("wikis", exist_ok=True)
        # blob:none: current files plus the full commit history (for sitemap
        # lastmod dates) without downloading any historic file contents
        subprocess.run(["git", "clone", "--filter=blob:none", SITES[site_name]["wiki_git_url"], wiki_dir], check=True)

def collect_last_modified(wiki_dir:str) -> dict:
    # last commit date (yyyy-mm-dd) per file, repo-relative posix paths; one git
    # log pass, newest first, so the first date seen per file wins. Empty on a
    # shallow clone: every file then just reports the single visible commit.
    result = {}
    log = subprocess.run(["git", "-C", wiki_dir, "-c", "core.quotepath=false", "log", "--format=\x01%cs", "--name-only"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    if log.returncode != 0:
        return result
    current_date = None
    for line in log.stdout.splitlines():
        if line.startswith("\x01"):
            current_date = line[1:]
            continue
        line = line.strip()
        if line and current_date and line not in result:
            result[line] = current_date
    return result

def collect_site_dicts(site_name:str):
    # returns (wiki_md_files, wiki_file_dict, wiki_image_dict, navigation_structure)
    wiki_dir = f"wikis/{site_name}"

    wiki_image_dict = {}
    if os.path.isdir(f"{wiki_dir}/images"):
        wiki_image_files = glob.glob(f"{wiki_dir}/images/**", recursive=True)
        for file in wiki_image_files:
            base_name, name, dir_name = make_key_from_md_filename(file)
            if not name:
                continue

            name = file.replace("\\", "/").replace(f"{wiki_dir}/images/", "")
            name = "images/" + name

            wiki_image_dict[name.lower()] = file

    wiki_file_dict = {}
    navigation_structure = {}
    wiki_md_files = glob.glob(f"{wiki_dir}/**/*.md", recursive=True)
    for file in wiki_md_files:
        base_name, name, dir_name = make_key_from_md_filename(file)
        wiki_file_dict[name] = file

        if "_Sidebar" in file:
            navigation_structure = get_navigation_structure_from_sidebar(file)
            continue

        if "_Footer" in file:
            continue

    return (wiki_md_files, wiki_file_dict, wiki_image_dict, navigation_structure)

def build_site(site_name:str, dicts_by_site:dict, run_jekyll:bool=True):
    site = SITES[site_name]
    baseurl = site["baseurl"]
    wiki_dir = f"wikis/{site_name}"
    wiki_md_files, wiki_file_dict, wiki_image_dict, navigation_structure = dicts_by_site[site_name]
    all_file_dicts = {name: dicts[1] for name, dicts in dicts_by_site.items()}

    # reset the generated template inputs of the previous site
    docs_folder = f"{TEMPLATE_DIR}/docs"
    rmtree_force(docs_folder)
    rmtree_force(f"{TEMPLATE_DIR}/assets/img")
    if os.path.isfile(f"{TEMPLATE_DIR}/index.md"):
        os.remove(f"{TEMPLATE_DIR}/index.md")
    os.mkdir(docs_folder)

    # copy wiki images (if any) to /assets/img folder, all lowercase
    if os.path.isdir(f"{wiki_dir}/images"):
        shutil.copytree(f"{wiki_dir}/images", f"{TEMPLATE_DIR}/assets/img")
        lowercase_tree(f"{TEMPLATE_DIR}/assets/img")

    # convert links in each file, collecting page records for sitemap.xml/llms.txt.
    # downloaded external images are copied in afterwards, once they are all known.
    last_modified = collect_last_modified(wiki_dir)
    pages = []
    for file in wiki_md_files:
        record = clean_md_file(file, f"{TEMPLATE_DIR}/docs", wiki_file_dict, wiki_image_dict, navigation_structure, baseurl, all_file_dicts)
        is_home = "home" in record["output_filename"]
        if is_home:
            shutil.move(record["output_filename"], f"{TEMPLATE_DIR}/index.md")

        if record["key"].startswith("_"):  # _Sidebar/_Footer, not rendered by jekyll
            continue
        if is_home:
            record["url"] = f"{SITE_URL}{baseurl}/"
        else:
            record["url"] = f"{SITE_URL}{baseurl}/docs/{urllib.parse.quote(record['key'])}.html"
        rel_source = os.path.relpath(file, wiki_dir).replace("\\", "/")
        record["lastmod"] = last_modified.get(rel_source)
        record["site"] = site_name
        pages.append(record)

    # serve the downloaded github-hosted images from our own assets folder
    if os.path.isdir(EXTERNAL_IMAGE_DIR):
        shutil.copytree(EXTERNAL_IMAGE_DIR, f"{TEMPLATE_DIR}/assets/img/{EXTERNAL_IMAGE_SUBDIR}", dirs_exist_ok=True)

    if not run_jekyll:
        return pages

    # run jekyll: base config plus the per-site overlay (title, baseurl, links)
    configs = "_config.yml"
    if os.path.isfile(f"{TEMPLATE_DIR}/_config_{site_name}.yml"):
        configs += f",_config_{site_name}.yml"

    dest = f"../{OUT_ROOT}{baseurl}"
    jekyll_result = subprocess.run(f"bundle exec jekyll build --config {configs} -d {dest}", shell=True, cwd=TEMPLATE_DIR)
    if jekyll_result.returncode != 0:
        sys.exit(f"jekyll build of {site_name} failed with exit code {jekyll_result.returncode}")

    clean_html_files(f"{OUT_ROOT}{baseurl}", baseurl)
    return pages

if __name__=="__main__":
    parser = argparse.ArgumentParser(description=f"Convert the Github wikis of {', '.join(SITES)} to one static html site in {OUT_ROOT}/.")
    parser.add_argument("--sites", default=",".join(SITES), help="comma-separated subset of sites to (re)build, default all")
    parser.add_argument("--serve", action="store_true", help=f"serve {OUT_ROOT}/ locally on port 8000 afterwards")
    parser.add_argument("--skip-clone", action="store_true", help="reuse existing wiki clones instead of recloning")
    parser.add_argument("--skip-jekyll", action="store_true", help="only preprocess markdown into template/docs, skip jekyll and deployment output")
    parser.add_argument("--indexnow-days", type=int, default=2, help="queue pages whose wiki page changed within this many days for IndexNow (default 2)")
    parser.add_argument("--indexnow-all", action="store_true", help="queue every page for IndexNow instead of only recently changed ones")
    args = parser.parse_args()

    selected = [s.strip() for s in args.sites.split(",") if s.strip()]
    unknown = [s for s in selected if s not in SITES]
    if unknown:
        sys.exit(f"unknown site(s) {unknown}, choose from {list(SITES)}")

    run_jekyll = not args.skip_jekyll
    if run_jekyll and set(selected) == set(SITES):
        rmtree_force(OUT_ROOT)  # full build starts clean; partial builds only touch their own subdir

    # all wikis are cloned and indexed, also outside --sites: rewriting the
    # cross-wiki links of any site needs the page lists of all of them
    for site_name in SITES:
        ensure_wiki(site_name, reclone_wiki=not args.skip_clone)
    dicts_by_site = {site_name: collect_site_dicts(site_name) for site_name in SITES}

    # the root site must build first: jekyll cleans its destination (_out itself),
    # keep_files in _config.yml protects the subsite dirs on partial rebuilds
    all_pages = []
    for site_name in [s for s in SITES if s in selected]:
        all_pages += build_site(site_name, dicts_by_site, run_jekyll=run_jekyll)

    if run_jekyll:
        generate_sitemap(f"{OUT_ROOT}/sitemap.txt")
    if set(selected) == set(SITES):  # partial builds would produce incomplete files
        os.makedirs(OUT_ROOT, exist_ok=True)
        generate_sitemap_xml(all_pages, f"{OUT_ROOT}/sitemap.xml")
        generate_llms_txt(all_pages, f"{OUT_ROOT}/llms.txt")
        generate_security_txt(f"{OUT_ROOT}/.well-known/security.txt")
        generate_indexnow(all_pages, OUT_ROOT, args.indexnow_days, args.indexnow_all)

    if args.serve:
        subprocess.run([sys.executable, "-m", "http.server", "8000"], cwd=OUT_ROOT)
