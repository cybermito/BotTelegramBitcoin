import logging
from telegram.constants import CHATACTION_UPLOAD_DOCUMENT
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
#from telegram.ext import CallbackContext
#from telegram.ext import CommandHandler

TOKEN = 'TOKENCYBERMITOBOT'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

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
