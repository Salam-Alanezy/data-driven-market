ns_name='events'
ns_description='API-operasjoner relatert til events. Dette API-et vil hovedsaklig bli brukt for å lagre og hente eventdata.'

params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
     
        }

params_post = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'payload': 'Eksempel på dataformat (påkrevd)'
        }

params_product_id = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'product_id':'Unik product-ID (påkrevd)'
        }

post_description='Lagre et nytt event i databasen.'
post_response = {
    201:'Event lagret vellykket.',
    400:'Valideringsfeil.',
    401: 'Ugyldig API-nøkkel',
    500:'Uventet feil under innsetting av event.'
}


get_description='Henter alle eventer'
get_response = {
    200: 'Alle eventer har blitt hentet',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av eventer.'
}



params_ninja = {
    'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
    'uid': 'Unik bruker-ID (påkrevd)',
    'country': {'description': 'Legg til land (påkrevd)', 'default': 'NO'},
    'year': {'description': 'Legg til år (påkrevd)', 'default': '2023'}   
}

get_ninja_response = {
    200: 'Alle eventer har blitt hentet',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av eventer.'
}