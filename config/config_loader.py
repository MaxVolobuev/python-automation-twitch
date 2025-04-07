import os
from dotenv import load_dotenv

load_dotenv()  # Load ENV variable from .env

ENV = os.getenv("ENV", "dev")  # By default dev

CONFIG = {
    "dev": {
        "BASE_URL": "https://dev.twitch.tv/directory",
        "MOBILE_DEVICE": "Pixel 2"
    },
    "prod": {
        "BASE_URL": "https://www.twitch.tv/directory",
        "MOBILE_DEVICE": "Pixel 2"
    },
    "stg": {
        "BASE_URL": "https://stg.twitch.tv/directory",
        "MOBILE_DEVICE": "iPhone X"
    }
}

# Take correct config based on ENV
# If ENV is not in CONFIG, use dev config
ENV_CONFIG = CONFIG.get(ENV, CONFIG["dev"])
