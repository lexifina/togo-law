# Togo: law history in git

The law of Togo as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigueur_au.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `tg/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution de la République Togolaise (Loi n° 2024-005 du 6 mai 2024), with its annexed Déclaration solennelle des droits et devoirs fondamentaux | 1 | As promulgated, in force 6 May 2024; no revision found |
| `donnees-personnelles/` | Loi n° 2019-014 relative à la protection des données à caractère personnel | 1 | As promulgated, in force 30 October 2019; no amending law found |
| `code-du-travail/` | Code du travail (Loi n° 2021-012 du 18 juin 2021) | 2 | As promulgated, in force 18 June 2021; art. 190 (maternity leave) replaced by Loi n° 2022-019, in force 15 November 2022 |

The per-act `README.md` in each folder lists every provision, how often it changed and when.

**Where the text comes from.** Every version is read from the Journal officiel de la République togolaise (jo.gouv.tg), which publishes each issue as a PDF. Issues from about 2017 on carry a born-digital text layer. The Journal officiel is the only official source online. It has no consolidated text, so each later version is built by applying the amending law, and the record shows only the history that the Journal officiel's own issues support.

**Not included yet**

- **The Constitution of 1992** and its revisions (2002, 2005, 2007, 2019). It is a separate act, repealed by the 2024 Constitution.
- **The Code pénal (Loi n° 2015-010).** The Journal officiel publishes it only as a scanned image with a poor OCR layer, and this record does not transcribe images.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 190 of the Code du travail say on 1 January 2022? | `python tools/en_vigueur_au.py 2022-01-01 code-du-travail 190` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2022-01-01T23:59:59Z" main -- code-du-travail/art-190.md):code-du-travail/art-190.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2022-01-01T23:59:59Z" main -- code-du-travail/art-190.md; git show "$($r):code-du-travail/art-190.md"` |
| Which law wrote each paragraph of art. 190? | `git blame code-du-travail/art-190.md` |
| Every change to an article, word by word | `git log -p --word-diff code-du-travail/art-190.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/loi-2022-019` (tags `law/<key>` mark each law's commit) |
| The whole Constitution on a date | `python tools/en_vigueur_au.py 2025-01-01 constitution` |
| Which law gave a provision its wording on a date | `python tools/en_vigueur_au.py --law 2023-01-01 code-du-travail 190` |

Articles of the annexed Déclaration are files such as `constitution/declaration-art-005.md`. After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Lome (UTC), on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read. The promulgation date is the `Enacted:` trailer and the Journal officiel date is the `Published:` trailer.
- **The 2024 Constitution sets the rule:** "Les lois entrent en vigueur dès leur promulgation" (art. 33). The Constitution itself was promulgated and published on 6 May 2024.
- **Before 2024** no general rule on when laws take effect was found; the 1992 Constitution has none for laws. Each law ends "sera exécutée comme loi de l'Etat" without a date of its own, so it is dated by its promulgation, the date of its "Fait à Lomé" line. The Code du travail was signed and published on 18 June 2021, and Loi 2022-019 on 15 November 2022.
- **Loi 2019-014 has two dates in its source.** It is titled "du 29 octobre 2019" and printed in the Journal officiel of 29 October 2019, but signed "Fait à Lomé, le 30 octobre 2019". A law cannot take effect before it is signed, so it is dated 30 October 2019.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Nothing dropped.** For each law, every word from its title to its signature is in a provision file, except the title, the enacting formula, the chapter and section headings, the article numbers and the signature.
- **Loi 2019-014 against a second text.** It was compared article by article with the Assemblée nationale's text as adopted in plenary on 23 October 2019 (Internet Archive copy). They agree word for word apart from spacing and one accent ("l'Etat"/"l'État").
- **The Constitution against a second copy.** The Assemblée nationale also published the Constitution as a PDF in Journal officiel layout. It matches the Journal officiel word for word except in art. 60. There it says the magistrats du parquet are appointed by "le Président du Conseil des ministres"; the Journal officiel says "le Président du Conseil". The Journal officiel is the official publication, and its wording is kept.
- **Today's text.** The Journal officiel's search (by title, reference and body text, 29 October 2026) shows no law amending the Constitution, Loi 2019-014 or the Code du travail other than Loi 2022-019. The newest issue on jo.gouv.tg is n° 98 bis of 23 October 2025, so later changes, if any, are not yet published there.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- Each act's first commit is the act as promulgated, credited to the act itself.
- The 2022 commit holds exactly art. 190 of the Code du travail, credited to Loi n° 2022-019, which replaced that article and nothing else.
- Blame credits whole lines (one paragraph per line). Within art. 190, a paragraph whose words did not change in 2022 keeps its 2021 line. Use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **Three acts only** (see above).
- **Headings** (Titre, Chapitre, Section) are left out; each file starts with "# Article N" and the article number is not repeated. Loi 2019-014 gives each article a short title ("Des définitions"), which is kept as the first line. The enacting formula and the signatures are left out.
- **Line-end hyphens.** The Journal officiel hyphenates words at line ends. The hyphen is removed when the joined word is the form used elsewhere in the same issue, and kept for real compounds (au-delà, celle-ci, quatre-vingt-dix). The rule is in REPRODUCE.md.
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

`tools/fetch.py` downloads each source once with curl. It waits 10 seconds between requests to jo.gouv.tg, the crawl delay that site's robots.txt asks for. The Assemblée nationale copies come through the Internet Archive. Every source is cached by the sha256 of its URL. `tools/parse.py` reads only the cache. It rebuilds paragraphs from the PDF layout: the Journal officiel leaves a blank line between paragraphs and sets article numbers and headings in bold. It reads each page column by column, then writes `corpus.json`. The shared builder `tools/build.py` turns that into the commits. `REPRODUCE.md` lists every source, command, tool version and decision, and the result of the hash-for-hash rebuild.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Journal Officiel de la République togolaise](https://jo.gouv.tg) | Issue PDFs (born-digital from about 2017), with a search by reference, date and text | Every version, its dates, and the search for amending laws |
| [Assemblée nationale](https://assemblee-nationale.tg) (Internet Archive copy) | Texts as adopted in plenary, and a copy of the 2024 Constitution | Checking Loi 2019-014 and the Constitution |

Legitogo (legitogo.gouv.tg) serves an expired TLS certificate and, over plain http, only a script shell with no text (checked 28 October 2026).

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Texts: Journal Officiel de la République togolaise (https://jo.gouv.tg), official texts of the Togolese Republic, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En français

Ce dépôt retrace dans git l'histoire de trois textes togolais : un fichier par article, un commit par loi à la date de son entrée en vigueur, et la loi à l'origine du texte comme auteur du commit. Il contient la Constitution du 6 mai 2024 (loi n° 2024-005) et sa Déclaration solennelle annexée, la loi n° 2019-014 relative à la protection des données à caractère personnel, et le code du travail (loi n° 2021-012 du 18 juin 2021), dont l'article 190 a été remplacé par la loi n° 2022-019 du 15 novembre 2022. Tous les textes proviennent du Journal officiel de la République togolaise. Les lois sont datées de leur promulgation : c'est la règle de l'article 33 de la Constitution de 2024, et les lois antérieures ne fixent pas d'autre date. `python tools/en_vigueur_au.py 2022-01-01 code-du-travail 190` affiche l'article 190 tel qu'il était en vigueur à cette date, et `git blame code-du-travail/art-190.md` nomme la loi à l'origine de chaque alinéa. Ce dépôt ne constitue pas un avis juridique.
