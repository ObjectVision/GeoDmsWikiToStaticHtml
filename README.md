# Intro
Github wiki content is generally not allowed to be indexed by third-parties like Google Search. GeoDmsWikiToStaticHtml is a tool to convert public Github wiki content to static html content. This allows the wiki content to be duplicated neatly and served at a location that allows for indexing, while keeping the source in one location.

The result is served at https://www.geodms.nl. Major thanks to [just the docs](https://just-the-docs.com/) for their awesome template.

# Automatic deployment (recommended)
The Github Actions workflow [.github/workflows/build-and-deploy.yml](.github/workflows/build-and-deploy.yml) builds the site and deploys it to geodms.nl over FTPS. No local installation is needed.

It runs:
- **nightly** (03:17 UTC),
- **on demand**: Actions tab -> *Build and deploy geodms.nl* -> *Run workflow*. Tick *dry run* to only build and inspect the result as a downloadable artifact, without deploying.
- **on every wiki edit**, if the optional trigger [extra/wiki-updated-trigger-for-GeoDMS-repo.yml](extra/wiki-updated-trigger-for-GeoDMS-repo.yml) is installed in the ObjectVision/GeoDMS repository (see the comments in that file).

One-time setup, in this repository under *Settings -> Secrets and variables -> Actions*:

| Kind     | Name             | Value                                              |
|----------|------------------|----------------------------------------------------|
| Secret   | `FTP_SERVER`     | hostname of the webserver                          |
| Secret   | `FTP_USERNAME`   | ftp account name                                   |
| Secret   | `FTP_PASSWORD`   | ftp account password                               |
| Variable | `FTP_SERVER_DIR` | optional; remote deploy dir, default `public_html/` |

The deploy action ([SamKirkland/FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action)) keeps a state file (`.ftp-deploy-sync-state.json`) on the server so subsequent deploys only transfer changed files. It never deletes files it did not upload itself, so hand-placed files (e.g. `.htaccess`) are left alone; pages removed from the wiki linger on the server until removed by hand.

# Local usage
Requirements: [Python](https://www.python.org/downloads/), [Ruby](https://jekyllrb.com/docs/installation/) and the Jekyll and Bundler gems (`gem install jekyll bundler`, then `bundle install` inside `template/`).

```
python convert_wiki_to_static_html.py [--serve] [--skip-clone] [--skip-jekyll] [--wiki-url <git url>]
```

This will:
- clone the wiki repository into `wiki/` (`--skip-clone` reuses an existing clone, `--wiki-url` converts another wiki)
- parse `_Sidebar.md` and use it as navigation bar
- convert internal `[[ ]]` image and file links to `[]()` format, into `template/docs/`
- run `bundle exec jekyll build` (`--skip-jekyll` stops before this step), producing the site in `template/_site/`
- with `--serve`: serve the result at http://localhost:8000

To upload a locally built site to the webserver, store a WinSCP site with the ftp credentials once and run:

```
.\deploy_local_winscp.ps1 -Site "<stored WinSCP site name>"
```

# Notes
- `template/Gemfile.lock` is pinned to the Windows platform (`x64-mingw-ucrt`); the CI workflow therefore uses a windows runner. To build on Linux, run `bundle lock --add-platform x86_64-linux` in `template/` and commit the lockfile.
- Documentation content is distributed under CC BY-SA 4.0; this tool under GNU GPL-3.
