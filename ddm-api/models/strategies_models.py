
from flask_restx import  fields

# Modell for produktstrategi
productStrategyModel = {
    'ProduktID': fields.Integer(required=True, description='Unik identifikator for produktet'),
    'Viktighet': fields.String(required=True, description='Viktighet for produktet'),
    'Prioriteringsnivå': fields.String(required=True, description='Prioritetsnivå for produktet'),
    'Beskrivelse av viktigheten': fields.String(required=True, description='Beskrivelse av viktigheten'),
    'Beskrivelse av Prioriteringsnivå': fields.String(required=True, description='Beskrivelse av prioritetsnivået')
}

holidaysModel = {
    'id': fields.Integer(required=True, description='Unik identifikator for sesongen'),
    'navn': fields.String(required=True, description='Navnet på sesongen'),
    'kategori': fields.String(required=True, description='Kategorien for sesongen'),
    'hvordan_markedsforer_bransjen_seg': fields.String(required=True, description='Beskrivelse av hvordan bransjen markedsfører seg'),
    'hva_selger_de_mest_av': fields.String(required=True, description='Beskrivelse av hva bransjen selger mest av'),
    'fridag': fields.String(required=True, description='Angir om det er en fridag for bransjen (Ja/Nei)'),
    'start_markedsforingsdato': fields.String(required=True, description='Startdato for markedsføring av sesongen'),
    'slutt_markedsforingsdato': fields.String(required=True, description='Sluttdato for markedsføring av sesongen'),
    'samme_dato_hvert_ar': fields.String(required=True, description='Angir om datoene er de samme hvert år (Ja/Nei)'),
    'tilleggsstrategier': fields.String(required=True, description='Tilleggsstrategier brukt av bransjen')
}