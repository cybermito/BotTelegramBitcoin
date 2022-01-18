import logging
from telegram.ext import *
from telegram.ext import updater
from telegram.ext import commandhandler
import responses

from constantes import CYBERMITOTOKEN

#Inicializamos el sistema de log del programa
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

#Creamos los comandos para el bot
def start_command(update, context): #Estas funciones definen lo que va a realizar el comando que estamos creando. El argumento update recibe
    #las actualizaciones de mensajes de telegram con lo que nosotros llamaremos al método correspondiente que queramos actue. En este caso
    #responder con un mensaje de texto. context es un argumento que se pone para tener compatibilidad con versiones antiguas de la librería. 
    update.message.reply_text("Hola, Yo soy un bot. ¿Que tal?")

def help_command(update, context):
    update.message.reply_text("Escribe algo e intentaré darte la mejor respuesta")

def custom_command(update, context):
    update.message.reply_text("Este es un comando customizado, tu puedes añadir cualquier comando que quieras.")

#Una vez creados los comandos que vayamos a usar, podemos crear una pequeña lista de dichos comandos en nuestro bot que ayudaran
#a dar una visión de lo que hace cada uno. En cuanto escribamos / saldrá dicha lista. Pero para eso tenemos que ir al botfather y crearla.
#Para eso accedemos al botfather y seleccionando el bot que vamos a programar, le damos a editar, en edición seleccionamos edit commands
#y aquí creamos la lista de comandos que vayamos a programar. 

#Ahora vamos a definir una función que responderá a los mensajes que reciba el bot, ya no como comandos con la /, si no, mensajes directos. 
def handle_message(update, context):
    text = str(update.message.text).lower() #Transformamos el mensaje a mínusculas para así poder interactuar mucho más fácilmente. 
    logging.info(f'Usuario ({update.message.chat.id}) dice: {text} ')

    #Respuesta del bot al mensaje escrito por el usuario. (Responde con el mismo mensaje que se le ha escrito)
    #update.message.reply_text(response)

    #Esta línea es añadida después de crear las respuestas customizadas en el archivo response.py
    response = responses.get_response(text)
    update.message.reply_text(response)

#Definimos una función que controlará los errores que puedas surgir durante la ejecución y nos los sacará por la terminal 
def error(update, context):
    logging.error(f'Update {update} causes error {context.error}')

if __name__ == '__main__':
    updater = Updater(CYBERMITOTOKEN, use_context=True)
    dp = updater.dispatcher

    #Creamos/Activamos los comandos, los cuales hemos definido su funcioamiento en las funciones anteriores.
    dp.add_handler(CommandHandler('start', start_command)) #con CommandHandler creamos los comandos que comienzan con /
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    #Ahora creamos el funcioamiento para recibir los mensajes en el bot e interpretar su contenido para responder a lo que nos dicen.
    dp.add_handler(MessageHandler(Filters.text, handle_message))#con MessageHandler leemos el mensaje escrito por el usuario, filtramos solo el texto
    #y lo pasamos a la función handle_message que es donde programaremos la respuesta al texto escrito. 

    #Ahora creamos el log de todos los errores que puedan suceder
    dp.add_error_handler(error) #Los pasamos a la función error que hemos creado para visualizarlo.

    #Ejecutamos el bot
    updater.start_polling(1.0)# 1.0 es los segundos que queremos que tarde en responder el bot, si lo dejamos a 0 sería instantaneo, pero 
    #para evitar errores mejor dejar un tiempo de margen e la ejecución de la respuesta.
    updater.idle() #¿Para el programa cuando recibe la señal de finalizanción? La descripción en el manual es 
    #Blocks until one of the signals are received and stops the updater. Esta es la última línea que se ejecuta. 






