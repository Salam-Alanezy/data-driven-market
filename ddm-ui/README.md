<div align="left">
<img src="https://ddm-doc-img.alanezconsulting.no/ddm-gui.png" width="300">
</div>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css">

## Introduksjon

Data-Driven-Market UI (ddm-ui) er brukergrensesnittet til CRM-systemet designet for Lilleborg Dagligvare AS. Dette grensesnittet er utviklet for å gi en intuitiv og brukervennlig opplevelse for butikkledere og ansatte, og for å gjøre interaksjonen med systemets kjernefunksjoner enkel og effektiv.

<img src="https://ddm-doc-img.alanezconsulting.no/ui-doc.gif" width="1000">

## Kjernefunksjoner i UI

1. **Handleliste**: Enkel opprettelse og administrasjon av handlelister med strekkodeinntasting og skanning.
2. **Varetelling**: Effektiv sporing og oppdatering av varebeholdningen.
3. **Bransjekalender**: Tilgang til en tilpasset kalender med viktige hendelser og markedsføringsråd.
4. **Produktanalyse**: Visualisering av salgstrender og produktanalyse.
5. **Utforsking av nye produkter og prissammenligning**: Gjennomgang og sammenligning av produkter og priser fra konkurrerende butikker.

## Teknologi og Rammer

- **Bootstrap**: For responsivt og moderne UI design.
- **Jinja2**: Templating engine brukt i kombinasjon med Flask for dynamisk innholdsrendering.
- **JavaScript**: For interaktive elementer og asynkron datahåndtering.
- **CSS**: For tilpasset stillegging og branding.

## Installasjon og Oppsett

### Forutsetninger

- Naviger til prosjektets rotkatalog.
- Sørg for at du har installert alle avhengigheter som beskrevet i prosjektets hoved-README.

### Kjør UI Lokalt

1. **Start Flask-serveren**: Se instruksjoner i hoved-README for `ddm-api`.
2. **Åpne UI**: Naviger til `localhost` med porten spesifisert i Flask-appens oppsett (standard: 5000).

## Navigasjon og Bruk

- **Hjemmeside**: Oversikt over systemets hovedfunksjoner.
- **Handleliste**: Direkte tilgang fra hovedmenyen.
- **Varetelling**: Finn denne funksjonen under lageradministrasjon.
- **Bransjekalender**: Tilgjengelig fra navigasjonsfeltet.
- **Produktanalyse**: Få tilgang til analyser og rapporter via analyser-fanen.

## Sikkerhet og Tilgang

- Dette grensesnittet krever gyldige brukerlegitimasjoner.
- Rettighetsstyring er håndtert av `ddm-api` for å sikre at sensitive data forblir beskyttet.
