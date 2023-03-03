from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from routes.api_contact import send_email
from routes.api_info import get_word_info


server = Flask(__name__)
CORS(server, supports_credentials=True)


app_id = "HIDDEN"
app_key = "HIDDEN"
language_code = "en-us"
endpoint = "entries"


@server.route("/api/info/")
def api_info():
    word = request.args.get('word')
    if not word:
        return jsonify({'error': 'Missing word parameter'}), 400

    result, status_code = get_word_info(word)

    resp = jsonify(result)
    resp.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    return resp, status_code


@server.route('/api/contact', methods=['POST', 'OPTIONS'])
@cross_origin()
def api_contact():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message'].encode('utf-8').decode('utf-8')
        send_email(subject, email, f"Name: {name}\nMessage: {message}")
        return jsonify({'message': 'Email send successfully'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error sending email'}), 500

if __name__ == '__main__':
    server.run(debug=True)