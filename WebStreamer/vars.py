# @SMD_Owner

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID","19553188"))
    API_HASH = str(environ.get("API_HASH","52c7a1c621bc52258f55961d65028bb0"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "6925301978:AAHkWXsRMQzCwoqxakCpLrc0YbMGKEPxG00"))
    SHORTNER_API = str(environ.get("SHORTNER_API", "944ca63bcf41cc4159c9f40ba941012d9bba89d5")) 
    SHORTENR_URL = str(environ.get("SHORTENR_URL", "upshrink.com")) 
    AUTH_CHANNEL = str(environ.get("AUTH_CHANNEL", "TamilMov_LinkZz")) 
    CUSTOM_FILE_CAPTION = str(environ.get("CUSTOM_FILE_CAPTION","** {file_name} \n\n ⚡️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 :  \n {short_link} \n\n 💢Join : @{main_chat} **")) 
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1002013080843"))  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1600"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", BIND_ADDRESS))
        if not ON_HEROKU or environ.get("FQDN")
        else APP_NAME + "-raam-30d37bff9880.herokuapp.com"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = f"{FQDN}/"

    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "aredirect"))
    OWNER_ID = int(environ.get('OWNER_ID', '885675538'))

    BANNED_CHANNELS = list(set(int(x) for x in str(environ.get("BANNED_CHANNELS", "-1001296894100")).split()))
