import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["عبدو","المطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/a8407158b615e1f3c6a63.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𓏺 𝖠𝖻𝖽𝗈 .
◉ 𝚄𝚂𝙴𝚁 : ❪ @Roejx ❫
◉ 𝙸𝙳      : ❪ 6413369458 ❫
◉ 𝙱𝙸𝙾    : ❪ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @Roejx • ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "• 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 •", url=f"https://t.me/Roejx"),
            ]
        ]
         ),
     )
  
