from telebot import types, TeleBot

bot = TeleBot('7560070316:AAEVgb07N6xxJmApASUI0XMltdIiTA5ifPE')

name = ''
age = 0
@bot.message_handler(contant_types=['text'])

def get_start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Привет друг! Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши: Привет")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'{name} сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age = int(message.text)
    bot.send_message(message.from_user.id, f' {name}, вы {2024 - age} года рождения')
    bot.register_next_step_handler(message, get_start)
    bot.polling(none_stop=True, interval=0)

