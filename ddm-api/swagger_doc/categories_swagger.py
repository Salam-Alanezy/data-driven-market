


ns_name = 'categories'
ns_description = 'Gir tilgang til data for organisering av dagligvareprodukter ved å presentere hierarkisk struktur, underkategorier og produktstrategi for bedre navigasjon og forståelse.'

params_post = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
        'payload': 'Eksempel på dataformat (påkrevd)'
        }
params = {
        'X-API-Key': 'API-nøkkel for autentisering (påkrevd)',
        'uid': 'Unik bruker-ID (påkrevd)',
     
        }


post_description='Legger til hovedkategorier dataen'
post_response = {
        201: 'Hovedkategorien ble lagt til med suksess',
        400: 'Ugyldige data sendt for viktighet av hovedkategori',
        401: 'Ugyldig API-nøkkel',
        500: 'Uventet feil under tillegging av viktighet for hovedkategori'
        }

get_description='Henter hovedkategorier for en spesifikk bruker'
get_response = {
        200: 'Hovedkategorier ble hentet med suksess',
        401: 'Ugyldig API-nøkkel',
        500: 'Uventet feil under henting av hovedkategorier'
        }

get_sub_description = 'Henter alle underkategorier'
get_sub_response = {
        200: 'Underkategorier ble hentet med suksess',
        401: 'Ugyldig API-nøkkel',
        500: 'Uventet feil under henting av underkategorier'
        }

get_all_description='Henter alle kategorier'
get_all_response = {
        200: 'Kategorier ble hentet med suksess',
        401: 'Ugyldig API-nøkkel',
        500: 'Uventet feil under henting av kategorier'
        }