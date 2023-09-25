ns_name='store'
ns_description='Denne delen av API-et skal brukes til skanning av produkter som ligger lageret i kassen.'

params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)'
        }

params_post = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'payload': 'Eksempel på dataformat (påkrevd)'
        }

post_description='Legg til nytt produkt'
post_response = {
    201: 'Produkt er lagt',
    400: 'Ugyldige data',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under innsetting av data'
}

get_description='Hent alle produktene'
get_response = {
    200: 'Data hentet.',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av data.'
}


get_by_id_description='Hent produkt basert på strekkode'