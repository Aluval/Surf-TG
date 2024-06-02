from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "10811400"))
    API_HASH = getenv("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
    BOT_TOKEN = getenv("BOT_TOKEN", "6590434079:AAGSszefZEKGwAyy4K3UxCpMq0iF-T6yvVc")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://ALLINONE24BOT:ALLINONE24BOT@cluster0.6gxmegr.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "SUNRISES24")
    PASSWORD = getenv("PASSWORD", "Harsha24")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "SUNRISES467")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "SUNRISES467")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
