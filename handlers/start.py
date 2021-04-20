from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋 there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Chat me @bossfightbot""",
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
                        " ASSISTEN 🎙️", url="https://t.me/lifeisuckx"
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
                        "🎙️ Support Group 🎙️", url="https://t.me/daisysupport_Official")
                ]
            ]
        )
   )

