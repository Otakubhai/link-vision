import logging
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import random
from flask import Flask
from threading import Thread
from config import *
import os

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize bot
bot = Client(
    "Link_Vision",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.command("start"))
async def start(client: Client, msg: Message):
    logger.info(f"Received /start command from {msg.from_user.id}")
    text = "The Bot is Alive! This Bot was made by @Aakash1230"
    await msg.reply(text)

# Flask app for health check
flask_app = Flask('')

@flask_app.route('/')
def home():
    return "Bot is running", 200

def run_flask():
    logger.info("Starting Flask server for health check.")
    flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Tag groups for the five different categories
tt = ["School", "Random", "Oye", "Test Subject", "IDK", "Moye Moye", "Why"]
Hanime1 = Cosplay1 = JAV1 = Western1 = Indian1 = tt  # For now using tt, you can update these later

@bot.on_message(filters.private & filters.command("anime"))
async def anime(client: Client, msg: Message):
    logger.info(f"Received /anime command from {msg.from_user.id}")
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
    logger.info(f"Callback query received: {data} from {query.from_user.id}")

    # Step 1: After choosing XOXO or Otaku, show 5 more buttons
    if data in ["xoxo", "otaku"]:
        text = "Choose Category!"
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hanime", callback_data="hanime"),
                    InlineKeyboardButton("Cosplay", callback_data="cosplay")
                ],
                [
                    InlineKeyboardButton("JAV", callback_data="jav"),
                    InlineKeyboardButton("Western", callback_data="western"),
                    InlineKeyboardButton("Indian", callback_data="indian")
                ]
            ]
        )
        await query.edit_message_text(text, reply_markup=btn)
        logger.info(f"{data} selected, showing categories.")

    # Step 2: After choosing one of the categories, select from corresponding tag group
    elif data == "hanime":
        selected_tags = random.sample(Hanime1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Hanime callback processed successfully.")

    elif data == "cosplay":
        selected_tags = random.sample(Cosplay1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Cosplay callback processed successfully.")

    elif data == "jav":
        selected_tags = random.sample(JAV1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("JAV callback processed successfully.")

    elif data == "western":
        selected_tags = random.sample(Western1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Western callback processed successfully.")

    elif data == "indian":
        selected_tags = random.sample(Indian1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Indian callback processed successfully.")

    # Step 3: Special format for Otaku
    elif data == "otaku":
        selected_tags = random.sample(tt, 4)
        text = f"""💦 Easter - Winter Tale 
┏━━━━━━━━━━━━━━━━━
┣ 🎥 ᴅᴜʀᴀᴛɪᴏɴ : 20 Min+
┣ ⌛️ ꜱᴛᴀᴛᴜꜱ : ꜰɪɴɪꜱʜᴇᴅ
┣ 🏷 ᴇᴘɪꜱᴏᴅᴇꜱ : 01
┣ 📷 ᴜᴀʟɪᴛʏ : 480p, 720p, 1080p 
┗━━━━━━━━━━━━━━━━━
&lt;blockquote&gt;📝 Tags : #Uncnsored, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}&lt;/blockquote&gt;"""
        await query.edit_message_text(text)
        logger.info("Otaku callback processed successfully.")

print("Alive!")
logger.info("Bot started and running.")
if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.run()import logging
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import random
from flask import Flask
from threading import Thread
from config import *
import os

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize bot
bot = Client(
    "Link_Vision",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.command("start"))
async def start(client: Client, msg: Message):
    logger.info(f"Received /start command from {msg.from_user.id}")
    text = "The Bot is Alive! This Bot was made by @Aakash1230"
    await msg.reply(text)

# Flask app for health check
flask_app = Flask('')

@flask_app.route('/')
def home():
    return "Bot is running", 200

def run_flask():
    logger.info("Starting Flask server for health check.")
    flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Tag groups for the five different categories
tt = ["School", "Random", "Oye", "Test Subject", "IDK", "Moye Moye", "Why"]
Hanime1 = Cosplay1 = JAV1 = Western1 = Indian1 = tt  # For now using tt, you can update these later

@bot.on_message(filters.private & filters.command("anime"))
async def anime(client: Client, msg: Message):
    logger.info(f"Received /anime command from {msg.from_user.id}")
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
    logger.info(f"Callback query received: {data} from {query.from_user.id}")

    # Step 1: After choosing XOXO or Otaku, show 5 more buttons
    if data in ["xoxo", "otaku"]:
        text = "Choose Category!"
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hanime", callback_data="hanime"),
                    InlineKeyboardButton("Cosplay", callback_data="cosplay")
                ],
                [
                    InlineKeyboardButton("JAV", callback_data="jav"),
                    InlineKeyboardButton("Western", callback_data="western"),
                    InlineKeyboardButton("Indian", callback_data="indian")
                ]
            ]
        )
        await query.edit_message_text(text, reply_markup=btn)
        logger.info(f"{data} selected, showing categories.")

    # Step 2: After choosing one of the categories, select from corresponding tag group
    elif data == "hanime":
        selected_tags = random.sample(Hanime1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Hanime callback processed successfully.")

    elif data == "cosplay":
        selected_tags = random.sample(Cosplay1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Cosplay callback processed successfully.")

    elif data == "jav":
        selected_tags = random.sample(JAV1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("JAV callback processed successfully.")

    elif data == "western":
        selected_tags = random.sample(Western1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Western callback processed successfully.")

    elif data == "indian":
        selected_tags = random.sample(Indian1, 4)
        ratings = random.randint(85, 100)
        text = f"""╔════════════════════
╠ 💯 Ratings : {ratings}
╠ 🎨 Tags : #Uncensored, Premium, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}
╠ ⏳Duration : 10 Min+
╠ 🗃File Format : 480p, 720p, 1080p
╚═══════════════════════"""
        await query.edit_message_text(text)
        logger.info("Indian callback processed successfully.")

    # Step 3: Special format for Otaku
    elif data == "otaku":
        selected_tags = random.sample(tt, 4)
        text = f"""💦 Easter - Winter Tale 
┏━━━━━━━━━━━━━━━━━
┣ 🎥 ᴅᴜʀᴀᴛɪᴏɴ : 20 Min+
┣ ⌛️ ꜱᴛᴀᴛᴜꜱ : ꜰɪɴɪꜱʜᴇᴅ
┣ 🏷 ᴇᴘɪꜱᴏᴅᴇꜱ : 01
┣ 📷 ᴜᴀʟɪᴛʏ : 480p, 720p, 1080p 
┗━━━━━━━━━━━━━━━━━
&lt;blockquote&gt;📝 Tags : #Uncnsored, {selected_tags[0]}, {selected_tags[1]}, {selected_tags[2]}, {selected_tags[3]}&lt;/blockquote&gt;"""
        await query.edit_message_text(text)
        logger.info("Otaku callback processed successfully.")

print("Alive!")
logger.info("Bot started and running.")
if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.run()
