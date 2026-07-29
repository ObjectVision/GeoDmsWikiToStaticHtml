import argparse
import glob
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys

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
        "wiki_git_url": "https://github.com/ObjectVision/GeoDMS.wiki.git",
        "baseurl": "",
    },
    "rsopen": {
        "wiki_git_url": "https://github.com/ObjectVision/RSopen.wiki.git",
        "baseurl": "/rsopen",
    },
    "networkmodel_pbl": {
        "wiki_git_url": "https://github.com/ObjectVision/NetworkModel_PBL.wiki.git",
        "baseurl": "/networkmodel_pbl",
    },
}

OUT_ROOT = "_out"
TEMPLATE_DIR = "template"

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

def generate_md_header(base_name:str, name:str, parent, level:int, has_children:bool, is_in_navigation:bool):
    display_name = base_name.replace("-", " ")

    header  = "---\n"
    header += f"title: {display_name}\n"
    header += f"layout: default\n"

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

def clean_md_file(md_fn_raw, md_fldr_out, wiki_file_dict, wiki_image_dict, navigation_structure, baseurl=""):
    base_name, name, dir_name = make_key_from_md_filename(md_fn_raw)
    display_name = base_name.replace("-", " ")
    is_in_navigation = name in navigation_structure
    parent, level, has_children = ["", 0, False]
    if (is_in_navigation):
        parent, level, has_children = navigation_structure[name]

    header = generate_md_header(base_name, name, parent, level, has_children, is_in_navigation)
    with open(md_fn_raw, "r", encoding="utf-8") as fn:
        names_with_big_tables_and_sup = {"value-type":True, "null":True}

        text = fn.read()
        links = find_all_internal_markdown_links(text)

        cleaned_text = f"{text}"

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
    cleaned_text = f"{header}# **{display_name}**\n{cleaned_text}"
    output_filename = f"{md_fldr_out}/{name}.md"
    with open(output_filename, "w", encoding="utf8") as f:
        f.write(cleaned_text)


    return output_filename

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

def build_site(site_name:str, run_jekyll:bool=True, reclone_wiki:bool=True):
    site = SITES[site_name]
    baseurl = site["baseurl"]
    wiki_dir = f"wikis/{site_name}"

    if reclone_wiki:
        rmtree_force(wiki_dir)
    if not os.path.isdir(wiki_dir):
        os.makedirs("wikis", exist_ok=True)
        subprocess.run(["git", "clone", "--depth", "1", site["wiki_git_url"], wiki_dir], check=True)

    # reset the generated template inputs of the previous site
    docs_folder = f"{TEMPLATE_DIR}/docs"
    rmtree_force(docs_folder)
    rmtree_force(f"{TEMPLATE_DIR}/assets/img")
    if os.path.isfile(f"{TEMPLATE_DIR}/index.md"):
        os.remove(f"{TEMPLATE_DIR}/index.md")
    os.mkdir(docs_folder)

    # copy wiki images (if any) to /assets/img folder, all lowercase
    wiki_image_dict = {}
    if os.path.isdir(f"{wiki_dir}/images"):
        shutil.copytree(f"{wiki_dir}/images", f"{TEMPLATE_DIR}/assets/img")
        lowercase_tree(f"{TEMPLATE_DIR}/assets/img")

        wiki_image_files = glob.glob(f"{wiki_dir}/images/**", recursive=True)
        for file in wiki_image_files:
            base_name, name, dir_name = make_key_from_md_filename(file)
            if not name:
                continue

            name = file.replace("\\", "/").replace(f"{wiki_dir}/images/", "")
            name = "images/" + name

            wiki_image_dict[name.lower()] = file

    # create wiki file dict
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

    # convert links in each file
    for file in wiki_md_files:
        cleaned_md_filename = clean_md_file(file, f"{TEMPLATE_DIR}/docs", wiki_file_dict, wiki_image_dict, navigation_structure, baseurl)
        if "home" in cleaned_md_filename:
            shutil.move(cleaned_md_filename, f"{TEMPLATE_DIR}/index.md")

    if not run_jekyll:
        return

    # run jekyll: base config plus the per-site overlay (title, baseurl, links)
    configs = "_config.yml"
    if os.path.isfile(f"{TEMPLATE_DIR}/_config_{site_name}.yml"):
        configs += f",_config_{site_name}.yml"

    dest = f"../{OUT_ROOT}{baseurl}"
    jekyll_result = subprocess.run(f"bundle exec jekyll build --config {configs} -d {dest}", shell=True, cwd=TEMPLATE_DIR)
    if jekyll_result.returncode != 0:
        sys.exit(f"jekyll build of {site_name} failed with exit code {jekyll_result.returncode}")

    clean_html_files(f"{OUT_ROOT}{baseurl}", baseurl)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description=f"Convert the Github wikis of {', '.join(SITES)} to one static html site in {OUT_ROOT}/.")
    parser.add_argument("--sites", default=",".join(SITES), help="comma-separated subset of sites to (re)build, default all")
    parser.add_argument("--serve", action="store_true", help=f"serve {OUT_ROOT}/ locally on port 8000 afterwards")
    parser.add_argument("--skip-clone", action="store_true", help="reuse existing wiki clones instead of recloning")
    parser.add_argument("--skip-jekyll", action="store_true", help="only preprocess markdown into template/docs, skip jekyll and deployment output")
    args = parser.parse_args()

    selected = [s.strip() for s in args.sites.split(",") if s.strip()]
    unknown = [s for s in selected if s not in SITES]
    if unknown:
        sys.exit(f"unknown site(s) {unknown}, choose from {list(SITES)}")

    run_jekyll = not args.skip_jekyll
    if run_jekyll and set(selected) == set(SITES):
        rmtree_force(OUT_ROOT)  # full build starts clean; partial builds only touch their own subdir

    # the root site must build first: jekyll cleans its destination (_out itself),
    # keep_files in _config.yml protects the subsite dirs on partial rebuilds
    for site_name in [s for s in SITES if s in selected]:
        build_site(site_name, run_jekyll=run_jekyll, reclone_wiki=not args.skip_clone)

    if run_jekyll:
        generate_sitemap(f"{OUT_ROOT}/sitemap.txt")

    if args.serve:
        subprocess.run([sys.executable, "-m", "http.server", "8000"], cwd=OUT_ROOT)
