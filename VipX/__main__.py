import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VipX import LOGGER, app, userbot
from VipX.core.call import Vip
from VipX.plugins import ALL_MODULES
from VipX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VipX").error(
            "🙄 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 😐"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VipX").warning(
            "🥲 𝐒𝐢𝐫 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐈𝐝 & 𝐒𝐞𝐜𝐫𝐞𝐭 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝. 𝐃𝐨𝐧𝐭 𝐖𝐨𝐫𝐫𝐲 𝐍𝐨𝐭 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐄𝐧𝐣𝐨𝐲 𝐓𝐞𝐧𝐬𝐢𝐨𝐧 𝐅𝐫𝐞𝐞 🥰"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VipX.plugins." + all_module)
    LOGGER("VipX.plugins").info(
        "😋 𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲 🎉"
    )
    await userbot.start()
    await Vip.start()
    await Vip.decorators()
    LOGGER("VipX").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️ 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗥𝗢𝗖𝗞𝗬 ♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VipX").info("😢 𝐒𝐨𝐫𝐫𝐲 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ☹️")
