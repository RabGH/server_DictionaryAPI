from flask import jsonify, request
from flask import Flask
from routes.api_info import get_word_info
import requests
import random

server = Flask(__name__)

app_id = "20643a03"
app_key = "06034ed8cade7a32f636a3c9bf328fb5"
language_code = "en-us"
endpoint = "wordlist"



def get_random_word():

    url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/"
    headers = {"app_id": app_id, "app_key": app_key}

    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            words = resp.json()['results']
            word = random.choice(words)['word']
            print(word)
            return word
        else:
            return {'error': 'Error fetching word', 'status_code':resp.status_code}, resp.status_code
        
    except (requests.exceptions.RequestException, IndexError) as e:
        status_code = getattr(e.response, 'status_code', 500)
        return {'error': 'Response not found'}, status_code