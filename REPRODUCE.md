# How this repository was made (Togo)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Journal Officiel de la République togolaise | <https://jo.gouv.tg> | 2026-10-29 | 84 | Official legislation; no licence stated on jo.gouv.tg |
| Assemblée nationale du Togo (assemblee-nationale.tg), via the Internet Archive | <https://assemblee-nationale.tg/wp-content/uploads/2021/10/donnees-perso-LOI-AN.pdf> | 2026-10-28 | 2 | Official; no licence stated |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République Togolaise | 1 | 2024-05-06 to 2024-05-06 |
| `donnees-personnelles` | Loi n° 2019-014 relative à la protection des données à caractère personnel | 1 | 2019-10-30 to 2019-10-30 |
| `code-du-travail` | Code du travail (Loi n° 2021-012 du 18 juin 2021) | 2 | 2021-06-18 to 2022-11-15 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 1 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 8 tags.

## Dates

Each commit is dated at noon (Africa/Lome) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution du 6 mai 2024, art. 33: « Les lois entrent en vigueur dès leur promulgation. » Before it, no general rule on the entry into force of laws was found; each law ends « sera exécutée comme loi de l'Etat » and is dated here by its promulgation, the date of its « Fait à Lomé » line. https://jo.gouv.tg/sites/default/files/JO/JOS_06_05_2024%20-%2069%20E%20ANNEE%20N%C2%B042%20BIS%20.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/togo-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `079f29331946ccbbdf3eb72f1c4021fbb98dcaa01e84f57da7529b09e53cd5d2` (469860 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `dac078dce3ae4525ca2c4a50b36f84fff41785d7` |
| parse.py | `1949b84d0079e59ed02e3eda9c9288e16fa0e885` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

4 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 4 history commits and 8 tags (history tip `9df1367de667fe502e32d9f4ca4faf24d9034a95`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Phase 1 is the 2024 Constitution, Loi 2019-014 (data protection) and the Code du travail of 2021: each has a born-digital text in the Journal officiel. The Code pénal (Loi 2015-010) is published only as a scan with a poor OCR layer, so it is left out (no OCR). The 1992 Constitution and its revisions (2002, 2005, 2007, 2019) are a separate, repealed act and are not built yet; their JO texts are cached.
- The 2024 Constitution took effect on promulgation, 6 May 2024 (art. 33; art. 100), the day of JO 2024 n° 42 bis. Its annexed Déclaration solennelle des droits et devoirs fondamentaux is part of the law and is kept as declaration-* units, with its own opening sentence as declaration-preambule.
- Laws before 2024: no general rule on entry into force was found (the 1992 Constitution has none for laws). Each law ends « sera exécutée comme loi de l'Etat » and is dated by its promulgation, the date of its « Fait à Lomé » line: Loi 2021-012 on 18 June 2021 and Loi 2022-019 on 15 November 2022 (each published in the JO that day).
- Loi 2019-014 is titled « du 29 octobre 2019 » and printed in the JO of 29 October 2019, but signed « Fait à Lomé, le 30 octobre 2019 ». It cannot take effect before it is signed, so it is dated 30 October 2019; enacted is the signature date and published the JO date.
- Loi 2019-014 was compared word for word with the Assemblée nationale's text as adopted in plenary on 23 October 2019 (headings and article numbers aside): 5 differences: art. 56: "sénat." / "sénat ." | art. 57: "cndh ;" / "cndh;" | art. 65: "l'etat," / "l'état," | art. 72: "l'etat," / "l'état," | art. 97: "" / "délibéré et adopté le 23 octobre 2019 la présidente de l'assemblée nationale". The JO text is kept.
- Code du travail: Loi 2022-019 (JO 2022 n° 49 bis) replaces art. 190 only; that is version 2, credited to it. The JO search (by title, reference and body text, 2026-10-29) shows no other law amending the Code du travail, Loi 2019-014 or the 2024 Constitution. The newest issue on jo.gouv.tg (home page, 2026-10-29) is n° 98 bis of 23 October 2025.
- Paragraphs follow the JO layout (a blank line between paragraphs, bold heads); a line-end hyphen is removed unless the hyphenated form occurs more often than the joined form elsewhere in the same issue, or, when neither occurs, the two parts are both words of the issue, the second is ci/là/delà/même(s), or both are number words (au-delà, celle-ci, quatre-vingt-dix, sous-traite). The running heads, page numbers, chapter and section headings, the enacting formula and the signatures are left out; each article file starts « # Article N » and the article number is not repeated in the text.
- The Assemblée nationale also published the 2024 Constitution as a JO-styled PDF (uploaded May 2024, Internet Archive capture of 11 July 2024). Its text is the JO's word for word except art. 60, where it reads « nommés par le Président du Conseil des ministres sur proposition du garde des Sceaux » and the JO file on jo.gouv.tg reads « nommés par le Président du Conseil sur proposition du garde des Sceaux ». The Journal officiel is the official publication, and its wording is kept.
- The earlier first cut (preview a33a6c3) of the Constitution dropped the preamble's opening sentence and let six heading fragments into articles; this parser replaces it.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote or transcribed legal text; parsing is rule-based (parse.py).
