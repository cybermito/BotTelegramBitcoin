import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started....")

def start_command(update, context): #Definimos una función que responderá al comando /start.
    update.message.reply_text('Type something to get started')

def help_command(update, context): #Definimos una función que responderá al comando /help.
    update.message.reply_text('If you need help! You should ask for it on Google')

def handle_message(update, context): #Definimos una función que responderá al mensaje que escribamos, lo hará llamndo a la librería que
    #hemos creado en el fichero Responses.py
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context): #Si ocurre algún error esta función es llamada y nos devolverá el tipo de error ocurrido. 
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True) #Creamos el objeto updater al cuál le pasamos nuestro Token. use_context lo ponemos
    #True para mantener compatibilidad hacia atrás, a partir de la versión 13 no es necesario ponerlo por que por defecto está en True.
    dp = updater.dispatcher #generamos el objeto dispatcher.

    dp.add_handler(CommandHandler("start", start_command)) #creamos el comando /star que ejecutará la función start_command
    dp.add_handler(CommandHandler("help", help_command)) #creamos el comando /help que ejecutará la función help_command

    dp.add_handler(MessageHandler(Filters.text, handle_message)) #Aquí lo que hace es comprobar el mensaje recibido en el bot, lo filtra y solo
    #coge el texto, el cuál pasa a la función handle_message.

    dp.add_error_handler(error) #si se detecta un error, se ejecuta la función error declarada inicialmente.

    updater.start_polling() #se pone en modo escucha esperando las actualizaciones de mensajes o comandos en el bot
    updater.idle() #Parece ser que para el programa hasta que recibe una señal del actualizador para ejecutarla. 

main()