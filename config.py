from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "BQBrZZVbg2VKUAmJvPCYut5xFOjETssDBlOoyqgsv85jOzgSyBsrm0KmnKSMxZCji1HhqTFQhuY1aWv8cavfmNWksNKtU6x3ewdkXvmiAMXOd_zEW-4wOUqfWDSqIo2XzJSiD4T2GdP6phINEccwnX84ER53xPSYNBjRPVkDiNDJe1cT-DsnZaLrEBPqaZF_pFLTnznXSaJ_5wrzdZ3bKrpFVhxi_iL7lI4aaj98bMQeW1GL7L6vUYBv6WMy2W6EgiA8LVvSpaIsGqX9bTctFwelKUVd0gPJmdsTFacNgFMTmCWygopPij8T7i8Mp7drCFPsnjcy0FsraFD6LrjYgJd8AAAAAWpvsoYA")
BOT_TOKEN = getenv("BOT_TOKEN" ,"5208962076:AAFRivp9NqIABXvc0m8FI7PFxtaViYQeyeM")
API_ID = int(getenv("API_ID", "5642193"))
API_HASH = getenv("API_HASH","c28fc9ac88530587236175da89184d75")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://logesh:logesh@cluster0.z75dh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1872927069").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1872927069").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001857376981"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Tessa")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
