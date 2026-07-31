# Intro
Github wiki content is generally not allowed to be indexed by third-parties like Google Search. GeoDmsWikiToStaticHtml converts public Github wikis to static html content. This allows the wiki content to be duplicated neatly and served at a location that allows for indexing (also by LLM crawlers), while keeping the source in one location.

The result is served at https://www.geodms.nl. Major thanks to [just the docs](https://just-the-docs.com/) for their awesome template.

# Sites
One run builds all wikis into a single `_out/` tree that is deployed as one whole:

| Site | Source wiki | Served at |
|---|---|---|
| GeoDMS | https://github.com/ObjectVision/GeoDMS/wiki | https://www.geodms.nl/ |
| RSopen | https://github.com/ObjectVision/RSopen/wiki | https://www.geodms.nl/rsopen/ |
| NetworkModel PBL | https://github.com/ObjectVision/NetworkModel_PBL/wiki | https://www.geodms.nl/networkmodel_pbl/ |
| CRISP | https://github.com/ObjectVision/CRISP/wiki | https://www.geodms.nl/crisp/ |
| GeoDMS Academy | https://github.com/ObjectVision/GeoDMS_Academy/wiki | https://www.geodms.nl/academy/ |

The main site links to the subsites in its navigation bar; each subsite links back. `_out/sitemap.xml` (with per-page last-modified dates from the wiki git history) and the older `_out/sitemap.txt` cover all sites — point the server's hand-placed `robots.txt` at `https://www.geodms.nl/sitemap.xml`. `_out/llms.txt` is a markdown index of all pages ([llmstxt.org](https://llmstxt.org/)), a clean entry point for llm crawlers. `_out/.well-known/security.txt` states where to report security issues ([RFC 9116](https://www.rfc-editor.org/rfc/rfc9116)); change the addresses in `SECURITY_CONTACTS` in the script.

The wikis can link to each other (and to themselves) with their normal github wiki urls, e.g. `https://github.com/ObjectVision/RSopen/wiki/Beschikbaarheid`: the converter rewrites those to the corresponding internal geodms.nl location, including `#section` anchors. Links to pages that do not exist in the target wiki are kept as github links.

**Adding a wiki:** the wiki needs a `Home.md` and a `_Sidebar.md`. Then:
1. add an entry to `SITES` in `convert_wiki_to_static_html.py` (name, wiki git url, baseurl);
2. create `template/_config_<name>.yml` with its `title`, `baseurl` and links (copy an existing overlay);
3. add the name to `keep_files` in `template/_config.yml`, and optionally a `nav_external_links` entry there so the main site links to it.

# Automatic deployment (recommended)
The Github Actions workflow [.github/workflows/build-and-deploy.yml](.github/workflows/build-and-deploy.yml) builds all sites and deploys them to geodms.nl over FTPS. No local installation is needed. On a public repository Github Actions is free of charge.

It runs:
- **nightly** (03:17 UTC) — change the `cron:` line in the workflow to alter the frequency, e.g. `"17 3 * * 1"` for weekly on Monday;
- **on demand**: Actions tab -> *Build and deploy geodms.nl* -> *Run workflow*. Tick *dry run* to only build and inspect the result as a downloadable artifact, without deploying.
- **on every wiki edit** of the GeoDMS wiki, if the optional trigger [extra/wiki-updated-trigger-for-GeoDMS-repo.yml](extra/wiki-updated-trigger-for-GeoDMS-repo.yml) is installed in the ObjectVision/GeoDMS repository (see the comments in that file).

One-time setup, in this repository under *Settings -> Secrets and variables -> Actions*:

| Kind     | Name             | Value                                              |
|----------|------------------|----------------------------------------------------|
| Secret   | `FTP_SERVER`     | hostname of the webserver                          |
| Secret   | `FTP_USERNAME`   | ftp account name                                   |
| Secret   | `FTP_PASSWORD`   | ftp account password                               |
| Variable | `FTP_SERVER_DIR` | optional; remote deploy dir, default `public_html/` |

The deploy action ([SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)) keeps a state file (`.ftp-deploy-sync-state.json`) on the server so subsequent deploys only transfer changed files. It never deletes files it did not upload itself, so hand-placed files (e.g. `.htaccess`, `robots.txt`) are left alone; pages removed from a wiki linger on the server until removed by hand.

# Local usage
Requirements: [Python](https://www.python.org/downloads/), [Ruby](https://jekyllrb.com/docs/installation/) and the Jekyll and Bundler gems (`gem install jekyll bundler`, then `bundle install` inside `template/`).

```
python convert_wiki_to_static_html.py [--sites geodms,rsopen,...] [--serve] [--skip-clone] [--skip-jekyll]
```

This will, per site:
- clone its wiki repository into `wikis/<name>` (`--skip-clone` reuses existing clones)
- parse `_Sidebar.md` and use it as navigation bar
- convert internal `[[ ]]` image and file links to `[]()` format, into `template/docs/`
- run `bundle exec jekyll build` with `_config.yml` plus the site's `_config_<name>.yml` overlay (`--skip-jekyll` stops before this step), into `_out<baseurl>`

and finally write `_out/sitemap.txt`. With `--serve` the whole result is served at http://localhost:8000. `--sites` rebuilds a subset; the other sites' output stays untouched in `_out/`.

To upload a locally built site to the webserver, store a WinSCP site with the ftp credentials once and run:

```
.\deploy_local_winscp.ps1 -Site "<stored WinSCP site name>"
```

# The page tree in the left column

By default the left column follows the wiki's own `_Sidebar.md`. A site can override that with
`nav/<site>.md` in this repo, in exactly the same syntax. The wiki then stays as its authors
left it, while the website groups the pages the way a reader of the website needs them;
`nav/geodms.md` does this for the main site. Delete the file and the wiki sidebar takes over
again.

A list item that is plain text rather than a link becomes a section: the converter writes a
stub page for it and just-the-docs fills that page with the list of its children. That is how
`Getting started`, `Reference` and `Development` exist without a wiki page behind them.

Pages that are not in the tree are still built, still reachable by url and still in the search
index; they only stay out of the menu. So a new wiki page has to be added to the tree to
appear in the left column.

# Notes
- Images pasted directly into the github wiki editor end up on github's attachment CDN instead of in the wiki's `images/` folder. The converter downloads those (cached in `_external_images/`) and serves them from `assets/img/external/`, so the site stays self-contained, leaks no visitor data to github, and can run a strict `img-src` policy. A download failure is reported and leaves the github url in place.
- After every deploy the workflow notifies [IndexNow](https://www.indexnow.org/) of the pages whose wiki source changed in the last two days, which reaches Bing, Yandex, Seznam and Naver without needing an account (Google ignores IndexNow; it uses the sitemap). Run the workflow with *indexnow_all* to submit every page once. The key in `INDEXNOW_KEY` is public by design and is served from the site root.
- Math is rendered by MathJax 3, configured in `template/assets/js/mathjax-script-type.js` (loaded before the mathjax bundle, both deferred). The wikis write inline math as `$...$`, which MathJax 3 does not recognise out of the box — without that config every inline formula shows up as raw LaTeX. Code and pre blocks are skipped by MathJax, and `\$` stays a literal dollar.
- Every page gets a meta description (the snippet text in search results) extracted from its first real paragraph; a leading breadcrumb or tag line is skipped in favour of the paragraph after it. Pages that start with only tables or images fall back to the site description.
- Non-English sites set `lang` in their `_config_<name>.yml` (RSopen: `lang: nl`).
- Github renders a markdown table that directly follows a paragraph, kramdown/Jekyll does not; the converter inserts the missing blank line so such tables render correctly here too.
- The Jekyll SEO header (canonical url, meta description) is kept in the generated pages since the whole point of this site is being indexable. `clean_html_file(..., remove_jekyll_header_part=True)` can strip it again for local file-based use.
- `template/Gemfile.lock` is pinned to the Windows platform (`x64-mingw-ucrt`); the CI workflow therefore uses a windows runner. To build on Linux, run `bundle lock --add-platform x86_64-linux` in `template/` and commit the lockfile.
- Documentation content is distributed under CC BY-SA 4.0; this tool under GNU GPL-3.
