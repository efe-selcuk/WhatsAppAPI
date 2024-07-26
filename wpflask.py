import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'efe'  # Sizin belirlediğiniz token
ACCESS_TOKEN = 'EAFzABgCNDBoBOZCHGnZAZBWW9PDtjVB6p0ZCSeNLteoXn5LvoBZCvMnNWCo7nM9fKHHcl4mZBLPe7o7yBgX2BlNcAis4h32yvWJjn3B0yjq7ZAa2x3Q3YZAbgPYNRzDJL6Ux5sxZBZAmuTpZCrOlF5ahONSJPGLPJIZBlDZBBA541EtgZAZC5pBU6dGegZCdqQtRoPqBv035ckOri7pA78mZA0gfoPZBgEOkmkTEZCmQABl1QQZD'  # WhatsApp Business API erişim tokenı

@app.route('/')
def home():
    return "Flask uygulaması çalışıyor!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        challenge = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')

        if mode == 'subscribe' and verify_token == VERIFY_TOKEN:
            return challenge
        else:
            return 'Invalid verify token', 403

    if request.method == 'POST':
        try:
            data = request.json
            print(f"Gelen veri: {data}")

            # Gelen mesajları işleyin
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    value = change.get('value', {})
                    
                    # Kontrol edelim ve her iki durumu da ele alalım
                    if 'messages' in value:
                        message = value['messages'][0]
                        phone_number_id = value['metadata']['phone_number_id']
                        from_number = message['from']
                        msg_body = message['text']['body']

                        # Gelen mesaja yanıt verin
                        reply_text = f"Merhaba! Mesajınızı aldım: {msg_body}"
                        send_message(phone_number_id, from_number, reply_text)

                    elif 'statuses' in value:
                        print(f"Durum güncellemesi: {value['statuses']}")

            return jsonify({"status": "success"}), 200

        except Exception as e:
            print(f"Hata: {e}")
            return 'Internal Server Error', 500

def send_message(phone_number_id, to, text):
    url = f"https://graph.facebook.com/v13.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": text
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Yanıt gönderildi: {response.status_code}, {response.text}")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
