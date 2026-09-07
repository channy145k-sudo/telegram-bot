import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from gtts import gTTS

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.message.chat_id

    tts = gTTS(text=user_text, lang='km', slow=False)
    
    audio_path = f"voice_{chat_id}.mp3"
    tts.save(audio_path)

    with open(audio_path, 'rb') as audio_file:
        await context.bot.send_voice(chat_id=chat_id, voice=audio_file)

    if os.path.exists(audio_path):
        os.remove(audio_path)

if __name__ == '__main__':
    TOKEN = "8222178811:AAEpoV9RlthU22bK8s6_XS5pm9O0whhUT5c"  # ដាក់ Token របស់អ្នកនៅទីនេះ

    application = ApplicationBuilder().token(TOKEN).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), text_to_speech)
    application.add_handler(echo_handler)

    print("Bot កំពុងដំណើរការ...")
    application.run_polling()

