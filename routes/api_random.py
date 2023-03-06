from random import randint
from routes.api_info import get_word_info
import requests


app_id = "20643a03"
app_key = "06034ed8cade7a32f636a3c9bf328fb5"
language_code = "en-us"
endpoint = "entries"

def get_random_word():
    # Send a GET request to the entries endpoint with a random word as the word parameter
    url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}"
    headers = {"app_id": app_id, "app_key": app_key}
    resp = requests.get(url, headers=headers)

    # If the response was successful, return the word and its definition
    if resp.status_code == 200:
        result = resp.json()
        words = [entry['word'] for entry in result['results']]
        # Select random word
        random_index = randint(0, len(words) - 1)
        random_word = words[random_index]
        # Get the information for the random word
        word_info, status_code = get_word_info(random_word)
        return word_info, status_code
    else:
        return {'error': 'Error fetching words', 'status_code': resp.status_code}, resp.status_code
