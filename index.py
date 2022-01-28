import os
import telebot
from telebot import types
import requests
import sys
import traceback
import urllib
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("botabsensi.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://botabsensi-3b7d6-default-rtdb.firebaseio.com/"
	})
ref = db.reference("userid")
# print(ref.get())
# for x in ref.get():
#   print(ref.child(x).get())

API_KEY = "1733533777:AAEk9vE6dF_eSeoJ34eclh1pkOsBmRpqsdg"
bot = telebot.TeleBot(API_KEY)
# db["whitelist"] = ["1245546100","946612767","1931487429"]
whitelist = []
# for x in ref.get():
#   whitelist.append(str(ref.child(x).get()))
  # print(ref.get())
# print(whitelist)

@bot.message_handler(commands=["start"])
def greet(message):
    no_id = str(message.from_user.id)
    # for userID in whitelist:
    if no_id == str(ref.child(no_id).get()):
        bot.reply_to(message, "Selamat datang {} {} di bot absensi Nanchong. Bot ini dibuat untuk membantu mengisikan form absensi.".format(message.from_user.first_name, message.from_user.last_name) +
        "\n\nAdapun beberapa command yang bisa digunakan:" +
        "\n/start untuk memulai bot" +
        "\n/help untuk melihat cara menggunakan command" +
        "\n/absensiuniv untuk mengisi absensi" +
        "\n/payment untuk melakukan pembayaran langganan bot" +
        "\n/cek : untuk melakukan pengecekan ID dan Username"+
        "\n\nDemikian seputar bot Nanchong semoga bisa membantu meringankan beban absen univnya 😁😁😁"
        )
        @bot.message_handler(commands=["help"])
        def help(message):
            bot.send_message(message.from_user.id, "Cara menggunakan botnya:\n\n /absenuniv *email *nama lengkap *nim *nomortelp *jenjang *fakultas *prodi *hurufdepan *namadosen *kodeseksi *namamatkul *sks *minggu *pertemuan\n\nContohnya :\n\n/absenuniv *Ucup Surucup_99999999999@mhs.unj.ac.id *Ucup Surucup *99999999999 *08888888888 *S1 *Fakultas Teknik *(S1) Sistem dan Teknologi Informasi *R *Raharjo, S.Pd.,M.Si. *99999999999 *Pendidikan Pancasila *2 *9 *9")
        
        @bot.message_handler(commands=["absenuniv"])
        def absenuniv(message):
            
            with open('matkul.txt', 'r') as file:
                markup = types.InlineKeyboardMarkup()
                datamatkul = file.read()
                datamatkul = datamatkul.split("\n")
                print(datamatkul)
                for indexdata in datamatkul:
                    removecommand = message.text.replace("/absenuniv","")
                    print(removecommand)
                    string = indexdata+removecommand
                    print(string)
                    newstring = string.replace(" *","*")
                    print(newstring)
                    finalstring = newstring.replace(" ", "%20")
                    print(finalstring)
                    data = finalstring.split('*')
                    print(data)
                    data.pop(0)
                    if len(data) < 7:
                        bot.send_message(message.from_user.id, "Tidak sesuai format harap ulangi!")
                    else:
                        # print(data)
                        entry = ""
                        if data[0] == "A":
                          entry = "entry.2010325683"
                        elif data[0] == "B":
                          entry = "entry.1490912290"
                        elif data[0] == "C":
                          entry = "entry.1655822116"
                        elif data[0] == "D":
                          entry = "entry.1224325679"
                        elif data[0] == "E":
                          entry = "entry.1700993841"
                        elif data[0] == "F":
                          entry = "entry.1264841064"
                        elif data[0] == "G":
                          entry = "entry.415322596"
                        elif data[0] == "H":
                          entry = "entry.1911240248"
                        elif data[0] == "I":
                          entry = "entry.1025120431"
                        elif data[0] == "J":
                          entry = "entry.2040818435"
                        elif data[0] == "K":
                          entry = "entry.174033833"
                        elif data[0] == "L":
                          entry = "entry.54974004"
                        elif data[0] == "M":
                          entry = "entry.935837216"
                        elif data[0] == "N":
                          entry = "entry.2144606882"
                        elif data[0] == "O":
                          entry = "entry.1613190089"
                        elif data[0] == "P":
                          entry = "entry.1624172777"
                        elif data[0] == "Q":
                          entry = "entry.770846117"
                        elif data[0] == "R":
                          entry = "entry.669808987"
                        elif data[0] == "S":
                          entry = "entry.1042103582"
                        elif data[0] == "T":
                          entry = "entry.1756380006"
                        elif data[0] == "U":
                          entry = "entry.173948960"
                        elif data[0] == "V":
                          entry = "entry.929135864"
                        elif data[0] == "W":
                          entry = "entry.652314514"
                        elif data[0] == "X":
                          entry = "entry.1152317860"
                        elif data[0] == "Y":
                          entry = "entry.1152317860"
                        elif data[0] == "Z":
                          entry = "entry.1333095075"
                        links = "https://docs.google.com/forms/d/e/1FAIpQLScXSj_X8mA4AdHBYKV0iGpVhWC_8aNudY7bJPO9agtTukZOlw/viewform?emailAddress=nandaekasuciramadan_1519621004@mhs.unj.ac.id&entry.608390691=Nanda%20Eka%20Suci%20Ramadan&entry.1579586451=1519621004&entry.1079795373=081280716308&entry.1067113942=S1&entry.1315756331=Fakultas%20Teknik&entry.314869359=(S1)%20Sistem%20dan%20Teknologi%20Informasi&entry.1263835528={}&{}={}&entry.148101967={}&entry.865534847={}&entry.820195671={}&entry.496196548={}&entry.644590421=Minggu%20Ke%20-{}&entry.73141647=Pertemuan%20Ke-{}" . format(data[0],entry,data[1],data[1],data[2],data[3],data[4],data[5],data[6])
                        # print(links)
                        URL = "http://tinyurl.com/api-create.php"
                        url = ""
                        try:
                            url = URL + "?" \
                                + urllib.parse.urlencode({"url": links})
                            res = requests.get(url)
                            # print("STATUS CODE:", res.status_code)
                            # print("   LONG URL:", links)
                            # print("  SHORT URL:", res.text)
                            print("Shorten success")
                            url = res.text
                        except Exception as e:
                            raise
                        url_btn = types.InlineKeyboardButton(text="    {}   ".format(data[3].replace("%20"," ")), url=url)
                        markup.add(url_btn)
                bot.send_message(message.from_user.id, text="Silahkan klik tombol yang ada dibawah untuk absen",reply_markup=markup)
    else:
        # print("Username = {} | ID = {}" . format(message.from_user.username, message.from_user.id))
        bot.send_message(message.from_user.id, "Anda Belum terdaftar langganan premium. Silahkan daftar dan lakukan pembayaran untuk menggunakan bot ini. Hubungi pembuat bot jika sudah melakukan pembayaran :"+
        "\n\nhttps://t.me/nanchonggg"+
        "\nhttps://t.me/nanchonggg"+
        "\nhttps://t.me/nanchonggg"+
        "\n\n/payment : untuk melihat metode pembayaran"+
        "\n/cek : untuk melakukan pengecekan ID dan Username"+
        "\n\nKirimkan hasil pengecekan ID dan Username beserta bukti pembayaran ke pembuat bot untuk didaftarkan.", disable_web_page_preview=True
        )
        # break
@bot.message_handler(commands=["cek"])
def cek(message):
  bot.send_message(message.from_user.id,"Username = {} | ID = {}" . format(message.from_user.username, message.from_user.id))  
@bot.message_handler(commands=["payment"])
def payment(message):
  bot.send_message(message.from_user.id, "Untuk sementara pembayaran hanya bisa melalui dana."+
  "\n\nDana : https://link.dana.id/qr/2aw7nb2i"+
  "\nDana : https://link.dana.id/qr/2aw7nb2i"+
  "\nDana : https://link.dana.id/qr/2aw7nb2i"
  ,disable_web_page_preview=True
  )         
print("server active")
bot.polling()
