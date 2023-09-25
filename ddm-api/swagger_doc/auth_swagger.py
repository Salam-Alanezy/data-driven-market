ns_name = 'auth'
ns_description = 'API for brukerautentisering'

params = {
    'X-API-Key': 'API-nøkkel for autentisering (påkrevd)'
}

login_description = 'Logg inn en bruker'
login_response = {
    200: 'Bruker logget inn vellykket.',
    201: 'Bruker logget inn for første gang.',
    400: 'Ugyldige innloggingsopplysninger.',
    401: 'Ugyldig API-nøkkel.',
    403: 'Innlogging ikke tillatt for denne brukeren.',
    500: 'Uventet feil under innlogging.'
}

register_description = 'Registrer en ny bruker'
register_response = {
    201: 'Bruker registrert vellykket.',
    400: 'Ugyldige registreringsdata.',
    401: 'Ugyldig API-nøkkel.',
    409: 'Bruker med samme e-post eksisterer allerede.',
    500: 'Uventet feil under registrering.'
}

