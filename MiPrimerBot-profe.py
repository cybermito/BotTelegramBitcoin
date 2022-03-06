from dis import dis
import logging
from telegram.constants import CHATACTION_UPLOAD_DOCUMENT
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

from constantes import CYBERMITOTOKEN
#from telegram.ext import CallbackContext
#from telegram.ext import CommandHandler

#El token lo podemos meter en un archivo aparte e importarlo. Este archivo con los token que guardemos
#lo meteremos en .gitignore para que no se cree repositorio de él. 

"""
    Configuramos el módulo de registro (logs) para conocer como y cuando se ha generado algún error, o no funciona el programa como esperabamos.
    
"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

"""
    Creamos un objeto Updater. La clase updater continuamente busca nuevas actualizaciones que provienen del bot de telegram y
    las pasa a la clase Dispatcher. Cuando creamos un objeto Updater este automáticamente crea un Dispatcher uniendolos con una cola
    de comandos. Podemos crear manipuladores (handlers) de diferentes tipos en el Dispatcher que serán enviados por el Updater de acuerdo
    a los handlers que hayamos registrado y que redirigirá a una función que hayamos definido, devolviendo un resultado (callback).

    clases: telegram.ext.Updater y telegram.ext.Dispatcher 

    Cada manipulador (handler) es una instancia de alguna de las subclases de telegram.ext.Handler. La librería provee handler para la mayoría
    de los casos, pero si se necesita algo más especifico, se puede crear una subclase handler propia.

    El argumento use_context es un argumento especial solamente necesario para la versión 12 de la librería, que por defecto es False. A partir
    de la 13 por defecto es True. Permite una mejor compatibilidad con versiones anteriores de la biblioteca y da a los usuarios algo de tiempo
    para actualizar. 

"""
updater = Updater(token=CYBERMITOTOKEN, use_context=True) #Creamos el objeto Updater
dispatcher = updater.dispatcher #Creamos el dispatcher para un acceso más rapido.
print(updater)
print()
print(dispatcher)
print()


#Definimos las funciones que se ejecutarán según el comando/handler creado. 
#Un handler es una instancia derivada de la clase telegram.ext.Handler.
#La estructura es la siguiente:
''' Definir una función que respondera o será utilizada como Callback a las actualizaciones
que recibamos desde Telegram, un mensaje, un audio, un gif, etc.
Ejemplo: 
def start_callback(update, context):
    update.message.reply_text("Bienvenido a este entretenido bot")

después crearemos el handler en si para que se genere la respuesta a un comando, en
este caso /start

dispatcher.add_handler(commandHandler("start", start_callback))
'''
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, soy un bot, por favor habla conmigo")

def adios(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¿Ya te vas? ¡Quedate un ratito más!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update: Update, context: CallbackContext):
    text_caps =' '. join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

adios_handler = CommandHandler('adios', adios)
dispatcher.add_handler(adios_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

updater.start_polling()
updater.idle()
