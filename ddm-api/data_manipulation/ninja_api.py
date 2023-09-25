import requests
from config import Config

def get_holidays(country,year):
    url = f'https://api.api-ninjas.com/v1/holidays?country={country}&year={year}'

    payload = {}
    headers = {
    'X-Api-Key': Config.NINJAXApiKey
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


