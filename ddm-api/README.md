<div align="left">
<img src="https://ddm-doc-img.alanezconsulting.no/ddm-api.png" width="300">
</div>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css">

## Introduksjon

API-et er en bro mellom brukersnittet og databaser og andre datakilder. Det spiller en avgjørende rolle i å hente, lagre, oppdatere og slette data fra forskjellige kilder for å støtte funksjonaliteten til Data-Driven-Market-prosjektet. API-et er utviklet for å håndtere flere databaser og datakilder, inkludert:

- Firebase Firestore: For strukturert lagring av data.
- Firebase Storage: For lagring av filer og ressurser.
- Self-hosted FTP-server: For filoverføringer og håndtering av store mengder data.
- Ninja API: For å hente eksterne data som kommende hendelser basert på land og år.
- Kassel API: For integrasjon med tredjepartsdata og tjenester.

API-et gir en enhetlig og strukturert tilnærming til å kommunisere med disse datakildene, og gir et pålitelig grunnlag for å støtte Data-Driven-Market-applikasjonen.



## Teknologi

API-et er utviklet ved hjelp av følgende teknologier:

- <i class="fab fa-python" style="color:blue;"></i> Python: Hovedspråket for utvikling av API-logikk.
- <i class="fas fa-database" style="color:gray;"></i> Firebase: For databaselagring og autentisering.
- <i class="fas fa-coffee" style="color:yellow;"></i> Flask: Et Python-web-rammeverk for å opprette RESTful API-er.
- <i class="fas fa-pencil-alt" style="color:darkblue;"></i> Flask RestX: Et Flask-utvidelsesbibliotek for API-dokumentasjon og validering.
- <i class="fab fa-docker" style="color:lightblue;"></i> Docker: For å containerisere API-et og enkel distribusjon.
- <i class="fas fa-book" style="color:green;"></i> Swagger: For dokumentasjon av API-endepunkter.


Denne teknologistakken er valgt for å sikre pålitelighet, skalerbarhet og enkel vedlikehold av API-et.


## Prosjektstruktur
<div align="center">
<img src="https://ddm-doc-img.alanezconsulting.no/project-structure.png" width="800">
</div>


## API-et sikkerhet

API-et benytter følgende sikkerhetsmekanismer:

- api_key: Autentiserer brukere og tilganger til API-endepunkter.
- uid: Identifiserer brukere for å gi tilgang til relevante data og tjenester.

## Endepunker Beskrivelse
<div align="center">
<img src="https://ddm-doc-img.alanezconsulting.no/end-point-table.png" width="800">
</div>


## Videre utvikling
Programmet er fortsatt under utvikling og det er flere endepunker som vil laget og endret etter testing og behov.


## Starte programmet
For å starte programmet må du ha Python versjon 10 eller høyere. 
Følg stegene under for å kjøre programmet. 

### config.py
config.py er konfrigrasjon filen for programmet. Alle nødvendige miljø-variabler/.env blir satt fra denne filen.

### Sikkerhet
For å kunne kjøre API kallene må api_key og uid eksistere i config.py
- api_key: Autentiserer brukere og tilganger til API-endepunkter.
- uid: Identifiserer brukere for å gi tilgang til relevante data og tjenester.

### .env
Disse variablene under er nødvendige får å kjøre programmet:
```
# PORT FOR RUNNING THE PROGRAM
PORT=

# JSON-FILES FROM FTP 
JSON_BASE_PATH=

# FIREBASE CONFIG
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=

# X-API-KEY
XAPIKEY=

# External APIs
KASSAL_API=
NINJAXApiKey=
SSB_BASE_URL=
```


### Prosjekt miljø
Opprett prosjekt-miljø:
- Åpne terminalen/cmd
- Naviger til prosjektet
Skriv denne kommando i 'root' prosjektet: 
```
python -m venv venv
```

For å aktivere prosjekt-miljø:
```
cd venv/Scripts
activate
```

Der etter naviger tilbake til 'root'

### Installer biblioteker 
Disse er de bibliotekene som blir brukt i prosjektet:
- Flask==2.3.2
- Flask-Cors==3.0.10
- Flask-RESTX==1.1.0
- python-dotenv==1.0.0
- bcrypt==4.0.1
- requests==2.31.0
- gunicorn==20.1.0
- firebase-admin==6.2.0

For å installere de nødvendige bibliotekene for prosjektet:
```
pip install -r requirements.txt
```

### Kjør programmet
```
python app.py
```
