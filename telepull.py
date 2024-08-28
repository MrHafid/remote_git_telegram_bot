import os
import asyncio
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Masukkan token bot dari BotFather
TOKEN = '****'

ALLOWED_USERS = [123123123, 123123123]  # Ganti dengan ID Telegram pengguna yang diizinkan

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_name = update.message.chat.title if update.message.chat.title else "Group Name"
    await update.message.reply_text(f'Hai aku Printsoft Bot dibuat oleh Hafid, aku ada untuk kebutuhan remote git {group_name}, terimakasih!')

async def puller(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Hanya tanggapi pesan dari admin grup atau pengguna yang diizinkan
    if update.message.chat.type in ['group', 'supergroup'] and update.message.from_user.id in ALLOWED_USERS:
        # Cek nama grup atau supergrup
        group_name = update.message.chat.title if update.message.chat.title else "Group Name"
        # Dapatkan nama command dan hilangkan @username bot jika ada
        command_text = update.message.text.split()[0]
        if '@' in command_text:
            command_name = command_text.split('@')[0]
        else:
            command_name = command_text
            
        if group_name == 'Liteprint' and 'lite' in command_name:
            await update.message.reply_text(f'{group_name} Memproses {command_name}, Mohon ditunggu...')
            # Gunakan subprocess untuk menjalankan perintah git pull
            process = subprocess.Popen('cd /Applications/XAMPP/xamppfiles/htdocs/liteprint && git pull', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
            # Tunggu hingga proses selesai
            stdout, stderr = process.communicate()

            # Ambil output dari stdout dan stderr
            output = stdout.decode('utf-8') + '\n' + stderr.decode('utf-8')

            # Kirim output ke chat
            await update.message.reply_text(f'Output Git Pull {group_name}:\n \n{output}\n ')

        elif group_name == 'LMS' and 'lms' in command_name:
            await update.message.reply_text(f'{group_name} Memproses {command_name}, Mohon ditunggu...')
            # Gunakan subprocess untuk menjalankan perintah git pull
            lms = subprocess.Popen('cd /Applications/XAMPP/xamppfiles/htdocs/lms && git pull', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
            # Tunggu hingga proses selesai
            stdout, stderr = lms.communicate()

            # Ambil output dari stdout dan stderr
            output = stdout.decode('utf-8') + '\n' + stderr.decode('utf-8')

            # Kirim output ke chat
            await update.message.reply_text(f'Output Git Pull {group_name}:\n \n{output}\n ')
        
        else:
        
            await update.message.reply_text('Group tidak sesuai!')
        
    else:
        await update.message.reply_text('Kamu tidak memiliki izin untuk menjalankan perintah ini.')

def main() -> None:
    # Start token bot
    application = Application.builder().token(TOKEN).build()

    # Tambahkan handler untuk perintah /start
    application.add_handler(CommandHandler('start', start))

    # Tambahkan handler untuk perintah /pull
    application.add_handler(CommandHandler('litepull', puller))

    # Tambahkan handler untuk perintah /pull
    application.add_handler(CommandHandler('lmspull', puller))

    # Jalankan polling untuk menerima pesan
    application.run_polling()
    

if __name__ == '__main__':
    main()

