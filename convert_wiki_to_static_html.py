import os
import glob
import shutil
import re
import pathlib

def make_key_from_md_filename(filename):
    return os.path.splitext(os.path.basename(filename).replace(" ", "-"))[0].lower()

def get_filename_key_from_md_link(md_link:str, link_open:str="[[", link_close:str="]]") -> str:
    new_md_link = md_link.replace(link_open, "")
    new_md_link = new_md_link.replace(link_close, "")
    new_md_link = new_md_link.replace("++", "--")
    new_md_link = new_md_link.replace(" + ", "---")

    split_md_link = new_md_link.split("|")
    link_alias = ""
    if len(split_md_link) > 2:
        link_alias = split_md_link[0]

    final_link = split_md_link[-1]
    final_link = final_link.split("/")
    final_link = final_link[-1]
    key = final_link.replace(" ", "-")
    
    return link_alias, key.lower()

def find_all_internal_markdown_links(text:str):
    return re.findall(r"\[\[[^\[\]\v]+\]\]",text)

def find_all_external_markdown_links(text:str):
    return re.findall(r"\[[^\[\]\v]+\]",text)

def generate_md_header(name:str, parent:str, level:int, has_children:bool, is_in_navigation:bool):
    header  = "---\n"
    header += f"title: {name}\n"
    header += f"layout: default\n"

    if has_children:
        header += "has_children: true\n"

    if (parent):
        header += f"parent: {parent}\n"

    if not is_in_navigation:
        header += "nav_exclude: true\n"
    else:
        header += f"nav_order: {level}\n"


    header += "---\n"

    #---
    #title: GeoDMS
    #layout: home
    #---

    return header

def clean_md_file(md_fn_raw, md_fldr_out, wiki_file_dict, wiki_image_dict, navigation_structure):
    name = make_key_from_md_filename(md_fn_raw)
    if (name=="software"):
        i = 0
    is_in_navigation = name in navigation_structure
    parent, level, has_children = ["", 0, False]
    if (is_in_navigation):
        parent, level, has_children = navigation_structure[name]


    header = generate_md_header(name, parent, level, has_children, is_in_navigation)
    if (is_in_navigation):
        j = 0

    with open(md_fn_raw, "r", encoding="utf-8") as fn:
        text = fn.read()
        links = find_all_internal_markdown_links(text)

        cleaned_text = f"{header}{text}"

        for link in links:
            link_alias, key = get_filename_key_from_md_link(link)
            key_is_in_files = key in wiki_file_dict 
            key_is_in_images = key in wiki_image_dict

            if key_is_in_files:
                # [[attribute]] -> [attribute](docs/attribute)
                if not link_alias:
                    link_alias = key
                cleaned_text = cleaned_text.replace(link, f"[{link_alias}]({key})")
            elif key_is_in_images:
                # [[images/GUI/qt.png]] -> ![qt](assets/img/GUI/qt.png)
                cleaned_text = cleaned_text.replace(link, f"![{link_alias}](assets/img/GUI/{key})")
            else: 
                print(f"{link} {key} {md_fn_raw} is not in dict")

    with open(f"{md_fldr_out}/{name}.md", "w", encoding="utf8") as f:
        f.write(cleaned_text)


    return

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
    with open(sidebar_fn) as f:
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
                link_alias, key = get_filename_key_from_md_link(internal_links[0])
            else:
                link_alias, key = get_filename_key_from_md_link(external_links[0], "[", "]")
            
            if "annex" in key: 
                j  = 0


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
                navigation_structure[parent][2] = True

            previous_parent = key
            previous_level = leading_spaces

    return navigation_structure

def convert_wiki_to_static_html():
    # params
    wiki_git_url = "https://github.com/ObjectVision/GeoDMS.wiki.git"
    wiki_dir = "wiki"
    wiki_dir_cleaned = "wiki_dir_cleaned"
    navigation_md_file = "_Sidebar.md"

    reclone_wiki = False
    if reclone_wiki:
        # remove old wiki dir
        if os.path.isdir(wiki_dir):
            os.system(f"rmdir {wiki_dir} /s /q")
        # clone wiki
        os.system(f"git clone {wiki_git_url} {wiki_dir}")

    # remove old cleaned wiki dir
    if os.path.isdir(wiki_dir_cleaned):
        os.system(f"rmdir {wiki_dir_cleaned} /s /q")

    # output
    os.mkdir(wiki_dir_cleaned)
    os.mkdir(f"{wiki_dir_cleaned}/assets")
    os.mkdir(f"{wiki_dir_cleaned}/docs")

    # copy wiki md files to docs
    #shutil.copytree(f"{wiki_dir}/*.md", f"{wiki_dir_cleaned}/docs")

    # copy wiki images to /assets/img folder
    shutil.copytree(f"{wiki_dir}/images", f"{wiki_dir_cleaned}/assets/img")

    wiki_image_dict = {}
    wiki_image_files =  glob.glob(f"{wiki_dir}/images/**", recursive=True)
    for file in wiki_image_files:
        name = make_key_from_md_filename(file)
        if not name:
            continue
        ext = os.path.splitext(file)[1]
        name = name + ext
        wiki_image_dict[name] = file

    # create wiki file dict
    wiki_file_dict = {}
    wiki_md_files = glob.glob(f"{wiki_dir}/**/*.md", recursive=True)
    for file in wiki_md_files:
        name = make_key_from_md_filename(file)
        wiki_file_dict[name] = file

        if "_Sidebar" in file:
            navigation_structure = get_navigation_structure_from_sidebar(file)
            continue

        if "_Footer" in file:
            print("TODO: implement _Footer parsing.")
            continue

        if "Home" in file:
            shutil.copy(file, f"{wiki_dir_cleaned}/index.md")
            continue

        #shutil.copy(file, f"{wiki_dir_cleaned}/docs/{name}.md")

    for file in wiki_md_files:
        cleaned_md_file = clean_md_file(file, f"{wiki_dir_cleaned}/docs", wiki_file_dict, wiki_image_dict, navigation_structure)

    #print(wiki_file_dict)
    print(f"num wiki md files: {len(wiki_md_files)}")

    return

if __name__=="__main__":
    convert_wiki_to_static_html()