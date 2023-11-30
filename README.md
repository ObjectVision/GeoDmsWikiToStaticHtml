# Intro
Github wiki content is generally not allowed to be indexed by third-parties like Google Search. GeoDmsWikiToStaticHtml is a tool to convert public Github wiki content to static html content. This allows the wiki content to be duplicated neatly and served at a location that allows for indexing, while keeping the source in one location. 

# Installation
- [Python](https://www.python.org/downloads/)
- [Ruby](https://jekyllrb.com/docs/installation/)
- [Gems: Jekyll, Bundler](https://jekyllrb.com/docs/)

# Usage
1. git clone https://github.com/ObjectVision/GeoDmsWikiToStaticHtml.git
2. Change parameter *wiki_git_url* in convert_wiki_to_static_html.py to the a Github wiki repository of your choice
3. Change directory in terminal to GeoDmsWikiToStaticHtml
4. From command line: python convert_wiki_to_static_html.py

This will run through several steps:
- Clone the wiki repository locally
- Parse the _Sidebar.md and use it as navigation bar
- Convert internal image and file links "[[ ]]" to "[]()" format
- Run: bundle exec jekyll serve

If all went well the static html pages are build and served locally.
Major thanks to [just the docs](https://just-the-docs.com/) for their awesome template.
