import os
import glob
import shutil
import re
import pathlib

def make_key_from_md_filename(filename):
    base_filename =os.path.splitext(os.path.basename(filename))[0]
    key_filename = os.path.splitext(os.path.basename(filename).replace(" ", "-"))[0].lower()
    key_filename = key_filename.replace("...", "-")
    dir_name = os.path.dirname(filename)
    dir_name = dir_name.replace("_site\\\\", "")
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
    
    if link_alias and link_alias[-1] == "\\":
        link_alias = link_alias[0:-1]

    return link_alias, key_raw, key.lower()

def find_all_internal_markdown_links(text:str):
    return re.findall(r"\[\[[^\[\]\v]+\]\]",text)

def find_all_external_markdown_links(text:str):
    return re.findall(r"\[[^\[\]\v]+\]",text)

def generate_md_header(base_name:str, name:str, parent, level:int, has_children:bool, is_in_navigation:bool):
    display_name = base_name.replace("-", " ")
    
    header  = "---\n"
    header += f"title: {display_name}\n"
    header += f"layout: default\n"

    #if "home" in name:
    #    header += f"permalink: /\n"
    #else:
    #    header += f"permalink: {name}/\n"

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

    #---
    #title: GeoDMS
    #layout: home
    #---

    return header

def clean_md_file(md_fn_raw, md_fldr_out, wiki_file_dict, wiki_image_dict, navigation_structure):
    base_name, name, dir_name = make_key_from_md_filename(md_fn_raw)
    display_name = base_name.replace("-", " ")
    if (name=="software"):
        i = 0
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
                mid_path = ""
                if "/GUI/" in filename: # TODO: generalize this
                    mid_path = "/gui"

                if "/GUI/tools" in filename:
                    mid_path = "/gui/tools"
                
                mid_path = key.replace("images/", "")
                mid_path = mid_path.replace(image_name, "")

                #if "home" in name:
                cleaned_text = cleaned_text.replace(link, f"![{link_alias}](/assets/img/{mid_path}{image_name})")
                #else:
                #    cleaned_text = cleaned_text.replace(link, f"![{link_alias}](../assets/img/{mid_path}{image_name})")
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

def format_json_search_file_content(json_fn:str):
    
    #{"0": {
    #"doc": "(registry)-settings",
    #"title": "registry path",
    #"content": "The path for most of the settings in the registry is: . Computer\\HKEY_CURRENT_USER\\Software\\ObjectVision\\%ComputerName%\\GeoDMS. This means the settings are user and machine specific. Only the set of recent files is located in: . Computer\\HKEY_CURRENT_USER\\Software\\ObjectVision\\DMS\\RecentFiles . In earlier versions settings were also stored in Computer\\HKEY_CURRENT_USER\\Software\\ObjectVision\\DMS. You might find some settings here, but new GeoDMS versions do not use these anymore. ",
    #"url": "/docs/(registry)-settings.html#registry-path",
    
    lines = []
    text = ""
    with open(json_fn, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        split_line = line.split(":")
        if len(split_line) == 1:
            continue

        first_part = ""
        second_part = ""

        if len(split_line) > 0:
            first_part = f"{split_line[0]}:"
        if len(split_line) > 1:
            is_first = True
            for part in split_line[1:]:
                if is_first:
                    is_first = False
                    if part[0] == " ":
                        part = part[1:]
                second_part = f"{second_part}{part}"
            second_part = second_part.replace("\"", "")
            second_part = second_part.replace("'", "")
            second_part = second_part.replace("\n", "")
            second_part = second_part.replace(",", "")
            second_part = second_part.replace(":", "")

        second_postfix = ","
        quotes = "\""
        if second_part and second_part[-1] == "{":
            second_postfix = ""
            quotes = ""

        if "relUrl" in first_part:
            second_postfix = ""

        line = f"{first_part}{quotes}{second_part}{quotes}{second_postfix}"
        line = line.replace(":,", "")
        line = line.replace("\n", "")
        line = line.replace("'", "")
        line = line.replace("\"\"", "")
        line = line.replace("\\""", "")
        line = line.replace("\\", "/")
        line = line.replace(";", "")
        text = f"{text} {line}"
    return text + "}}"

def merge_json_into_just_the_docs_js(follow_the_docs_js_original_fn:str="_site/assets/js/just-the-docs.js"):
    search_data_formatted_line = format_json_search_file_content("_site/assets/js/search-data.json")

    js_script = ""
    with open(follow_the_docs_js_original_fn, "r", encoding="utf-8") as f:
        js_script = f.read()

    #var path = window.location.pathname;
    #var html_page_name = path.split("/").pop();
    #if (html_page_name.includes('index')) {
    #    search_data = search_data.replace(/\/docs/g, "docs");
    #}
    #else {
    #    search_data = search_data.replace(/\/docs/g, "../docs");
    #}

    replace_text = "var request = new XMLHttpRequest();\n  request.open('GET', '/assets/js/search-data.json', true);\n\n  request.onload = function(){\n    if (request.status >= 200 && request.status < 400) {\n      var docs = JSON.parse(request.responseText);\n"    
    js_script = js_script.replace(replace_text, f"let search_data = '{search_data_formatted_line}';\n  var path = window.location.pathname;\n  var html_page_name = path.split(\"/\").pop();\n  if (html_page_name.includes('index')) {{\n    search_data = search_data.replace(/\/docs/g, \"docs\");\n  }}\n  else {{\n   search_data = search_data.replace(/\\/docs/g, \"../docs\");\n}}\n var docs = JSON.parse(search_data);")
    
    replace_text = "    } else {\n      console.log('Error loading ajax request. Request status:' + request.status);\n    }\n  };\n\n  request.onerror = function(){\n    console.log('There was a connection error');\n  };\n\n  request.send();"
    js_script = js_script.replace(replace_text, "")
    
    #js_script = js_script.replace("    } else {\n      console.log('Error loading ajax request. Request status:' + request.status);\n    }\n  };", )
    with open(follow_the_docs_js_original_fn, "w", encoding="utf-8") as f:
        f.write(js_script)

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
        html_pages.append(f"https://www.geodms.nl{dir_name}/{base_name}.html")

    with open(output_fn, "w") as fn:
        for page in html_pages:
            fn.write(f"{page}\n")
    return

def convert_wiki_to_static_html(serve_locally:bool = False):
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

    # make all items lower case
    os.system(f"for /r \"{just_the_docs_template_dir}/assets/img\" %D in (.) do @for /f \"eol=: delims=\" %F in ('dir /l/b/ad \"%D\"') do @ren \"%D\%F\" \"%F\"")
    os.system(f"for /r \"{just_the_docs_template_dir}/assets/img\" %D in (.) do @for /f \"eol=: delims=\" %F in ('dir /l/b/a-d \"%D\"') do @ren \"%D\%F\" \"%F\"")

    wiki_image_dict = {}
    wiki_image_files =  glob.glob(f"{wiki_dir}/images/**", recursive=True)
    for file in wiki_image_files:
        base_name, name, dir_name = make_key_from_md_filename(file)
        if not name:
            continue

        name = file.replace("wiki/images\\", "")
        name = "images/" + name.replace("\\", "/")
        
        wiki_image_dict[name.lower()] = file

    # create wiki file dict
    wiki_file_dict = {}
    wiki_md_files = glob.glob(f"{wiki_dir}/**/*.md", recursive=True)
    for file in wiki_md_files:
        base_name, name, dir_name = make_key_from_md_filename(file)
        wiki_file_dict[name] = file

        if "_Sidebar" in file:
            navigation_structure = get_navigation_structure_from_sidebar(file)
            #print()
            #print(navigation_structure)
            #print()
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
    os.system("bundle exec jekyll build")
    
    # clean html files
    clean_html_files("_site")
    generate_sitemap("_site/sitemap.txt")
    #merge_json_into_just_the_docs_js()


    if (serve_locally):
        os.chdir("_site")
        os.system("python -m http.server 8000")
    
    #os.system("bundle exec jekyll serve")
    os.chdir(current_run_dir)

    return

if __name__=="__main__":
    serve_locally = True
    convert_wiki_to_static_html(serve_locally)