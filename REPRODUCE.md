# How this repository was made (Togo)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Journal Officiel de la République togolaise | <https://jo.gouv.tg> | 2026-10-29 | Official legislation; no licence stated on jo.gouv.tg |
| Assemblée nationale du Togo (assemblee-nationale.tg), via the Internet Archive | <https://assemblee-nationale.tg/wp-content/uploads/2021/10/donnees-perso-LOI-AN.pdf> | 2026-10-28 | Official; no licence stated |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

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

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `8f31a071598b5fc6b7f984327d28672bd1ef68c8b99ae93e7a2ae19ae1b4bc21` (469786 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

4 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Phase 1 is the 2024 Constitution, Loi 2019-014 (data protection) and the Code du travail of 2021: each has a born-digital text in the Journal officiel. The Code pénal (Loi 2015-010) is published only as a scan with a poor OCR layer, so it is left out (no OCR). The 1992 Constitution and its revisions (2002, 2005, 2007, 2019) are a separate, repealed act and are not built yet.
- The 2024 Constitution took effect on promulgation, 6 May 2024 (art. 33; art. 100), the day of JO 2024 n° 42 bis. Its annexed Déclaration solennelle des droits et devoirs fondamentaux is part of the law and is kept as declaration-* units, with its own opening sentence as declaration-preambule.
- Laws before 2024: no general rule on entry into force was found (the 1992 Constitution has none for laws). Each law ends « sera exécutée comme loi de l'Etat » and is dated by its promulgation, the date of its « Fait à Lomé » line: Loi 2021-012 on 18 June 2021 and Loi 2022-019 on 15 November 2022 (each published in the JO that day).
- Loi 2019-014 is titled « du 29 octobre 2019 » and printed in the JO of 29 October 2019, but signed « Fait à Lomé, le 30 octobre 2019 ». It cannot take effect before it is signed, so it is dated 30 October 2019; enacted is the signature date and published the JO date.
- Loi 2019-014 was compared word for word with the Assemblée nationale's text as adopted in plenary on 23 October 2019 (headings and article numbers aside): 5 differences: art. 56: "sénat." / "sénat ." | art. 57: "cndh ;" / "cndh;" | art. 65: "l'etat," / "l'état," | art. 72: "l'etat," / "l'état," | art. 97: "" / "délibéré et adopté le 23 octobre 2019 la présidente de l'assemblée nationale". The JO text is kept.
- Code du travail: Loi 2022-019 (JO 2022 n° 49 bis) replaces art. 190 only; that is version 2, credited to it. The JO search (by title, reference and body text, 2026-10-29) shows no other law amending the Code du travail, Loi 2019-014 or the 2024 Constitution. The newest issue on jo.gouv.tg (home page, 2026-10-29) is n° 98 bis of 23 October 2025.
- Paragraphs follow the JO layout (a blank line between paragraphs, bold heads); a line-end hyphen is removed unless the hyphenated form occurs more often than the joined form elsewhere in the same issue, or, when neither occurs, the two parts are both words of the issue, the second is ci/là/delà/même(s), or both are number words (au-delà, celle-ci, quatre-vingt-dix, sous-traite). The running heads, page numbers, chapter and section headings, the enacting formula and the signatures are left out; each article file starts « # Article N » and the article number is not repeated in the text.
- The Assemblée nationale also published the 2024 Constitution as a JO-styled PDF (uploaded May 2024, Internet Archive capture of 11 July 2024). Its text is the JO's word for word except art. 60, where it reads « nommés par le Président du Conseil des ministres sur proposition du garde des Sceaux » and the JO file on jo.gouv.tg reads « nommés par le Président du Conseil sur proposition du garde des Sceaux ». The Journal officiel is the official publication, and its wording is kept.
- The earlier first cut (preview a33a6c3) of the Constitution dropped the preamble's opening sentence and let six heading fragments into articles; this parser replaces it.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote or transcribed legal text; parsing is rule-based.
