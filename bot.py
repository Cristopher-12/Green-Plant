import sys 
import os
import requests
import json
import urllib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "1772293546:AAHjGBU4C3sB-ACs88I7HeUx8bxDc2M5Ocs"

def start(bot,update):
    try:

        username = update.message.from_user.username
        message = "Hola " + username  + " Soy Green Plant Un bot que te ayuda a identificar Plantas"
        
        update.message.reply_text(message)

    except Exception as e:
        print ("Error001: {}".format(error.args[0]))

def help(bot,update):
    try:

        message = """Puedo reconocer Plantas como:
            Bugambilias
            Tulipanes
            Gardenias
            Bonsai
            Pata de elefante"""
        update.message.reply_text(message)

    except Exception as e:
        print ("Error003: "+type(e).__name__)

def getImage(bot,update):
    try:

        message = "Estoy analizando tu imagen. Dame un momento"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id
            
        filename = os.path.join("src/","{}.jpg".format(id))

        file.download(filename)

        r = enviar(id)

        update.message.reply_text(r)

    except Exception as e:
        print ("Error007: "+type(e).__name__)

def enviar(id):
    data2 = {'myfile': open('src/{}.jpg'.format(id), 'rb')}

    url = "https://8080-white-chipmunk-g15f5ty0.ws-us03.gitpod.io/upload?"

    result = requests.post(url, files = data2)

    res = result.json()

    respuesta = res["resultado"]

    return respuesta

def error (bot, update, error):
    try:

        print(error)

    except Exception as e:
        print ("Error004: "+type(e).__name__)


    
def main():
    try:
        token = "1772293546:AAHjGBU4C3sB-ACs88I7HeUx8bxDc2M5Ocs"

        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()

    except Exception as e:
        print ("Error005: "+type(e).__name__)
    
if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print ("Error006: "+type(e).__name__)
