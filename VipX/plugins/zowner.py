from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
# Command
PLAY_COMMAND = get_command("PLAY_COMMAND")
GSTATS_COMMAND =get_command("GSTATS_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")
STOP_COMMAND = get_command("STOP_COMMAND")
SKIP_COMMAND = get_command("SKIP_COMMAND")
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")
SEEK_COMMAND = get_command("SEEK_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
UNGBAN_COMMAND = get_command("UNGBAN_COMMAND")
GBANNED_COMMAND = get_command("GBANNED_COMMAND")
SETTINGS_COMMAND = get_command("SETTINGS_COMMAND")
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
GETVAR_COMMAND = get_command("GETVAR_COMMAND")
UPDATE_COMMAND = get_command("UPDATE_COMMAND")
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")
ADDSUDO_COMMAND = get_command("ADDSUDO_COMMAND")
DELSUDO_COMMAND = get_command("DELSUDO_COMMAND")
GETLOG_COMMAND = get_command("GETLOG_COMMAND")
BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")
AUTH_COMMAND = get_command("AUTH_COMMAND")
UNAUTH_COMMAND = get_command("UNAUTH_COMMAND")
BLACKLISTCHAT_COMMAND = get_command("BLACKLISTCHAT_COMMAND")
UNBLOCK_COMMAND = get_command("UNBLOCK_COMMAND")
BLOCK_COMMAND = get_command("BLOCK_COMMAND")
GBAN_COMMAND = get_command("GBAN_COMMAND")

@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/147b45b43a964e146fa9b.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴇᴄᴛ ᴏᴡɴᴇʀ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😇 ʀᴏᴄᴋʏ 😇", url=f"https://t.me/ROCKY_ISS_BACK")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/3a2b010905848b0a27afc.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/66aa80c1153a20238e974.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/66aa80c1153a20238e974.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴇᴄᴛ ᴏᴡɴᴇʀ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😇 ʀᴏᴄᴋʏ 😇", url=f"https://t.me/ROCKY_ISS_BACK")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/471f5efc4676676c469b8.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/N91Ab/6")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/471f5efc4676676c469b8.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/N91Ab/6")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/471f5efc4676676c469b8.jpg",
        caption=f"""🍁ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/N91Ab/6")
                ]
            ]
        ),
    )

#Must Learn 

@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/471f5efc4676676c469b8.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /play 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
