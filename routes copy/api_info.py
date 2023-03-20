from flask import jsonify, request
import requests
import random

app_id = "20643a03"
app_key = "06034ed8cade7a32f636a3c9bf328fb5"
language_code = "en-us"
endpoint = "entries"


def get_word_info(word):
    url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language_code}/{word.lower()}"
    headers = {"app_id": app_id, "app_key": app_key}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            lexical_entries = result['results'][0]['lexicalEntries']
            pos = []
            definitions = []
            synonyms = []
            for entry in lexical_entries:
                pos.append(entry['lexicalCategory']['text'])
                for sense in entry['entries'][0]['senses']:
                    if 'definitions' in sense:
                        definitions.append(sense['definitions'][0])
                    if 'synonyms' in sense:
                        synonyms.append(sense['synonyms'][0]['text'])
            if not pos:
                return {'error': 'Word not found'}, 404
            resp = {
                'word': word.title(),
                'part_of_speech': ', '.join(pos).title(),
                'definition': definitions[0].capitalize(),
                'definitions': definitions[1:],
                'synonyms': synonyms
            }
            return resp, 200
        else:
            return {'error': 'Error fetching word', 'status_code': response.status_code}, response.status_code

    except (requests.exceptions.RequestException, IndexError) as e:
        status_code = getattr(e.response, 'status_code', 500)
        return {'error': 'Response not found'}, status_code
    

def get_random_word():
    url = f"https://od-api.oxforddictionaries.com/api/v2/wordlist/en/regions=us"
    headers = {"app_id": app_id, "app_key": app_key}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            words = [word['word'] for word in result['results']]
            word = random.choice(words)
            return word, 200
        else:
            return {'error': 'Error fetching word', 'statuc_code':response.status_code}, response.status_code
        
    except (requests.exceptions.RequestException, IndexError) as e:
        status_code = getattr(e.response, 'status_code', 500)
        return {'error': 'Response not found'}, status_code
    
    return None