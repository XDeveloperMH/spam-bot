import is
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message



Client = Client(
    "Spam Bot V1",
    bot_token="5200515883:AAHzWS9rax08kVkzo6CSETIBOT8mosKDMU4",
    api_id="8406611",
    api_hash="5820bc246505e0ff60af5391d649f9a6"
)


START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('▪️Add Me To Your Group ▪️', url="http://t.me/Spam_Protector_v1_Bot?startgroup=true")
        ]]
    ) 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am Service Message, command and link deleter bot.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )


@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()
