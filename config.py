from lazyleech import BOT_USERNAME
import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://inkd:rollnf@cluster0.672ix.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1934325452:AAEZBpctpSoqWoLBdMeonolBvPXjTpx79FU")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Asuna_LeechBot")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-1001580241495")
    API_ID = int(os.environ.get("API_ID", 3793864))
    API_HASH = os.environ.get("API_HASH", "3c8713a1cf5904f60960ecff27b1faa8")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "-1001580241495")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "-1001579439262")
