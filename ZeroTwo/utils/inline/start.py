#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/ZeroTwo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/ZeroTwo/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton

import config
from ZeroTwo import app


def btn(text, style=None, icon=None, **kw):
    try:
        from pyrogram.enums import ButtonStyle

        extra = {}
        if style:
            extra["style"] = getattr(ButtonStyle, style.upper())
        if icon:
            extra["icon_custom_emoji_id"] = str(icon)
        return InlineKeyboardButton(text=text, **kw, **extra)
    except (ImportError, TypeError):
        return InlineKeyboardButton(text=text, **kw)


def start_panel(_):
    return [
        [
            btn(_["S_B_1"], "success", 5134476056241112076,
                url=f"https://t.me/{app.username}?startgroup=true"),
            btn(_["S_B_2"], "success", 5134202243486057363,
                url=config.SUPPORT_CHAT),
        ],
    ]


def private_panel(_):
    return [
        [
            btn(_["S_B_3"], "success", 5134476056241112076,
                url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            btn(_["S_B_2"], "success", 5134202243486057363,
                callback_data="Alone_Music"),
            InlineKeyboardButton(text="💌 ʏᴛ-ᴀᴘɪ", callback_data="bot_info_data"),
        ],
        [
            btn(_["S_B_4"], "success", 5085022089103016925,
                callback_data="settings_back_helper"),
        ],
    ]
