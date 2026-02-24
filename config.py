import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "29816577"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "921b2c09a090b6848f35798dcc750d5a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6935290696:AAFEGmYDKpS7I79KAvKj0AoWgAXUUMA5YSU")

OWNER_ID = int(os.environ.get("OWNER_ID", "5142272541"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5142272541").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://laxman:laxman@cluster0.0e9zu0i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003796300718"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1003766768488")  # Optional here you'll get all logs
