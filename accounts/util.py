import random
from hashlib import sha256
import requests
from django.conf import settings

def generate_otp():
    return str(random.randint(100000, 999999))

def hash_otp(otp):
    return sha256(otp.encode()).hexdigest()

def send_telegram_message(chat_id, message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")
        return None
