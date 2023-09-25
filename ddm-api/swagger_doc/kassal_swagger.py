ns_name = "kassal"
ns_description="Dette API-et henter produkt informasjon fra ekstern API, Kassal-API. Dette API-et brukes for produkt-skanning og gir til å finne nye produkter."

get_params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'ean': 'Produktet strekkode (påkrevd)'
        }

search_params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'name': 'Produktetnavn (påkrevd)'
        }

all_params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'name': 'Produktetnavn (påkrevd)'
        }


get_description='Henter produkt fra Kassal-API basert på ean.'
get_response = {
    200: 'Data hentet.',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av data.'
}

all_description='Henter produkt fra Kassal-API basert på ean.'
all_response = {
    200: 'Data hentet.',
    401: 'Ugyldig API-nøkkel',
    500: 'Uventet feil under henting av data.'
}
