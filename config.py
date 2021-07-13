import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", " xxxxx")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-xxxxxxxx")
    API_ID = int(os.environ.get("API_ID", 4834535))
    API_HASH = os.environ.get("API_HASH", "xxxxxxxxx")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "-xxxxxxx")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "-xxxxxx")
