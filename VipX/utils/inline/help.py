from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="★ ɱᴏʀε ★", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🍁α𝙳мιи🍁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🙈αυтн🙈",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="😡вʟᴏᴄᴋ😡",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💀𝙶𝙲αѕт💀",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="😈ɢвαи😈",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🥶ʟуяι𝙲ѕ🥶",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="😍𝙿ʟαуℓιѕт😍",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="🥵ѵσι𝙲є-𝙲нαт🥵",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️ᴘʟαу🕹️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="😎sᴜᴅᴏ😎",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥰 𝗦𝗧𝗔𝗥‌𝗧 🥰",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="🤫 мσяє 🤫", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="😇 𝙷𝙴𝙻𝙿 😇",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

