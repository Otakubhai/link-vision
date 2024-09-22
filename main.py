import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import random
from flask import Flask
from threading import Thread
from config import *

bot = Client(
    "Link_Vision",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.command("start"))
async def start(client: Client, msg: Message):
    text = "The Bot is Alive! This Bot was made by @Aakash1230"
    await msg.reply(text)

flask_app = Flask('')

@flask_app.route('/')
def home():
    return "Bot is running", 200

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

@bot.on_message(filters.private & filters.command("anime"))
async def anime(client: Client, msg: Message):
    text = "Which Format Do You Want To Use?!"
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("XOXO", callback_data="xoxo"),
                InlineKeyboardButton("Otaku", callback_data="otaku")
            ]
        ]
    )
    await msg.reply(text, reply_markup=btn)

@bot.on_callback_query()
async def callback(client: Client, query: CallbackQuery):
    data = query.data
    ratings = random.randint(85, 100) 
    tt = ["Thick", "Bumsty", "M!LF", "Big B00bs", "B00bjob", "Bl@w Job", "Stockings", "Mini Bikini", "Step-Sis", "Step Mom", "Winter Surprise", "3sum", "G@ng Bang", "Waifu", "Cosplay", "Hard¢ore", "H@rdcor€", "$lut", "School", "School Girl", "Maid", "Romance", "Drama", "Story", "AV Debut", "Cheating", "Harassment", "Adultery", "Employee", "Hotel", "Adultery", "Creamp!e", "Old Women", "Older Women", "Glamorous", "Model", "BD$M", "Deep Thro@t", "Big A$$", "Huge Boombs", "Thick Women", "Thick Body", "Thick Thighs", "Preety Girl", "Shy Girl", "Beautiful Girl", "Innocent Girl", "Innocent", "Beautiful Women", "Shy Women", "Sensitive Girl", "Highschool", "Student", "Teacher", "Bikini", "Crop Top", "Shorts", "Forced Semx"]
    tag1 = random.choice(tt)
    tag2 = random.choice(tt)
    tag3 = random.choice(tt)
    tag4 = random.choice(tt)
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("One More XoXo", callback_data="xoxo"),
                InlineKeyboardButton("One More Otaku", callback_data="otaku")
            ]
        ]
    )
    if data == "xoxo":
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium,
╠ {tag1}, {tag2}, {tag3}, {tag4}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text, reply_markup=btn)
    elif data == "otaku":
        text = f"""&lt;b&gt;💦 Stepmom Wants Cream Filling On Easter - Winter Tale 
┏━━━━━━━━━━━━━━━━━
┣ 🎥 ᴅᴜʀᴀᴛɪᴏɴ : 20 Min+
┣ ⌛️ ꜱᴛᴀᴛᴜꜱ : ꜰɪɴɪꜱʜᴇᴅ
┣ 🏷 ᴇᴘɪꜱᴏᴅᴇꜱ : 01
┣ 📷 ꆰᴜᴀʟᴛɪʏ : 480p, 720p, 1080p 
┗━━━━━━━━━━━━━━━━━
&lt;blockquote&gt;📝 Tags : #Uncnsored, {tag1}, {tag2}, {tag3}, {tag4}&lt;/blockquote&gt;&lt;/b&gt;"""
        await query.edit_message_text(text, reply_markup=btn)




print("Alive!")
if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.run()