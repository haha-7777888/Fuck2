
#
# Copyright (C) 2021-2022 by TheAloneteam@Github
# This file is part of TheAloneMusic.
# Released under the GNU General Public License v3.0.
#

import os
import re

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv("/root/ZeroTwo/.env", override=True)


# --------------------------------------------------
# ENVIRONMENT HELPERS
# --------------------------------------------------

def get_env(name, default=None):
    """Return the default when an environment variable is missing or empty."""
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return value.strip()


def get_int(name, default):
    """Safely parse integer environment variables."""
    value = get_env(name, str(default))
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(
            f"Invalid {name}={value!r}. Please provide a valid integer."
        ) from None


def get_bool(name, default=False):
    """Parse boolean environment variables correctly."""
    value = get_env(name, str(default)).lower()

    if value in {"1", "true", "yes", "on"}:
        return True

    if value in {"0", "false", "no", "off"}:
        return False

    raise ValueError(
        f"Invalid {name}={value!r}. Use true/false, yes/no, or 1/0."
    )


# --------------------------------------------------
# TELEGRAM API CONFIGURATION
# --------------------------------------------------

# Get these values from https://my.telegram.org/apps

API_ID = get_int("API_ID", 26249286)
API_HASH = get_env("API_HASH")
BOT_TOKEN = get_env("BOT_TOKEN")
MONGO_DB_URI = get_env("MONGO_DB_URI")


# --------------------------------------------------
# BOT SETTINGS
# --------------------------------------------------

DURATION_LIMIT_MIN = get_int("DURATION_LIMIT", 600)

# Set to true to enable automatic advertisements.
ADS_MODE = get_env("ADS_MODE")

# Group ID for logging bot activities.
LOGGER_ID = get_int("LOGGER_ID", -1003972764819)

DEBUG_IGNORE_LOG = True

# Telegram user ID of the owner.
OWNER_ID = get_int("OWNER_ID", 6018803920)
CODE_CREW_CHANNEL = "https://t.me/thecodecrew"
# --------------------------------------------------
# HEROKU CONFIGURATION
# --------------------------------------------------

HEROKU_APP_NAME = get_env("HEROKU_APP_NAME")
HEROKU_API_KEY = get_env("HEROKU_API_KEY")

# --------------------------------------------------
# UPSTREAM REPOSITORY
# --------------------------------------------------

UPSTREAM_REPO = get_env(
    "UPSTREAM_REPO",
    "https://github.com/slayer123700/AloneMusic",
)

UPSTREAM_BRANCH = get_env("UPSTREAM_BRANCH", "master")
GIT_TOKEN = get_env("GIT_TOKEN")

# --------------------------------------------------
# SUPPORT LINKS
# --------------------------------------------------

SUPPORT_CHANNEL = get_env(
    "SUPPORT_CHANNEL",
    "https://t.me/LoyaItyLess",
)

SUPPORT_CHAT = get_env(
    "SUPPORT_CHAT",
    "https://t.me/LoyaItyLess",
)

# --------------------------------------------------
# ASSISTANT SETTINGS
# --------------------------------------------------

AUTO_LEAVING_ASSISTANT = get_bool(
    "AUTO_LEAVING_ASSISTANT",
    False,
)

# --------------------------------------------------
# SPOTIFY CONFIGURATION
# --------------------------------------------------

SPOTIFY_CLIENT_ID = get_env("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = get_env("SPOTIFY_CLIENT_SECRET")

# --------------------------------------------------
# PLAYLIST AND FILE SIZE LIMITS
# --------------------------------------------------

PLAYLIST_FETCH_LIMIT = get_int("PLAYLIST_FETCH_LIMIT", 25)

# Telegram file size limits, in bytes.
TG_AUDIO_FILESIZE_LIMIT = get_int(
    "TG_AUDIO_FILESIZE_LIMIT",
    104857600,
)

TG_VIDEO_FILESIZE_LIMIT = get_int(
    "TG_VIDEO_FILESIZE_LIMIT",
    1073741824,
)

# --------------------------------------------------
# PYROGRAM USER SESSIONS
# --------------------------------------------------

# Generate your sessions using a trusted session generator.
# Never commit session strings to a public repository.
STRING1 = get_env("STRING_SESSION")
STRING2 = get_env("STRING_SESSION2")
STRING3 = get_env("STRING_SESSION3")
STRING4 = get_env("STRING_SESSION4")
STRING5 = get_env("STRING_SESSION5")

# --------------------------------------------------
# INTERNAL BOT DATA
# --------------------------------------------------

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# --------------------------------------------------
# IMAGE URLS
# --------------------------------------------------

START_IMG_URL = get_env(
    "START_IMG_URL",
    "https://i.ibb.co/99NrkQjn/photo-2026-10-13-06-09-53-7696030749559881736.jpg",
)

PING_IMG_URL = get_env(
    "PING_IMG_URL",
    "https://image-link.edgeone.app/1791871666033-9gtgif.jpg",
)

PLAYLIST_IMG_URL = (
    "https://repgyetdcodkynrbxocg.supabase.co/storage/v1/object/public/"
    "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
)

STATS_IMG_URL = (
    "https://repgyetdcodkynrbxocg.supabase.co/storage/v1/object/public/"
    "https://i.ibb.co/0V89tqgs/photo-2026-10-13-06-08-59-7696030517631647780.jpg"
)

TELEGRAM_AUDIO_URL = (
    "https://repgyetdcodkynrbxocg.supabase.co/storage/v1/object/public/"
    "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
)

TELEGRAM_VIDEO_URL = TELEGRAM_AUDIO_URL

STREAM_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
SOUNCLOUD_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
YOUTUBE_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://image-link.edgeone.app/1791871688204-wrcgkl.jpg"


# --------------------------------------------------
# TIME CONVERSION
# --------------------------------------------------

def time_to_seconds(time):
    """Convert a colon-separated time string to seconds."""
    stringt = str(time)
    parts = stringt.split(":")

    try:
        return sum(
            int(part) * 60 ** index
            for index, part in enumerate(reversed(parts))
        )
    except ValueError:
        raise ValueError(
            f"Invalid time format: {time!r}"
        ) from None


DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")


# --------------------------------------------------
# CONFIGURATION VALIDATION
# --------------------------------------------------

if SUPPORT_CHANNEL and not re.match(
    r"^https?://",
    SUPPORT_CHANNEL,
    re.IGNORECASE,
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https:// or http://"
    )

if SUPPORT_CHAT and not re.match(
    r"^https?://",
    SUPPORT_CHAT,
    re.IGNORECASE,
):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https:// or http://"
    )

# Warn about missing credentials without printing their values.
missing_variables = []

for variable in ("API_HASH", "BOT_TOKEN", "MONGO_DB_URI"):
    if not get_env(variable):
        missing_variables.append(variable)

if missing_variables:
    raise SystemExit(
        "[ERROR] Missing required environment variables: "
        + ", ".join(missing_variables)
        + ". Configure them in your .env file."
    )

