# Structure

| Dossier | Contenu |
| --- | --- |
| `constitution/` | La Constitution du 6 mai 2024 (Ve RÃ©publique) |
| `constitution-<annÃ©e>/` | Une constitution antÃ©rieure, telle que publiÃ©e (par ex. `constitution-1992/`) |
| `codes/<code>/` | Un code en vigueur, tel que publiÃ© par sa loi ou ordonnance (par ex. `codes/code-penal/`, `codes/code-des-personnes-et-de-la-famille/`) |
| `codes/<code>-<annÃ©e>/` | Un code antÃ©rieur remplacÃ© par un code plus rÃ©cent du mÃªme nom (par ex. `codes/code-du-travail-2006/`) |
| `lois/<annÃ©e>/<annÃ©e>-<nÂ°>-<objet>/` | Une loi (loi organique, loi de finances, loi de ratification, loi modificative ...) |
| `ordonnances/<annÃ©e>/...` | Une ordonnance |
| `decrets/<annÃ©e>/...` | Un dÃ©cret |
| `arretes/<annÃ©e>/...` | Un arrÃªtÃ© (ministÃ©riel, interministÃ©riel ...) |
| `decisions/<annÃ©e>/...` | Une dÃ©cision publiÃ©e au Journal officiel |

L'annÃ©e est celle de la signature. Quand une annÃ©e compte plus de 990 actes d'un mÃªme type, elle est divisÃ©e par mois
(`decrets/<annÃ©e>/<mois>/...`). Aucun dossier ne compte plus de 1 000 entrÃ©es.

Chaque acte est un dossier : `preambule.md` (titre et visas), un fichier par article (`art-001.md` ; `art-012-bis.md`),
`signatures.md` (formule finale et signatures) et un `README.md` (Journal officiel, page, date d'entrÃ©e en vigueur).
Un acte sans articles est dans `texte.md`. Un code de plus de 990 articles range ses articles par tranches de 500
(`art-1000-1499/art-1205.md`).

## Dates

Chaque acte est un commit, datÃ© Ã  12 h 00 (LomÃ©, UTC) du jour de son entrÃ©e en vigueur, que rÃ©pÃ¨te le trailer
`In-force:`. `In-force-basis:` dit d'oÃ¹ vient ce jour :

- le texte lui-mÃªme, quand il fixe son entrÃ©e en vigueur (Â« entre en vigueur Ã  compter de sa signature / de sa
  publication / du 1er janvier ... Â») ;
- sinon, pour une loi ou une ordonnance, sa promulgation (date de signature) ;
- sinon, pour un dÃ©cret, un arrÃªtÃ© ou une dÃ©cision, sa publication au Journal officiel.

Un acte dont l'entrÃ©e en vigueur est diffÃ©rÃ©e (dÃ©lai, date fixÃ©e par un texte ultÃ©rieur) ou dont les dates se
contredisent n'est pas encore versÃ©. Avant 1970, que git ne sait pas dater, le commit est datÃ© du 1er janvier 1970 et le
vrai jour est dans le sujet et le trailer `In-force:`. Aucune date n'est le jour oÃ¹ nous avons tÃ©lÃ©chargÃ© le texte.

Les mesures individuelles (nominations, carriÃ¨res, distinctions) ne sont pas versÃ©es : ce ne sont pas des rÃ¨gles.

---

# Structure (English)

`constitution/` holds the Constitution of 6 May 2024; `constitution-<year>/` an earlier constitution; `codes/<code>/` a
code in force as its enacting law published it, `codes/<code>-<year>/` an earlier code it replaced; every other act is
filed by type and year of signature: `lois/`, `ordonnances/`, `decrets/`, `arretes/`, `decisions/`. One file per
article. Each commit is dated noon LomÃ© on the day the act took effect: the day the text sets, else promulgation for a
law or ordinance, else publication in the Journal officiel for a regulatory act. Acts with deferred or contradictory
dates are held; individual measures (appointments, careers, honours) are left out.
