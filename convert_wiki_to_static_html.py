import argparse
import glob
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys

DEFAULT_WIKI_GIT_URL = "https://github.com/ObjectVision/GeoDMS.wiki.git"

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

def clean_md_file(md_fn_raw, md_fldr_out, wiki_file_dict, wiki_image_dict, navigation_structure):
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
            key_is_in_files = key in wiki_file_dict
            key_is_in_images = key in wiki_image_dict

            if key_is_in_files:
                # [[attribute]] -> [attribute](docs/attribute)
                if not link_alias:
                    link_alias = key
                if "home" in name:
                    key = f"docs/{key}"
                cleaned_text = cleaned_text.replace(link, f"[{link_alias}]({key}.html)")
            elif key_is_in_images:
                # [[images/GUI/qt.png]] -> ![qt](assets/img/GUI/qt.png)
                filename, ext = os.path.splitext(key)
                image_name = pathlib.Path(filename).stem + ext

                mid_path = key.replace("images/", "")
                mid_path = mid_path.replace(image_name, "")

                cleaned_text = cleaned_text.replace(link, f"![{link_alias}](/assets/img/{mid_path}{image_name})")
            else:
                print(f"{link} {key} {md_fn_raw} is not in dict")
    cleaned_text = f"{header}# **{display_name}**\n{cleaned_text}"
    output_filename = f"{md_fldr_out}/{name}.md"
    with open(output_filename, "w", encoding="utf8") as f:
        f.write(cleaned_text)


    return output_filename

def clean_html_files(html_folder:str):
    html_files = glob.glob(f"{html_folder}/**/*.html", recursive=True)
    for html_file in html_files:
        clean_html_file(html_file)

def clean_html_file(html_fn_raw:str, set_nav_tabs_open:bool=True, convert_paths_for_local_use:bool=False, remove_jekyll_header_part=True):
    text = ""
    with open(html_fn_raw, "r", encoding="utf-8") as fn:
        text = fn.read()

    prefix = "../"
    is_index_page = "index" in html_fn_raw
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
        text = text.replace('/favicon.ico', f'{prefix}favicon.ico')

    if remove_jekyll_header_part:
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
    site_html_files = glob.glob(f"_site/**/*.html", recursive=True)
    html_pages = []
    for f in site_html_files:
        base_name, name, dir_name= make_key_from_md_filename(f)
        html_pages.append(f"https://geodms.nl{dir_name}/{base_name}.html")

    with open(output_fn, "w", encoding="utf-8") as fn:
        for page in html_pages:
            fn.write(f"{page}\n")
    return

def convert_wiki_to_static_html(serve_locally:bool=False, wiki_git_url:str=DEFAULT_WIKI_GIT_URL, reclone_wiki:bool=True, run_jekyll:bool=True):
    # params
    wiki_dir = "wiki"
    just_the_docs_template_dir = "template"

    if reclone_wiki:
        rmtree_force(wiki_dir)
        subprocess.run(["git", "clone", "--depth", "1", wiki_git_url, wiki_dir], check=True)
    elif not os.path.isdir(wiki_dir):
        sys.exit(f"wiki dir '{wiki_dir}' not found; run without --skip-clone first")

    # remove old cleaned wiki dir
    docs_folder = os.path.join(just_the_docs_template_dir, "docs")
    rmtree_force(docs_folder)
    rmtree_force(os.path.join(just_the_docs_template_dir, "assets", "img"))

    # output
    os.mkdir(docs_folder)

    # copy wiki images to /assets/img folder, all lowercase
    shutil.copytree(f"{wiki_dir}/images", f"{just_the_docs_template_dir}/assets/img")
    lowercase_tree(f"{just_the_docs_template_dir}/assets/img")

    wiki_image_dict = {}
    wiki_image_files =  glob.glob(f"{wiki_dir}/images/**", recursive=True)
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
            print("TODO: implement _Footer parsing.")
            continue

    # convert links in each file
    for file in wiki_md_files:
        cleaned_md_filename = clean_md_file(file, f"{just_the_docs_template_dir}/docs", wiki_file_dict, wiki_image_dict, navigation_structure)
        if "home" in cleaned_md_filename:
            shutil.move(cleaned_md_filename, f"{just_the_docs_template_dir}/index.md")

    # run jekyll
    current_run_dir = os.getcwd()
    os.chdir(just_the_docs_template_dir)
    try:
        if run_jekyll:
            jekyll_result = subprocess.run("bundle exec jekyll build", shell=True)
            if jekyll_result.returncode != 0:
                sys.exit(f"jekyll build failed with exit code {jekyll_result.returncode}")

            # clean html files
            clean_html_files("_site")
            generate_sitemap("_site/sitemap.txt")

        if (serve_locally):
            os.chdir("_site")
            subprocess.run([sys.executable, "-m", "http.server", "8000"])
    finally:
        os.chdir(current_run_dir)

    return

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Convert a Github wiki to a static html site (template/_site).")
    parser.add_argument("--serve", action="store_true", help="serve the generated site locally on port 8000 afterwards")
    parser.add_argument("--skip-clone", action="store_true", help="reuse the existing wiki clone instead of recloning")
    parser.add_argument("--skip-jekyll", action="store_true", help="only preprocess markdown into template/docs, skip the jekyll build")
    parser.add_argument("--wiki-url", default=DEFAULT_WIKI_GIT_URL, help="git url of the wiki to convert")
    args = parser.parse_args()

    convert_wiki_to_static_html(
        serve_locally=args.serve,
        wiki_git_url=args.wiki_url,
        reclone_wiki=not args.skip_clone,
        run_jekyll=not args.skip_jekyll,
    )
