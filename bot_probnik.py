import  pyowm
import telebot

owm = pyowm.OWM("68b4c1a56e57b789f0eed419382ed16b", language="ru")
bot = telebot.TeleBot('1232191030:AAFZQBNGbcFE_uQmLwEjDCUSiSQM2K9F9Sk')

@bot.message_handler(content_types=['text'])
def send_echo(message):

    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас: " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Довольно прохладно / Fa freddo"
    elif temp < 20:
        answer += "Прохладно / Fresco"
    elif temp < 25:
        answer += "Тепло / Calore"
    else:
        answer += "Жарко / Fa caldo"

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
