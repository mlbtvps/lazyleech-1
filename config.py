from lazyleech import BOT_USERNAME
import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5859165740:AAFDiBHAuP1fxeheB6OxDGfP5Rjzyylp0u0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Goku_SanBot")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-1001622357602")
    API_ID = int(os.environ.get("API_ID", 17894641))
    API_HASH = os.environ.get("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "5468192421 5559979635 5504969603 1349301822 5623031120")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "5468192421 5559979635 5504969603 1349301822 5623031120")
