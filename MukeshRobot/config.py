
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12227067 # integer value, dont use ""
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "6129232106:AAFnvrcgz5J9Ja-bW1H6Rtb4hE6oRF6aD6Q"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6204761408 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "+jLfuucjsi8kzMzE1"  # Your own group for support, do not add the @
    START_IMG = "https://te.legra.ph/file/2a15d2d3cf450154a35b9.jpg"
    EVENT_LOGS = ("-1001908711819")
    JOIN_LOGGER = ("-1001841879487")  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://ambot:ambot@ambot.onafiyb.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://citus:AbhiModszYT12@c-yone.2iti2yet5lss6l.postgres.cosmos.azure.com:5432/yone"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "PNNU99H3W9KDLKVM"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "9HK7J0H25AKQ"
    # Get your API key from https://timezonedb.com/api
    OPENAI_KEY = "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"
    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [736041718]  # User id of sudo users
    DEV_USERS = [6204761408]  # User id of dev users
    DEMONS = [6204761408]  # User id of support users
    TIGERS = [6204761408]  # User id of tiger users
    WOLVES = [6204761408]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
