from flask import Flask
from random import randint
from routes.api_info import get_word_info
import requests


app_id = "20643a03"
app_key = "06034ed8cade7a32f636a3c9bf328fb5"
language_code = "en-us"
endpoint = "entries"

server = Flask(__name__)

def get_random_word():
    url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}"
    headers = {"app_id": app_id, "app_key": app_key}
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        result = resp.json()
        words = [entry['word'] for entry in result['results']]
        random_index = randint(0, len(words) - 1)
        random_word = words[random_index]
        word_info, status_code = get_word_info(random_word)
        return word_info, status_code
    else:
        return {'error': 'Error fetching words', 'status_code': resp.status_code}, resp.status_code
