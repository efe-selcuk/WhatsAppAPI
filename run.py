import requests
import json

# WhatsApp Business API için gerekli bilgiler
phone_number_id = "420112591165945"  # Telefon numarası ID'si
access_token = "EAFzABgCNDBoBO38Mt33NGbExCmWSUVLD0VGa0S1qC2kGY2mqRZCohu0Ln2dGlH91cv9Xxq2ZBJlcnFwZB3bJTh3OKIDVmZBjpYZCSIJoB9qAViG57kk9uBJunGw8yjBFUQ71tuy8AzXfuNmqnsao2URnff9JriyLoZB6hEdBwfcffOkZBkjgpdZAhrta9nbGj23qO2NKVLzH9WNpyMK1hQuqWu1lEotVQe8B4ApT"  # Erişim token'ı

# Mesaj gönderme URL'si
url = f"https://graph.facebook.com/v20.0/{phone_number_id}/messages"

# HTTP istek başlıkları
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Mesajın içeriği
payload = {
    "messaging_product": "whatsapp",
    "to": "905306658348",  # Alıcının telefon numarası
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

# Mesaj gönderme isteği
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Yanıtı yazdır
print(response.status_code)
print(response.json())
