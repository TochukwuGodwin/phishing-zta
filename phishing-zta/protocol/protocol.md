# Review protocol

Follows the course protocol for systematic literature reviews (after Kitchenham & Charters, 2007).

## Research questions
- **RQ1 (general):** Why do phishing attacks keep succeeding despite technical protections and user awareness, and which defences are most effective?
- **RQ2 (focused):** Which types and channels of phishing are used today, including QR codes, real-time proxies and lateral phishing from compromised devices?
- **RQ3 (focused):** Which human, organisational and technical factors explain attacker success?
- **RQ4 (focused):** How effective are awareness training, email authentication, MFA, warnings and reporting, and when does each fail?
- **RQ5 (focused):** What do incidents show about where attacks could have been stopped, and how could Zero Trust limit spread from a compromised device?
- **RQS1–4 (statistical):** How many selected studies per year, attack type, defence evaluated and method?

## PICOC
Population: users and organisations targeted by phishing. Intervention: training, email authentication, MFA of different strengths, warnings, reporting.
Comparison: no defence or a weaker defence. Outcome: click and credential-submission rates, compromise, spoofed-mail delivery, reporting.
Context: enterprise and consumer email, web and mobile channels.

## Databases and dates
IEEE Xplore and ACM Digital Library only. Search date: 4 November 2026. Records returned span 2008–2026.

## Primary search string
```
("phishing" OR "spear phishing" OR "social engineering")
AND
("security awareness" OR "MFA" OR "DMARC" OR "WebAuthn")
AND
("effectiveness" OR "evaluation" OR "user study")
```
Results: IEEE Xplore 84, ACM Digital Library 445 (529 in total).

## Secondary string
Primary string `AND ("systematic literature" OR "systematic review" OR "literature review")`.
Results: IEEE Xplore 3, ACM Digital Library 90 (all 93 also in the primary set).

## Criteria
Inclusion: IC1 peer-reviewed journal, conference or workshop paper; IC2 English; IC3 contains terms from the search string; IC4 published 2008–2026.
Exclusion: EC1 not aligned with the RQs (for example machine-learning detection algorithms); EC2 does not address phishing or social engineering by email, web, SMS, voice or QR code; EC3 neither evaluates a defence nor analyses an attack mechanism; EC4 no empirical or analytical contribution (proposals, frameworks, game designs); EC5 duplicate.

## Process and counts
1. Retrieve and export records (529). 2. Remove duplicates, EC5 (1 removed, 528 remain).
3. Stage 1, title/keywords/abstract: records without a phishing or social-engineering term were excluded (EC2, 351); the other 177 were read and 78 kept.
4. Stage 2, stricter second pass on titles, abstracts and metadata: 51 selected, 27 excluded.
5. Data extraction for the 51 selected studies (`extraction/selected_studies.csv`).

## Limitations
Two databases only (venues such as USENIX Security are not indexed by either); the string requires the terms MFA, DMARC, WebAuthn or security awareness;
stage 2 did not use full texts (three-pass reading not applied); single screener; qualitative defence ratings in the report are the authors' synthesis.
