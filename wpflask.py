from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'efe'  # API sağlayıcınızın beklediği verify token

@app.route('/')
def home():
    return "Flask uygulaması çalışıyor!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # API sağlayıcının doğrulama isteğine yanıt ver
        mode = request.args.get('hub.mode')
        challenge = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')

        if mode == 'subscribe' and verify_token == VERIFY_TOKEN:
            return challenge
        else:
            return 'Invalid verify token', 403

    if request.method == 'POST':
        data = request.json
        print(f"Gelen veri: {data}")  # Gelen veriyi konsola yazdır

        # Basit bir yanıt
        response = {
            "text": "Webhook verisi alındı!"
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
