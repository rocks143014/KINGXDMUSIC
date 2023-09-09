from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="☯︎ᴘяєѕσиαʟ☯︎",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="⚠︎𝙶𝙻𝙾𝙱𝙰𝙻⚠︎", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="♲︎тσᴘ 10 ʟιѕт♲︎", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="☮︎ σωи ☮︎", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="☢ ɢ𝙻σвα𝙻 ☢", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="❄︎ɢяσυᴘ❄︎", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝗕𝗔𝗖𝗞 ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✫𝙰𝚄𝙳𝙸𝙾✫", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="✫𝚅𝙸𝙳𝙴𝙾✫", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝗕𝗔𝗖𝗞 ☆", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="♲︎тσᴘ 10 ʟιѕт♲︎", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="☯︎ᴘяєѕσиαʟ☯︎", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="☢ ɢ𝙻σвα𝙻 ☢", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="❄︎ɢяσυᴘ❄︎", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝗕𝗔𝗖𝗞 ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝗕𝗔𝗖𝗞 ☆",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✦𝐃𝐄𝐋𝐄𝐓𝐄✦",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☆ 𝗕𝗔𝗖𝗞 ☆",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="☆ 𝗖𝗟𝗢𝗦𝗘 ☆",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
