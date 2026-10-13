
#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/ZeroTwo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/ZeroTwo/blob/master/LICENSE >
#
# All rights reserved.
#

import logging
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from ZeroTwo import app, YouTube
from ZeroTwo.utils.database import (
    autoplay_off,
    autoplay_on,
    is_autoplay_on,
)
from ZeroTwo.utils.decorators import language, AdminRightsCheck
from config import BANNED_USERS

LOGGER = logging.getLogger(__name__)


@app.on_message(filters.command(["autoplay"]) & filters.group & ~BANNED_USERS)
@language
async def autoplay_command(client, message: Message, _):
    if len(message.command) < 2:
        playmode = await is_autoplay_on(message.chat.id)

        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴇɴᴀʙʟᴇ" if not playmode else "ᴅɪsᴀʙʟᴇ",
                    callback_data="AUTOPLAYCHANGE",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data="close",
                ),
            ],
        ]

        return await message.reply_text(
            _["autoplay_1"],
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    state = message.text.split(None, 1)[1].strip().lower()

    if state == "on":
        await autoplay_on(message.chat.id)
        return await message.reply_text(
            "» ᴀᴜᴛᴏᴘʟᴀʏ ᴇɴᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
        )

    if state == "off":
        await autoplay_off(message.chat.id)
        return await message.reply_text(
            "» ᴀᴜᴛᴏᴘʟᴀʏ ᴅɪsᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ."
        )

    return await message.reply_text(
        "» ɪɴᴠᴀʟɪᴅ ᴀʀɢᴜᴍᴇɴᴛ. ᴜsᴇ ᴏɴ/ᴏғғ."
    )


@app.on_message(filters.command(["askip"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def askip_command(client, message: Message, _, chat_id):
    from ZeroTwo.misc import db
    from ZeroTwo.utils.stream.stream import stream

    if not await is_autoplay_on(chat_id):
        return await message.reply_text(
            "» ɴᴏᴛ ᴏɴ ᴀᴜᴛᴏ ᴘʟᴀʏ. ᴘʟᴇᴀsᴇ ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏ ᴘʟᴀʏ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ."
        )

    check = db.get(chat_id)
    if not check:
        return await message.reply_text(
            "» ᴛʜᴇ ᴘʟᴀʏʙᴀᴄᴋ ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ."
        )

    # Keep the current queue entry until a replacement track is found.
    popped = check[0]
    old_mystic = popped.get("mystic")

    try:
        vidid = popped.get("vidid")
        if not vidid:
            return await message.reply_text(
                "» ᴄᴏᴜʟᴅ ɴᴏᴛ ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ ɪᴅ."
            )

        related = await YouTube.get_related_videos(vidid)
        if not related:
            return await message.reply_text(
                "» ɴᴏ ʀᴇʟᴀᴛᴇᴅ ᴛʀᴀᴄᴋs ғᴏᴜɴᴅ. ᴛʀʏ sᴋɪᴘᴘɪɴɢ ᴀɢᴀɪɴ."
            )

        video_id = random.choice(related)
        details, track_id = await YouTube.track(video_id, True)

        if not details or not details.get("title") or not details.get("vidid"):
            LOGGER.warning(
                "Autoplay skip: track details unavailable for video %s",
                video_id,
            )
            return await message.reply_text(
                "» ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴛʜᴇ ʀᴇʟᴀᴛᴇᴅ ᴛʀᴀᴄᴋ. ᴛʀʏ ᴀɢᴀɪɴ."
            )

        # Remove the old queue item only after a replacement was found.
        if check and check[0] is popped:
            check.pop(0)

        await stream(
            _,
            old_mystic,
            popped["user_id"],
            details,
            chat_id,
            popped["by"],
            popped["chat_id"],
            video=popped.get("streamtype") == "video",
            streamtype="youtube",
            forceplay=True,
        )

    except Exception:
        LOGGER.exception(
            "Autoplay skip failed in chat %s",
            chat_id,
        )
        await message.reply_text(
            "» ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ sᴋɪᴘᴘɪɴɢ. ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ ʟᴏɢs."
        )
