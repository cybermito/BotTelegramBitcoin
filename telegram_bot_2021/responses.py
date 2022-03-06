import re #Este módulo permite encontrar símbolos ($%;-...) en una cadena de caracteres y la pone
#dentro de una lista
def process_message(message, response_array, response):
    #Dividimos el mensaje y la puntuación del mensaje dentro de una lista.
    list_message = re.findall(r"[\w']+|[.,¡!¿?;]", message.lower())
    #Puntuamos el número de coincidencias en las palabras del mensaje para después
    #devolver una respuesta. 

    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    #ahora devolvemos la respuesta y la puntuación de dicha respuesta
    print(score, response)
    return(score, response)

#Esta función toma el mensaje recibido en el bot y devuelve una respuesta customizada
#por nosotros.
def get_response(message):
    #Creamos una lista de respuestas. Podemos ampliarla todo
    #lo que queramos. 
    response_list = [
        process_message(message, ['hola', 'hi', 'ey'], 'Hola'),
        process_message(message, ['adiós', 'adios', 'bye', 'hasta luego'], 'Adiós'),
        process_message(message, ['como', 'estas', 'cómo', 'estas', 'qué', 'tal', 'que'], 'Estoy bien, gracias'),
        process_message(message, ['como','te', 'llamas', 'cuál', 'tu', 'tú','nombre', 'cual'], 'Mi nombre es Cybermito, encantado'),
        process_message(message, ['ayuda', 'help', 'me', 'ayudame', 'ayúdame', 'ayudarme'], 'Haré todo lo posible por ayudarte')
        #Podemos ir añadiendo más mensajes de respuesta en base a lo recibido.
    ]

    #Comprobamos todas las puntuaciones en las respuestas y retornamos la mejor puntuación
    #Esto nos sirve como entrada para inteligencia artificial.

    response_score = []
    for response in response_list:
        response_score.append(response[0])
    
    #Obtenemos el mácimo valor para la mejor respuesta y la guardamos en un variable
    winning_response = max(response_score)
    matching_response = response_list[response_score.index(winning_response)]

    #Retornamos la respuesta ganadora al usuario. 
    if winning_response == 0:
        bot_response = 'No entiendo lo que has escrito.'
    else:
        bot_response = matching_response[1]

    print('Respuesta del Bot:', matching_response[1])
    return bot_response

#Este apartado que está comentado es para testear el algoritmo antes de ser
#ejecutado en el bot
#get_response('¿Cómo te llamas?')
#get_response( '¿Puedes ayudarme?')
#Una vez hemos testeado las funciones, pasamos a aplicarlas en la función principal. 