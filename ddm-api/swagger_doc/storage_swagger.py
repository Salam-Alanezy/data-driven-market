
ns_name='storage'
ns_description='API-operasjoner relatert til lagerlagring. Dette API-et vil hovedsaklig bli brukt under varetelling.'

params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
     
        }

params_product_id = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'product_id':'Unik product-ID (påkrevd)'
        }

post_description='Legg til et nytt produkt i lageret.'
post_response = {
    201: 'Produkt er lagt',
    400: 'Ugyldige data',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under innsetting av produkt.'
}

get_description='Henter alle produkter som er på lager'
get_response = {
    200: 'Lager hentet vellykket.',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av lager.'
}

update_description='Oppdater/endre produkt fra lageret basert på produktet id.'
update_response = {
    200: 'Produkt oppdatert vellykket.',
    400: 'Valideringsfeil.',
    401: 'Ugyldig API-nøkkel',
    404: 'Produktet ble ikke funnet.',
    500: 'Uventet feil under oppdatering av produkt.'
}

delete_description='Slett et produkt fra lageret.'
delete_response = {
    200: 'Produkt ble slettet.',
    400: 'Valideringsfeil.',
    401: 'Ugyldig API-nøkkel',
    404: 'Produktet ble ikke funnet.',
    500: 'Uventet feil under sletting av produkt.'
    
}