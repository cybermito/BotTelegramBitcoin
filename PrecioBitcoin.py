from bs4 import BeautifulSoup
import requests
import schedule

TOKEN = 'TOKEN' #Aquí indicamos el Token de nuestro bot
chatId = '315986624' #Este es el identificador de nuestro usuario de chat en el bot.

#<td class="wbreak_word align-middle coin_price">$60,832.60</td>
#Esta función hace webscraping de la web indicada para sacar el precio del bicoin.
def btc_scraping():
    url_bitcoin = 'https://awebanalysis.com/es/coin-details/bitcoin/'
    url = requests.get(url_bitcoin)
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class' : 'coin_price' })
    format_result = result.text

    return format_result

#Como encontrar el chatId
#En el bot ejecutamos /start
#En el navegador escribimos la siguiente url: Después de la palabra bot pegamos nuestro token.
#https://api.telegram.org/bot2057379615:AAEo6kDvXLvVqFOMwV8JhKu-b3CoCigOWNE/getUpdates
#Nos sale una serie de información en formato Json, identificamos el id nuestro como chat: id: y el número.
#No coger el update_id, este no es.

def bot_send_text(bot_message):
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + bot_message
    #            https://api.telegram.org/bot2057379615:AAEo6kDvXLvVqFOMwV8JhKu-b3CoCigOWNE/sendMessage?chat_id=315986624&parse_mode=Markdown&text='Escribe /start para iniciar el bot'

    response = requests.get(send_text)
    return response

#test_bot = bot_send_text('Escribe /start para iniciar el bot')
#print(test_bot)

def report():
    btc_price = f'El precio del Bitcoin es de {btc_scraping()}'
    bot_send_text(btc_price)
    
if __name__ == '__main__':

    schedule.every().day.at("18:11").do(report)

    while True:
        schedule.run_pending()