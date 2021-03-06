from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""đ **Há´á´Ęá´ {message.from_user.mention()}**\n
đ§đľđśđ đśđ đđľđ˛ đŻđšđŽđ°đ¸ đ°đŽđ...!**
âââââââââââââââââââ
âŁÂť á´á´ á´á´ęąÉŞá´ á´Ęá´Ęá´Ę Ęá´á´. 
âŁÂť ĘÉŞÉ˘Ę ÇŤá´á´ĘÉŞá´Ę á´á´ęąÉŞá´.
âŁÂť á´ ÉŞá´á´á´ á´Ęá´Ę ęąá´á´á´á´Ęá´á´á´.
âŁÂť á´á´á´ á´É´á´á´á´ ę°á´á´á´á´Ęá´ęą.
âŁÂť ęąá´á´á´Ęę°á´ęąá´ ęąá´á´á´á´.
âââââââââââââââââââ
á´á´ęąÉŞÉ˘É´á´á´ ĘĘ :** [đđšđŽđ°đ¸ đ°đŽđ](https://t.me/The_cat_lover0)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("á´á´á´á´á´É´á´ ĘÉŞęąá´", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "ęąá´á´á´á´Ęá´", url=f"https://t.me/catmusicworld"
                    ),
                    InlineKeyboardButton(
                        "á´á´á´á´á´á´ęą", url=f"https://t.me/catmusicworld"
                    ),
                ],[
                    InlineKeyboardButton(
                        "đ á´á´á´  Ęá´ĘĘ đ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ęąá´á´á´á´Ęá´", url=f"https://t.me/catmusicworld"),
                InlineKeyboardButton(
                    "á´á´á´á´á´á´ęą", url=f"https://t.me/catmusicworld"
                ),
            ],[
                InlineKeyboardButton("á´ĘĘ ÉŞÉ´ę°á´ Ęá´Ęá´", url=f"https://t.me/catmusicworld"),
            ]
        ]
    )

    alive = f"**Ęá´á´Ęá´ {message.from_user.mention()}, á´ĘÉŞęą ÉŞęą á´Ęá´ ĘĘá´á´á´ á´á´á´.**\n\nÂť á´Ąá´Ęá´ÉŞÉ´É˘ É´á´Ęá´á´ĘĘĘ\nÂť á´á´ á´á´ęąá´á´Ę : [đŻđšđŽđ°đ¸ đ°đŽđ](https://t.me/The_cat_lover0)\nÂť Ęá´á´ á´ á´ĘęąÉŞá´É´ : `v{__version__}`\nÂť á´ĘĘá´ á´ á´ĘęąÉŞá´É´ : `{pyrover}`\nÂť á´Ęá´Ęá´É´ á´ á´ĘęąÉŞá´É´ : `{__python_version__}`\nÂť á´Ęá´É˘á´á´ĘĘęą : `{pytover.__version__}`\nÂť á´á´á´ÉŞá´á´ : `{uptime}`\n\n**á´ĘÉŞęą ÉŞęą á´Ęá´ á´á´ á´á´ęąÉŞá´ á´Ęá´Ęá´Ę Ęá´á´ á´á´ęąÉŞÉ˘É´á´á´ á´É´á´ á´Ęá´á´á´á´á´ ĘĘ ĘĘá´á´á´ á´á´á´  É´á´á´á´Ąá´Ęá´, á´Ęá´É´á´á´ á´ á´ĘĘ á´á´á´Ę ę°á´Ę á´á´á´ÉŞÉ´É˘ Ęá´Ęá´..**\n\nÂŠ @catmusicworld"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**Âť ĘĘá´á´á´ á´á´á´ á´á´É´É˘ ę°Ęá´á´ ĘĘá´á´á´ á´á´á´ É´á´á´á´Ąá´Ęá´ ęąá´Ęá´ á´Ę..**\n\nđ `PONG!!`\n" f"âĄď¸ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "**ĘĘá´á´á´ á´á´á´ Ęá´á´ ęąá´á´á´á´ęą.**\n\n"
        f"â˘ **á´á´á´ÉŞá´á´ :** `{uptime}`\n"
        f"â˘ **ęąá´á´Ęá´ á´á´ :** `{START_TIME_ISO}`"
    )

@Client.on_message(filters.command("pavan") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**á´ĘÉŞęą ÉŞęą á´Ęá´ á´á´ Ęá´á´ á´ĄĘÉŞá´Ę ÉŞęą ęąá´á´á´ÉŞę°ÉŞá´á´ĘĘĘ á´á´ęąÉŞÉ˘É´á´á´ ĘĘ ĘĘá´á´á´ á´á´á´.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "á´ĘĘ ÉŞÉ´ę°á´ Ęá´Ęá´", url="https://t.me/catmusicworld")
                ]
            ]
        )
   )

@Client.on_message(filters.command("aayuu") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**á´ĘÉŞęą ÉŞęą á´Ęá´ á´á´ Ęá´á´ á´ĄĘÉŞá´Ę ÉŞęą ęąá´á´á´ÉŞę°ÉŞá´á´ĘĘĘ á´á´ęąÉŞÉ˘É´á´á´ ĘĘ ĘĘá´á´á´ á´á´á´.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "á´ĘĘ ÉŞÉ´ę°á´ Ęá´Ęá´", url="https://t.me/catmusicworld")
                ]
            ]
        )
   )
