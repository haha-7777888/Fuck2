
#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/ZeroTwo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/ZeroTwo/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from ZeroTwo import app
from ZeroTwo.misc import SUDOERS
from ZeroTwo.utils import help_pannel
from ZeroTwo.utils.database import get_lang
from ZeroTwo.utils.decorators.language import LanguageStart, languageCB
from ZeroTwo.utils.inline.help import help_back_markup
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(
    filters.regex("^settings_back_helper$") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    if isinstance(update, types.CallbackQuery):
        try:
            await update.answer()
        except Exception:
            pass

        if not update.message:
            return

        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)

        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )
    else:
        try:
            await update.delete()
        except Exception:
            pass

        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)

        await update.reply_photo(
            photo=START_IMG_URL,
            has_spoiler=False,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    # Use the same help text as private /help.
    keyboard = help_pannel(_)

    await message.reply_text(
        _["help_1"].format(SUPPORT_CHAT),
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
    )


@app.on_callback_query(
    filters.regex("^help_callback") & ~BANNED_USERS
)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    parts = callback_data.split(None, 1)

    if len(parts) < 2:
        await CallbackQuery.answer(
            "Invalid help option.",
            show_alert=True,
        )
        return

    cb = parts[1].strip()
    keyboard = help_back_markup(_)

    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.help_1,
            reply_markup=keyboard,
        )

    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.help_2,
            reply_markup=keyboard,
        )

    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.help_3,
            reply_markup=keyboard,
        )

    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.help_4,
            reply_markup=keyboard,
        )

    elif cb == "hb5":
        await CallbackQuery.edit_message_text(
            helpers.help_5,
            reply_markup=keyboard,
        )

    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            helpers.help_6,
            reply_markup=keyboard,
        )

    elif cb == "hb7":
        if CallbackQuery.from_user.id not in SUDOERS:
            await CallbackQuery.answer(
                "ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.",
                show_alert=True,
            )
            return

        await CallbackQuery.edit_message_text(
            helpers.help_7,
            reply_markup=keyboard,
        )

    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            helpers.help_8,
            reply_markup=keyboard,
        )

    elif cb == "hb9":
        await CallbackQuery.edit_message_text(
            helpers.help_9,
            reply_markup=keyboard,
        )

    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            helpers.help_10,
            reply_markup=keyboard,
        )

    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            helpers.help_11,
            reply_markup=keyboard,
        )

    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            helpers.help_12,
            reply_markup=keyboard,
        )

    elif cb == "hb13":
        await CallbackQuery.edit_message_text(
            helpers.help_13,
            reply_markup=keyboard,
        )

    else:
        await CallbackQuery.answer(
            "help page not found.",
            show_alert=True,
        )

