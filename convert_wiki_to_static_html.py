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
    #final_link = final_link.split("/")
    #if len(final_link) > 2 and "images" in final_link[0]:
    #    final_link = '/'.join(final_link)
    #else: 
    #    final_link = final_link[-1]

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

    if not is_in_navigation and not "home" in name:
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
                filename, ext = os.path.splitext(key)
                image_name = pathlib.Path(filename).stem + ext
                
                if "home" in name:
                    cleaned_text = cleaned_text.replace(link, f"![{link_alias}](assets/img/GUI/{image_name})")
                else:
                    cleaned_text = cleaned_text.replace(link, f"![{link_alias}](../assets/img/GUI/{image_name})")
            else: 
                print(f"{link} {key} {md_fn_raw} is not in dict")

    output_filename = f"{md_fldr_out}/{name}.md"
    with open(output_filename, "w", encoding="utf8") as f:
        f.write(cleaned_text)


    return output_filename

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
    just_the_docs_template_dir = "template"
    navigation_md_file = "_Sidebar.md"

    reclone_wiki = False
    if reclone_wiki:
        # remove old wiki dir
        if os.path.isdir(wiki_dir):
            os.system(f"rmdir {wiki_dir} /s /q")
        # clone wiki
        os.system(f"git clone {wiki_git_url} {wiki_dir}")

    # remove old cleaned wiki dir
    docs_folder = f"{just_the_docs_template_dir}\\docs"
    if os.path.isdir(docs_folder):
        os.system(f"rmdir {docs_folder} /s /q")

    if os.path.isdir(f"{just_the_docs_template_dir}\\assets\\img"):
        os.system(f"rmdir {just_the_docs_template_dir}\\assets\\img /s /q")
    
    # output
    os.mkdir(f"{just_the_docs_template_dir}/docs")

    # copy wiki images to /assets/img folder
    shutil.copytree(f"{wiki_dir}/images", f"{just_the_docs_template_dir}/assets/img")

    wiki_image_dict = {}
    wiki_image_files =  glob.glob(f"{wiki_dir}/images/**", recursive=True)
    for file in wiki_image_files:
        name = make_key_from_md_filename(file)
        if not name:
            continue

        name = file.replace("wiki/images\\", "")
        name = "images/" + name.replace("\\", "/")
        
        wiki_image_dict[name.lower()] = file

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

    # convert links in each file
    for file in wiki_md_files:
        cleaned_md_filename = clean_md_file(file, f"{just_the_docs_template_dir}/docs", wiki_file_dict, wiki_image_dict, navigation_structure)
        if "home" in cleaned_md_filename:
            shutil.move(cleaned_md_filename, f"{just_the_docs_template_dir}/index.md")

    # run jekyll
    current_run_dir = os.getcwd()
    os.chdir(just_the_docs_template_dir)
    os.system("bundle exec jekyll serve")
    os.chdir(current_run_dir)

    return

if __name__=="__main__":
    convert_wiki_to_static_html()