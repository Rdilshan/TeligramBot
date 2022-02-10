import telebot
import os
from PIL import Image

bot = telebot.TeleBot("5112955026:AAEzQR96ek3WxmLaVEDQbNi3KxHNBSjXBTw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "how are you doing?")


@bot.message_handler(commands=['hello'])
def send_welcome(message):

    bot.send_document(message.chat.id,open('D:\pdf.pdf','rb' ) )


@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)

    downloaded_file = bot.download_file(file_info.file_path)
    bot.send_document(message.chat.id, Image.open(file_info.file_path).convert('RGB'))




bot.polling()