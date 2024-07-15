import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Masukkan token bot dari BotFather
TOKEN = '7127400318:AAG2P5AQrSy1UstU212ZmEaUQGpTmtzRMXg'

ALLOWED_USERS = [7150361385, 880939368]  # Ganti dengan ID Telegram pengguna yang diizinkan

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hai aku Printsoft Bot, aku ada untuk kebutuhan remote git, terimakasih!')

async def litepull(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Hanya tanggapi pesan dari admin grup atau pengguna yang diizinkan
    if update.message.chat.type in ['group', 'supergroup'] and update.message.from_user.id in ALLOWED_USERS:
        # Jalankan perintah git pull di direktori proyek kamu
        os.system('cd /Applications/XAMPP/xamppfiles/htdocs/liteprint && git pull')
        await update.message.reply_text('Git pull berhasil dijalankan!')
    else:
        await update.message.reply_text('Kamu tidak memiliki izin untuk menjalankan perintah ini.')

def main() -> None:
    # Start token bot
    application = Application.builder().token(TOKEN).build()

    # Tambahkan handler untuk perintah /start
    application.add_handler(CommandHandler('litestart', start))

    # Tambahkan handler untuk perintah /pull
    application.add_handler(CommandHandler('litepull', litepull))

    # Jalankan polling untuk menerima pesan
    application.run_polling()
    

if __name__ == '__main__':
    main()

