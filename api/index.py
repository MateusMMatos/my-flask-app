from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZAPIER_WEBHOOK_URL = 'https://hooks.zapier.com/hooks/catch/YOUR_WEBHOOK_URL_HERE/'

@app.route('/nubank-webhook', methods=['POST'])
def nubank_webhook():
    data = request.json
    response = requests.post(ZAPIER_WEBHOOK_URL, json=data)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
