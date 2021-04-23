from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hallo 👋 aku bot untuk pemutar music di group , invite aku ke group kamu dan jadikan admin untuk memutar music dan jangan lupa menambahkan asisten ku @lifeisuckx untuk info cara mengunakan bot klik < cara mengunakan bot > di bawah """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "👑 OWNER 👑", url="https://t.me/Bossfightbot")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 GROUP CHAT 👨‍💻", url="https://t.me/loveiswarXVII"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "CARA MENGUNAKAN BOT", url="https://telegra.ph/command-XVII-MUSIC-04-23"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/loveiswarxvii")
                ]
            ]
        )
   )

