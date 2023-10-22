class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24179799
    API_HASH = "e0449ebeed25c5f96293b6cbf94aae61"

    CASH_API_KEY = "MYCJZ83GDE4G9U3K"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "https://customer.elephantsql.com/instance"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002077210756)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "https://customer.elephantsql.com/instance"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "kingsbotsupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6864309682:AAF2Pi4SKJvCY4rZ7RA9mSl0v2sBEi0QLVA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "UCRHZCYN3MZA"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6018567899  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

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
