# GeoDmsWikiToStaticHtml — instructions for Claude

## What this repository is, and what it is not

This is the machinery that turns five GitHub wikis into www.geodms.nl. **It holds almost no
content of its own.** If a request is "change this sentence on geodms.nl", the change belongs
in the wiki that sentence came from, not here.

| repository | produces | what belongs there |
|---|---|---|
| the **GitHub wikis** | the text of geodms.nl | the software: how GeoDMS works, how to configure it, model documentation |
| **GeoDmsWikiToStaticHtml** (this one) | www.geodms.nl | the converter, the Jekyll template, the theme, the page tree, the deploy |
| **ObjectVisionWebsite** | www.objectvision.nl | the company: projects, clients, publications, team |

The five wikis, cloned into `wikis/` on every run:

| site | wiki | url |
|---|---|---|
| geodms | ObjectVision/GeoDMS.wiki | www.geodms.nl |
| academy | ObjectVision/GeoDMS_Academy.wiki | /academy/ |
| rsopen | ObjectVision/RSopen.wiki | /rsopen/ |
| networkmodel_pbl | ObjectVision/NetworkModel_PBL.wiki | /networkmodel_pbl/ |
| crisp | ObjectVision/CRISP.wiki | /crisp/ |

**geodms.nl documents the software; objectvision.nl carries the track record.** A list of
clients or projects belongs on objectvision.nl, and geodms.nl links to it. Do not reintroduce
one here.

## Generated, do not edit

`template/docs/`, `template/index.md`, `template/assets/img/` and `_out/` are all written by
the converter on every run. Editing them looks like it works and is thrown away on the next
build. The sources are the wikis in `wikis/` (themselves clones, so also not the place to
edit) and the template files that are not generated: `_config*.yml`, `_includes/`,
`_layouts/`, `_sass/`.

## Running it

```
python convert_wiki_to_static_html.py                       # everything
python convert_wiki_to_static_html.py --skip-clone --skip-jekyll --sites geodms
python convert_wiki_to_static_html.py --preview new         # builds under /new/
```

`--skip-jekyll` does the markdown pass only and needs no Ruby, which is the fastest way to
check what the page tree and the front matter come out as. A full run needs Ruby and
`bundle install` in `template/`.

## The page tree in the left column

By default it follows each wiki's own `_Sidebar.md`. A site can override that with
`nav/<site>.md` in this repo, same syntax; `nav/geodms.md` does. That is how geodms.nl groups
the pages the way a website reader needs them while the wiki keeps the sidebar its authors
wrote.

Two things that bite:

- The sidebar parser reads **lines, not markdown**. A wiki link written inside an HTML comment
  is still picked up and still appears in the menu.
- just-the-docs matches a child to its parent on the parent's **title**, which comes from the
  file name. A sidebar that writes `[[Data Source]]` for a page called `Data-source.md` used to
  drop that whole branch out of the menu without a word. `nav_parent_title()` handles this; if
  you touch it, check that every site still reports no orphans.

A list item that is plain text becomes a section, with a stub page generated for it, which is
how `Getting started`, `Reference` and `Development` exist without a wiki page behind them.

## The theme

just-the-docs 0.7.0, pinned in `template/Gemfile`. The look matches objectvision.nl.

- `template/_sass/custom/setup.scss` — the palette. It lives here because **all three
  stylesheet variants** (`just-the-docs-default/-dark/-light.scss`) import `custom/custom.scss`
  but each imports its own colour scheme. A variable defined only in `color_schemes/wider.scss`
  is undefined while the dark and light variants compile, and the build fails on a file the
  site does not even use. If you change the SCSS, compile all three, not just the one in use.
- `template/_sass/color_schemes/wider.scss` — the theme's own variables.
- `template/_sass/custom/custom.scss` — rules that have no variable.
- `template/_layouts/default.html` — a copy of the theme's, with the masthead added, because
  the theme has no include hook above the sidebar. Pinned to 0.7.0 along with the Gemfile.

## Deploying

Github Actions, `.github/workflows/build-and-deploy.yml`: nightly, on a wiki-updated
dispatch, or manually. Manual runs take *preview* (deploys to geodms.nl/new/, marked noindex,
no sitemap and no IndexNow) and *dry_run* (artifact only).

The deploy step is tried up to three times, with a wait in between. The webserver refuses the
connection outright now and then: `ETIMEDOUT` on the control socket while the build itself
succeeded and the same host answers from a home connection. It follows large uploads and a
later run of exactly the same job goes through, which points at the host rate limiting an
address that opens a few thousand ftp connections in a row. The objectvision.nl site sits on
the same server and never sees it, and it uploads thirty files rather than five thousand.

If all three attempts fail, `deploy_local_winscp.ps1` is the fallback: run the workflow with
*dry_run*, unpack the artifact into `_out/` and upload from a machine that is not blocked.

## Git

Commit freely, in separate commits per subject. **Never push**; the owner pushes.

Commit messages state what changed and why. They do not name colleagues and do not review
anyone's input.
