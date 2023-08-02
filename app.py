import telebot, pandas, os

# from dotenv.main import load_dotenv

# load token
# load_dotenv()
token = "6099300581:AAEMjnQN0gnieIcj029_tuXyNLi7NSAZt88"
sheet_id = "1FUO33IdeaxgFnEfyb0ELkKo6fBBw5JyWH0zfdHH6Stg"

# You can set parse_mode by default. HTML or MARKDOWN
# bot = telebot.TeleBot(token, parse_mode="HTML")
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    data = getData("bot")
    command, ket, mess_list = [], [], []
    for x in data["Perintah"]:
        command.append(x)
    for x in data["Keterangan"]:
        ket.append(x)
    for x in data.index:
        mess_list.append(command[x] + " - " + ket[x])
    bot.send_message(
        message.chat.id,
        f"Selamat datang di Bot Info Fakultas Informatika! \nSilahkan pilih perintah yang diinginkan \n\n{listToString(mess_list)}",
    )


@bot.message_handler(commands=["about"])
def send_welcome(message):
    creator = "Creator: \nt.me/Kendiva 🔥 \n"
    supp = "Supported by: \nFakultas Informatika | Telkom University"
    bot.send_message(message.chat.id, creator + supp)


@bot.message_handler(commands=["mbkm"])
def send_welcome(message):
    data = getData("mbkm")
    link, ket, mess_list = [], [], []
    for x in data["Keterangan"]:
        ket.append(x)
    for x in data["Link"]:
        link.append(x)
    for x in data.index:
        mess_list.append(ket[x] + " \n" + link[x])
    bot.send_message(
        message.chat.id,
        f"Informasi MBKM \n\n{listToString(mess_list)}",
        disable_web_page_preview=True,
    )


@bot.message_handler(commands=["dosen"])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Silahkan masukkan kode dosen yang ingin dicari")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    kode_dosen = message.text
    mess = info_dosen(kode_dosen.upper())
    bot.send_message(chat_id, mess)


def info_dosen(kode_dosen):
    data = getData("dosen")
    mess = f"Perintah tidak valid: {kode_dosen.capitalize()}"
    for x in data["Kode"]:
        if kode_dosen == x:
            data_dosen = data.loc[data["Kode"] == x]
            nama = data_dosen["Nama"].to_string(index=False)
            j_kontak = data_dosen[
                "Jenis Kontak (Whatsapp/Telegram/Nomor Telp)"
            ].to_string(index=False)
            kontak = data_dosen["Kontak"].to_string(index=False)
            mess = f"Kode Dosen \n{x} \n\nNama Lengkap \n{nama}\n\nHubungi melalui \n{j_kontak}\n\nKontak \n{kontak}"
            break
    return mess


def getData(sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    data = pandas.read_csv(url)
    return data


def commandList():
    data = getData("bot")
    command = []
    for x in data["Perintah"]:
        command.append(x)
    return command


def listToString(s):
    str1 = "\n"
    return str1.join(s)


bot.infinity_polling()
