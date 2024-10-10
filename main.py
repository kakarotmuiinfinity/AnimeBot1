import time
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = '7849002758:AAHQ_AXCbvlpgfQqr5nZeRaCbV9FBNmYW0k'
STICKER_ID = 'CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAe'
PHOTO_URL = 'https://files.catbox.moe/j1fnq9.jpg'

# Start command function
async def start(update: Update, context):
    user_full_name = update.message.from_user.full_name
    bot_name = context.bot.username

    # Step 1: Send "🔥" after 2 seconds
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🔥")
    time.sleep(2)

    # Step 2: Send sticker after another 2 seconds
    message_sticker = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=STICKER_ID)
    time.sleep(2)

    # Step 3: Delete sticker and send "▣☐☐"
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_sticker.message_id)
    message_progress = await context.bot.send_message(chat_id=update.effective_chat.id, text="▣☐☐")
    time.sleep(2)

    # Step 4: Edit message to "☐▣☐"
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=message_progress.message_id, text="☐▣☐")
    time.sleep(2)

    # Step 5: Edit message to "☐☐▣"
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=message_progress.message_id, text="☐☐▣")
    time.sleep(2)

    # Step 6: Send photo with caption and buttons
    caption = f"Hᴇʟʟᴏ {user_full_name}✨\nMʏsᴇʟғ {bot_name}\nWᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ?\nI ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!"
    buttons = [
        [InlineKeyboardButton("✇ Aɴɪᴍᴇ Gʀᴏᴜᴘ ✇", url="https://t.me/Cartoon_Heaven")],
        [InlineKeyboardButton("❁ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ❁", url="https://t.me/Cartoon_Carnival")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=PHOTO_URL, caption=caption, reply_markup=reply_markup)

# Main function to run the bot
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    await application.start()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
  
