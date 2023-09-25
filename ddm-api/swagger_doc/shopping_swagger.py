ns_name='shopping'
ns_description='API-operasjoner relatert til handel liste. Dette API-et vil hovedsaklig bli brukt under bestillinger.'

params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)'
        }

params_post = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'payload': 'Eksempel på dataformat (påkrevd)'
        }

params_update = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'product_id':'Unik product-ID (påkrevd)',
        'payload': 'Eksempel på dataformat (påkrevd)'
        }

params_delete = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'product_id':'Unik product-ID (påkrevd)',
        }

post_description='Legg til et nytt produkt til handlingslisten.'
post_response ={201: 'Produkt lagt til vellykket.',
                400: 'Valideringsfeil.',
                401: 'Ugyldig API-nøkkel',
                500: 'Uventet feil under innsetting av produkt.'}



get_description='Få alle produkter i lager for en bruker.'
get_response = {
    200: 'Data hentet.',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av data.'
}


update_description='Oppdater/endre et produkt i handlingslisten basert på produktet id.'
update_response = {
    200: 'Produkt oppdatert vellykket.',
    400: 'Valideringsfeil.',
    401: 'Ugyldig API-nøkkel',
    404: 'Produktet ble ikke funnet.',
    500: 'Uventet feil under oppdatering av produkt.'
}

delete_description='Slett et produkt fra handlelisten.'
delete_response = {
    200: 'Produkt ble slettet.',
    400: 'Valideringsfeil.',
    401: 'Ugyldig API-nøkkel',
    404: 'Produktet ble ikke funnet.',
    500: 'Uventet feil under sletting av produkt.'
    
}