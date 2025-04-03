import os

class Config(object):
    BOT_TOKEN = os.environ.get("7628579933:AAHNZ0hn5JG17JHPg3bWtsx_OCAtirKvJB8")  # Ensure correct key name
    API_ID = int(os.environ.get("22581733"))  # Added key name and default value
    API_HASH = os.environ.get("1db7bdcf908100cc641c6a5276765c3d")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7001787251").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
