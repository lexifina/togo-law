# How this repository was made (Togo)

## Source

Every act comes from the Journal officiel de la République togolaise platform, <https://new.jo.gouv.tg>, through the
public JSON API its own pages call, `https://odoo.jo.gouv.tg/api/journal-officiel/`:

- `journals?limit=20&offset=0&date_from=<day>&date_to=<day>`: the issues published in a window, each with its text
  (`texte_extrait`, the platform's own text of the issue) and its list of acts (`publications`: number, title, signature
  date, first page). Windows are months, split in two while they hold more than 20 issues (the API's paging order is
  not stable, so pages are never chained).
- `publications/<id>`: one act's record (the `Source-api` trailer of each commit).

new.jo.gouv.tg's robots.txt says `Disallow: /`; robots.txt is advisory for this work (Lexifina's decision,
2026-11-08). Requests are paced: one in flight, about one a second, one more slot after ten clean minutes (at most
three), back to one at the first timeout or 5xx. No CAPTCHA, login or block was met or got round. The platform's terms
forbid commercial copying without written permission; this repository is free and non-commercial (see LICENSE).

Earlier acts (Constitution 2024, Loi 2019-014, Code du travail 2021 and Loi 2022-019) came from the old jo.gouv.tg PDFs
in October 2026; their history is kept, and the folders were moved by a pure-rename commit.

## Build

`runner/tg_fetch.py` (fetch, in the Lexifina scripts repository) and `runner/tg_build.py` (build): each issue's text is
cut into its acts at their heading lines ("Loi n° 2015-010 du ...", "Décret n° 2026-192/PC du ..."), matched to the
platform's list by number (or, when the platform's number is wrong, by type and signature day); each act into articles
("Article premier :", "Art. 2 :"), with the title and visas in `preambule.md` and the closing formula and signatures in
`signatures.md`. Running heads, page numbers and division headings between articles are dropped; nothing else is
changed: the publisher's OCR errors stay. No OCR of our own; no AI model writes, translates or corrects any legal text.

Commits are appended to `main` by `git fast-import`, fast-forward only, one per act, dated as STRUCTURE.md says.

## Not included

- individual measures (appointments, careers, honours, individual licences and approvals);
- court decisions printed in the Journal officiel (Cour constitutionnelle, Cour suprême): case law, kept for a
  separate repository;
- acts whose entry into force is deferred (a delay, a later act) or whose dates contradict each other;
- acts whose heading the issue text does not show, and issues the platform gives no text for.
