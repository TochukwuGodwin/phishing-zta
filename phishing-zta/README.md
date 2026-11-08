# Why Phishing Still Works: Analysing Modern Attacks and Evaluating Defences

Project for **Network and Information Systems Security** (Iscte – Instituto Universitário de Lisboa).
This repository holds the material behind the Part 1 (theoretical) report: a systematic literature review
on phishing and its defences, with a Zero Trust perspective on phishing that spreads from a compromised device.

**Research question:** why do phishing attacks keep working despite technical protections and user awareness,
and which defences are most effective?

## Repository structure

| Path | Content |
|---|---|
| `protocol/protocol.md` | Research questions, PICOC, search strings, databases, dates, inclusion/exclusion criteria, screening stages, limitations |
| `screening/screening_log.csv` | All 529 retrieved records (IEEE Xplore and ACM Digital Library) with stage decisions and exclusion criterion |
| `extraction/selected_studies.csv` | The 51 selected studies with attack type, defence evaluated and method |
| `extraction/README.md` | Legend for the codes used in the extraction sheet |
| `data/samples/` | Defanged phishing samples for Part 2 (template and a constructed example only, no real payloads) |
| `analysis/` | Python scripts: `reproduce_counts.py`, `levenshtein.py`, `risk_model.py`, `indicators.py` |
| `figures/` | Figures used in the report (selection flow, statistics, Zero Trust flow) |
| `report/` | Final report (Word) |

## Reproducing the numbers in the report

```bash
cd analysis
python reproduce_counts.py   # Table 4, Figure 1 and Figure 2: record counts and statistics of the 51 studies
python levenshtein.py        # worked example in Table 10 (d_L = 1, s = 0.89)
python risk_model.py         # illustrative layered model in Section 5.3 (about 5 credentials per 1,000; 0.05 with MFA)
python indicators.py ../data/samples/samples_example.csv   # indicator coding on the constructed example
```

Only the Python standard library is needed (Python 3.9+).

## Method in one paragraph

Primary search on 1 November 2026: 84 records in IEEE Xplore and 445 in the ACM Digital Library (529 in total).
One duplicate removed; stage 1 (title, keywords, abstract) kept 78; stage 2 selected 51 studies.
The secondary string (adds review terms) returned 3 IEEE and 90 ACM records, all already in the primary set,
and was used to find existing reviews and refine the research questions.
**Limitation:** stage 2 was based on titles, abstracts and metadata only; the full texts were not read, so the
three-pass reading (Keshav, 2007) was not applied. Screening was done by a single screener.

## Ethics and safe handling

- No real phishing payloads, credentials or personal data are stored here.
- URLs are stored defanged (`hxxps://login.example[.]test`); never open live phishing pages from a personal device.
- Raw database exports (BibTeX/CSV from ACM and IEEE) are not included because they contain publisher abstracts.
  To rebuild them, re-run the strings in `protocol/protocol.md` in each database (results will differ over time).

## Licence

Code and documentation: MIT licence (see `LICENSE`). Third-party papers listed in the CSV files remain the
property of their authors and publishers; only bibliographic metadata (title, authors, venue, DOI) is listed.

## Authors

Author 1 - Tochukwu Godwin Ugwuozor | 136439 
Author 2 - João Copeto | 110867 
Author 3 - Valerim da Silva | 142563
