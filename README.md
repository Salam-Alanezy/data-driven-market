# Data-Driven-Market

## Introduksjon
Data-Driven-Market er et CRM-system designet spesifikt for Lilleborg Dagligvare AS, en voksende dagligvarebutikk. Med tanke på utfordringene bedriften møter i produktadministrasjonen, sikter dette CRM-systemet mot å effektivisere og strømlinjeforme butikkens daglige drift.

## Kjernefunksjoner:
- **Opprette handleliste:** Raskt legge til varer via strekkodeinntasting eller skanning.
- **Hold øye med utløpsdatoer:** Overvåk produktene som nærmer seg utløpsdato.
- **Varetelling:** Holde orden på varebeholdningen.
- **Bransjekalender:** Inneholder viktige datoer og markedsføringstips tilpasset dagligvarebransjen.
- **Produktanalyse:** Innsikt i hva som selger og hva som ikke gjør det.
- **Utforske nye produkter:** Identifiser nye produkter som selges av konkurrenter via eksterne APIer.
- **Prissammenligning:** Sammenlign dine priser med konkurrerende butikker.

### Opprette handleliste
Gjennom enkel strekkodeinntasting eller skanning kan butikkledelsen raskt legge til ønskede varer i handlelisten. Når listen er fullført, kan brukeren eksportere listen som en Excel-fil, enten ved å sende den via e-post eller ved å laste den ned direkte til enheten. Produkter forblir aktive i CRM til de er merket av på handlelisten. 

**Input for handlelisten inkluderer:**
- Strekkode
- Produktnavn
- Leverandør
- Antall
- Produktbilde
- Utløpsdato (ved oppdatering av listen)

### Varetelling
Fungerer lignende som handlelisten; brukere kan manuelt legge inn eller skanne produktets strekkode.

**Input for varetelling inkluderer:**
- Strekkode
- Produktnavn
- Leverandør
- Antall
- Utløpsdato
- Produktbilde

### Lager- og utløpsdatovarsler
Ved regelmessig varetelling og innlogging av nyinnkjøpte varer kan brukeren motta varsler angående lagerstatus og utløpsdatoer. Dette sikrer at produktene alltid er tilgjengelige og bidrar til å minimere svinn.

### Bransjekalender
Kalenderen gir oversikt over viktige hendelser i dagligvarebransjen, som helligdager og spesielle feiringer, og tilbyr markedsføringsråd tilpasset disse hendelsene.

### Produktanalyse
Analyser salgstrender og identifiser hvilke produkter som selger best, hvilke som ligger for lenge på lager, og hvilke som bør bestilles i større kvanta.

### Utforske nye produkter og prissammenligning
Ved hjelp av eksterne APIer kan brukeren utforske produkter solgt av konkurrerende butikker, samt sammenligne priser for å sikre konkurransedyktighet.

## Teknisk Gjennomgang

### Struktur
Applikasjonen består av to hovedmoduler:
- **ddm-ui:** Brukergrensesnittet for CRM.
- **ddm-api:** API-et som støtter programmet.

### Teknologier
For utviklingsprosessen ble følgende teknologier valgt på grunn av pris og kompetanse:

- Python
- Flask
- Firebase
- HTML/CSS
- Bootstrap
