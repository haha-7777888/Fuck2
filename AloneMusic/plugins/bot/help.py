<<<<<<< HEAD:AloneMusic/plugins/bot/help.py
=======

#
# Copyright (C) 2021-2022 by TheAloneteam@Github,
# < https://github.com/TheAloneTeam >.
#
# This file is part of
# < https://github.com/TheAloneTeam/ZeroTwo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see
# < https://github.com/TheAloneTeam/ZeroTwo/blob/master/LICENSE >
#
# All rights reserved.

>>>>>>> f04aaea8476dbfed1015127490c85e9024d7679a:ZeroTwo/plugins/bot/help.py
from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

<<<<<<< HEAD:AloneMusic/plugins/bot/help.py
from AloneMusic import app
from AloneMusic.misc import SUDOERS
from AloneMusic.utils import help_pannel
from AloneMusic.utils.database import get_lang
from AloneMusic.utils.decorators.language import LanguageStart, languageCB
from AloneMusic.utils.inline.help import help_back_markup
=======
from ZeroTwo import app
from ZeroTwo.misc import SUDOERS
from ZeroTwo.utils import help_pannel
from ZeroTwo.utils.database import get_lang
from ZeroTwo.utils.decorators.language import LanguageStart
from ZeroTwo.utils.inline.help import help_back_markup

>>>>>>> f04aaea8476dbfed1015127490c85e9024d7679a:ZeroTwo/plugins/bot/help.py
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string


def get_english_strings():
    """Load English strings from strings/langs/en.yml."""
    return get_string("en")


<<<<<<< HEAD:AloneMusic/plugins/bot/help.py
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: types.CallbackQuery
):
    try:
        await update.answer()
    except:
        pass

    chat_id = update.message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    keyboard = help_pannel(_, True)
    await update.edit_message_text(
        _["help_1"].format(SUPPORT_CHAT),
        reply_markup=keyboard
    )


=======
@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(
    filters.regex("^settings_back_helper$") & ~BANNED_USERS
)
async def helper_private(
    client: app,
    update: Union[types.Message, types.CallbackQuery],
):
    _ = get_english_strings()

    if isinstance(update, types.CallbackQuery):
        try:
            await update.answer()
        except Exception:
            pass

        if not update.message:
            return

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

        keyboard = help_pannel(_)

        await update.reply_photo(
            photo=START_IMG_URL,
            has_spoiler=False,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
async def help_com_group(client, message: Message):
    """Display the help menu in groups using English YAML strings."""
    _ = get_english_strings()
    keyboard = help_pannel(_)

    await message.reply_text(
        _["help_1"].format(SUPPORT_CHAT),
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
    )
>>>>>>> f04aaea8476dbfed1015127490c85e9024d7679a:ZeroTwo/plugins/bot/help.py


@app.on_callback_query(
    filters.regex("^help_callback") & ~BANNED_USERS
)
async def helper_cb(client, CallbackQuery):
    """Load individual help pages from strings/langs/en.yml."""
    _ = get_english_strings()

    callback_data = CallbackQuery.data.strip()
    parts = callback_data.split(None, 1)

    if len(parts) < 2:
        await CallbackQuery.answer(
            "Invalid help option.",
            show_alert=True,
        )
        return

    cb = parts[1].strip()

    if not cb.startswith("hb") or not cb[2:].isdigit():
        await CallbackQuery.answer(
            "Help page not found.",
            show_alert=True,
        )
        return

    page = int(cb[2:])
    key = f"help_{page}"

    # Preserve the sudo-only restriction for page 7.
    if page == 7 and CallbackQuery.from_user.id not in SUDOERS:
        await CallbackQuery.answer(
            "This button is only for sudo users.",
            show_alert=True,
        )
        return

    # Check that the requested page exists in en.yml.
    if key not in _:
        await CallbackQuery.answer(
            f"{key} is missing from strings/langs/en.yml.",
            show_alert=True,
        )
        return

    keyboard = help_back_markup(_)
<<<<<<< HEAD:AloneMusic/plugins/bot/help.py
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        if CallbackQuery.from_user.id not in SUDOERS:
            await CallbackQuery.answer("ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsєʀs.", show_alert=True
            )
            return
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
=======

    await CallbackQuery.answer()
    await CallbackQuery.edit_message_text(
        _[key],
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
>>>>>>> f04aaea8476dbfed1015127490c85e9024d7679a:ZeroTwo/plugins/bot/help.py
