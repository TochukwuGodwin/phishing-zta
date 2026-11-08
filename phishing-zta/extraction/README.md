# Extraction sheet legend

`selected_studies.csv` lists the 51 selected studies. Columns: ID, database, year, venue type, title, authors, venue, DOI,
attack type, defence evaluated, method.

Fields were assigned from the title, abstract and metadata exported by the databases. Sample size, main result and limitations
were not systematically extracted because the full texts were not read.

| Column | Values |
|---|---|
| Attack type | Email phishing (generic); Social engineering (general); Spear / lateral / BEC; Real-time proxy / MFA bypass; Smishing; QR-code and LLM-generated; Email phishing, LLM-assisted; Lateral phishing, LLM-generated |
| Defence evaluated | Awareness / training; Email authentication (SPF/DKIM/DMARC); MFA / FIDO2 / passkeys; Reporting / incident response; Warnings / support tools; None (attack or susceptibility analysis) |
| Method | User study, survey or interviews; Field experiment / simulation; Measurement study; Technical implementation / analysis; Review / SoK |
