from flask import Flask, jsonify, request
from flask_cors import cross_origin
from routes.api_contact import send_email
from routes.api_info import get_word_info

server = Flask(__name__)


@server.route("/api/info/")
@cross_origin()
def api_info():
    word = request.args.get('word')
    if not word:
        return jsonify({'error': 'Missing word parameter'}), 400

    result, status_code = get_word_info(word)

    resp = jsonify(result)
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
    server.run(host='0.0.0.0', port=5000, debug=True)
