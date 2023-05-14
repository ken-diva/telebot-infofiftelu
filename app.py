import telebot, pandas, os
from dotenv.main import load_dotenv

# load token
load_dotenv()
token = os.environ["BOT_TOKEN"]

# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(token, parse_mode=None) 

# ini untuk jawaban defaultnya
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hi, silahkan masukkan kode dosen yang ingin dicari!")

@bot.message_handler(commands=['about'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Creator: t.me/Kendiva")
	
# @bot.message_handler(commands=['help'])
# def send_welcome(message):
# 	bot.reply_to(message, "aku bot kedua :D")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	chat_id = message.chat.id
	kode_dosen = message.text
	mess = info_dosen(kode_dosen.upper())
	bot.send_message(chat_id, mess)
	
def info_dosen(kode_dosen):
	file = ("test.xlsx") # taro file datanya disini
	data = pandas.read_excel(file)
	mess = f"Data tidak ditemukan untuk kode dosen: {kode_dosen.capitalize()}"
	for x in data["kode"]:
		if kode_dosen == x:
			data_dosen = data.loc[data['kode'] == x]
			# formatting purpose
			nama = data_dosen['nama']
			no_hp = data_dosen["no.hp"]
			mess = f"Kode Dosen: {x} \nNama Lengkap: {nama.to_string(index=False)}\nNo.Telp: 0{no_hp.to_string(index=False)}"
			break
	return mess

bot.infinity_polling()

