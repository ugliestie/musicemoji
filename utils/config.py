import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
USER_ID = int(os.getenv("USER_ID"))

LAST_FM_USERNAME = os.getenv("LAST_FM_USERNAME")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL"))
NOW_PLAYING = bool(os.getenv("NOW_PLAYING"))
CUSTOM_EMOJI = os.getenv("CUSTOM_EMOJI")