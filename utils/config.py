import os
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file, override=True)

TOKEN = os.environ.get("TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
USER_ID = int(os.environ.get("USER_ID"))

LAST_FM_USERNAME = os.environ.get("LAST_FM_USERNAME")
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

UPDATE_INTERVAL = int(os.environ.get("UPDATE_INTERVAL"))
NOW_PLAYING = bool(os.environ.get("NOW_PLAYING"))
CUSTOM_EMOJI = os.environ.get("CUSTOM_EMOJI")

DB_URL = os.environ.get("DB_URL")