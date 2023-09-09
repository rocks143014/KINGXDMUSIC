
from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def next_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settings_back_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="🤫 ηєϰᴛ 🤫", callback_data="settings_back_helper"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🥰αᴅмιи🥰",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="😛αυтн😛",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="😡вℓσᴄк😡",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💀ɢᴄαѕт💀",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="😈ɢвαи😈",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🥵ʟуяιᴄs🥵",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥶ᴘʟαʏʟιѕт🥶",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="😎νσι𝙲𝙴-𝙲нαт😎",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🤫𝐏𝐋𝐀𝐘🤫",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="😮𝐒𝐔𝐃𝐎😮",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="😝ѕтαят😝",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def next_back_markup(_):
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
                    text="😶 ηєϰᴛ 😶", callback_data="settings_back_helper"
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
