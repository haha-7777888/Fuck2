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


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
    text=_["S_B_1"],
    url=f"https://t.me/{app.username}?startgroup=true",
    style="success",
    icon_custom_emoji_id=5134476056241112076,
),
            InlineKeyboardButton(
    text=_["S_B_2"],
    url=config.SUPPORT_CHAT,
    style="success",
    icon_custom_emoji_id=5134202243486057363,
),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
    text=_["S_B_3"],
    url=f"https://t.me/{app.username}?startgroup=true",
    style="success",
    icon_custom_emoji_id=5134476056241112076,
            )
        ],
        [
            InlineKeyboardButton(
    text=_["S_B_2"],
    callback_data="Alone_Music",
    style="success",
    icon_custom_emoji_id=5134202243486057363,
),
            InlineKeyboardButton(text="💌 ʏᴛ-ᴀᴘɪ", callback_data="bot_info_data"),
        ],
        [
    InlineKeyboardButton(
        text=_["S_B_4"],
        callback_data="settings_back_helper",
        style="success",
        icon_custom_emoji_id=5085022089103016925,
    )
],
    ]
    return buttons
