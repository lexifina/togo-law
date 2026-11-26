# Structure

| Dossier | Contenu |
| --- | --- |
| `constitution/` | La Constitution du 6 mai 2024 (Ve République) |
| `constitution-<année>/` | Une constitution antérieure, telle que publiée (par ex. `constitution-1992/`) |
| `codes/<code>/` | Un code en vigueur, tel que publié par sa loi ou ordonnance (par ex. `codes/code-penal/`, `codes/code-des-personnes-et-de-la-famille/`) |
| `codes/<code>-<année>/` | Un code antérieur remplacé par un code plus récent du même nom (par ex. `codes/code-du-travail-2006/`) |
| `lois/<année>/<année>-<n°>-<objet>/` | Une loi (loi organique, loi de finances, loi de ratification, loi modificative ...) |
| `ordonnances/<année>/...` | Une ordonnance |
| `decrets/<année>/...` | Un décret |
| `arretes/<année>/...` | Un arrêté (ministériel, interministériel ...) |
| `decisions/<année>/...` | Une décision publiée au Journal officiel |

L'année est celle de la signature. Quand une année compte plus de 990 actes d'un même type, elle est divisée par mois
(`decrets/<année>/<mois>/...`). Aucun dossier ne compte plus de 1 000 entrées.

Chaque acte est un dossier : `preambule.md` (titre et visas), un fichier par article (`art-001.md` ; `art-012-bis.md`),
`signatures.md` (formule finale et signatures) et un `README.md` (Journal officiel, page, date d'entrée en vigueur).
Un acte sans articles est dans `texte.md`. Un code de plus de 990 articles range ses articles par tranches de 500
(`art-1000-1499/art-1205.md`).

## Dates

Chaque acte est un commit, daté à 12 h 00 (Lomé, UTC) du jour de son entrée en vigueur, que répète le trailer
`In-force:`. `In-force-basis:` dit d'où vient ce jour :

- le texte lui-même, quand il fixe son entrée en vigueur (« entre en vigueur à compter de sa signature / de sa
  publication / du 1er janvier ... ») ;
- sinon, pour une loi ou une ordonnance, sa promulgation (date de signature) ;
- sinon, pour un décret, un arrêté ou une décision, sa publication au Journal officiel.

Un acte dont l'entrée en vigueur est différée (délai, date fixée par un texte ultérieur) ou dont les dates se
contredisent n'est pas encore versé. Avant 1970, que git ne sait pas dater, le commit est daté du 1er janvier 1970 et le
vrai jour est dans le sujet et le trailer `In-force:`. Aucune date n'est le jour où nous avons téléchargé le texte.

Les mesures individuelles (nominations, carrières, distinctions) ne sont pas versées : ce ne sont pas des règles.

---

# Structure (English)

`constitution/` holds the Constitution of 6 May 2024; `constitution-<year>/` an earlier constitution; `codes/<code>/` a
code in force as its enacting law published it, `codes/<code>-<year>/` an earlier code it replaced; every other act is
filed by type and year of signature: `lois/`, `ordonnances/`, `decrets/`, `arretes/`, `decisions/`. One file per
article. Each commit is dated noon Lomé on the day the act took effect: the day the text sets, else promulgation for a
law or ordinance, else publication in the Journal officiel for a regulatory act. Acts with deferred or contradictory
dates are held; individual measures (appointments, careers, honours) are left out.
