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

The main site links to the subsites in its navigation bar; each subsite links back. `_out/sitemap.txt` covers all sites (the server's `robots.txt` points to it).

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

# Notes
- The Jekyll SEO header (canonical url, meta description) is kept in the generated pages since the whole point of this site is being indexable. `clean_html_file(..., remove_jekyll_header_part=True)` can strip it again for local file-based use.
- `template/Gemfile.lock` is pinned to the Windows platform (`x64-mingw-ucrt`); the CI workflow therefore uses a windows runner. To build on Linux, run `bundle lock --add-platform x86_64-linux` in `template/` and commit the lockfile.
- Documentation content is distributed under CC BY-SA 4.0; this tool under GNU GPL-3.
