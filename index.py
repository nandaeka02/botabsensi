import os
import telebot

API_KEY = "1733533777:AAGeCuSsd005TvCaC4FCN5s4goy_GXfAzhc"
bot = telebot.TeleBot(API_KEY)

whitelist = ['']

@bot.message_handler(commands=["start"])
def greet(message):
    no_id = str(message.from_user.id)
    for userID in whitelist:
        if no_id in userID:
            bot.reply_to(message, "Selamat datang {} {}".format(message.from_user.first_name, message.from_user.last_name))
            @bot.message_handler(commands=["help"])
            def help(message):
                bot.send_message(message.from_user.id, "Ada yang bisa kami bantu?")
        else:
            # bot.reply_to(message, "Anda Belum terdaftar langganan premium. Silahkan daftar dan lakukan pembayaran untuk menggunakan bot ini.")
            print(message.text)
            string = message.text
            string_split = string.split(' ')
            print(string_split[1])
            bot.send_message(message.from_user.id, "Anda Belum terdaftar langganan premium. Silahkan daftar dan lakukan pembayaran untuk menggunakan bot ini.")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.polling()
