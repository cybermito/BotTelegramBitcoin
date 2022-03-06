import logging

from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import MessageAutoDeleteTimerChanged, update

from constantes import CYBERMITOTOKEN

#Creamos el log del sistema para acceder a los mensajes de error y/o del programa
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

#Creamos el objeto que cogerá todas las actualizaciones/mensajes que reciba nuestro bot
#para pasarlo al dispatcher.
updater = Updater(token=CYBERMITOTOKEN, use_context=True)
dispatcher = updater.dispatcher

#A partir de aquí podemos crear las funciones callback que responderán a los handlers que creemos. 

def start(update, context): #Este callback permite argumentos múltiples
    #print(update)
    print(update.message.text)
    print()
    print(context.args)
    mensaje_usuario = " ".join(context.args)

    update.message.reply_text ("Has dicho: " + mensaje_usuario)

def respuesta(update, context):
    usuario = update.effective_user.username
    update.message.reply_text("Hola " + usuario)

start_handler = CommandHandler('start', start)
#dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(start_handler)

respuesta_handler = MessageHandler(Filters.text & (~Filters.command), respuesta)
dispatcher.add_handler(respuesta_handler)

updater.start_polling()
updater.idle()