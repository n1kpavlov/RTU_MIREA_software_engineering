import telebot
from telebot import types
import webbrowser
import time

bot = telebot.TeleBot('your_token')
type = ['Услуга №1', 'Услуга №2', 'Услуга №3']
times = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
t = 0
d = ''
tconv = lambda x: time.strftime("%d.%m.%Y", time.localtime(x))


@bot.message_handler(commands=['start', 'restart'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button_1 = types.KeyboardButton('Записаться на услугу')
    button_2 = types.KeyboardButton('Оставить отзыв')
    markup.row(button_1, button_2)
    markup.add(types.KeyboardButton('Перейти на сайт компании'))
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>.\n'
                                      f'Этот шаблон бота создан для помощи предпринимателям '
                                      f'(тект и картинки могут меняться в соответсвии с требованиями заказчика).'
                                      f'С его помощью можно автоматизировать запись клиентов на услуги.\n'
                                      f'Давай ознакомимся с функционалом бота подробнее.', parse_mode='html', reply_markup=markup)
    file = open('./hello.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Могу предложить вам список команд:\n\n'
                                      '/help - вывести список встроеных в бота команд на экран\n'
                                      '/restart - перезапустить бота\n'
                                      '/website - перейти на сайт компании\n'
                                      '/sign_up - записаться на услугу')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://web.telegram.org/k/#@nik_pavlov_1')
    bot.send_message(message.chat.id, 'Надеюсь, вы нашли, что искали')


@bot.message_handler(commands=['sign_up'])
def sign_up(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(f'{type[0]}', callback_data='type_1'))
    markup.add(types.InlineKeyboardButton(f'{type[1]}', callback_data='type_2'))
    markup.add(types.InlineKeyboardButton(f'{type[2]}', callback_data='type_3'))
    bot.send_message(message.chat.id, 'Выберите услугу, на которую хотели бы записаться', reply_markup=markup)



def dates(message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(f'{tconv(message.date + 86400)}', callback_data='date_1')
    button_2 = types.InlineKeyboardButton(f'{tconv(message.date + 172800)}', callback_data='date_2')
    button_3 = types.InlineKeyboardButton(f'{tconv(message.date + 259200)}', callback_data='date_3')
    markup.row(button_1, button_2, button_3)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f'Вы выбрали услугу: <b>{type[t]}</b>\n'
                                      f'Выберите дату посещения', parse_mode='html', reply_markup=markup)


def day_times(message):
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(f'{times[0]}', callback_data='time_1')
    button_2 = types.InlineKeyboardButton(f'{times[1]}', callback_data='time_2')
    button_3 = types.InlineKeyboardButton(f'{times[2]}', callback_data='time_3')
    button_4 = types.InlineKeyboardButton(f'{times[3]}', callback_data='time_4')
    markup.row(button_1, button_2, button_3, button_4)
    button_5 = types.InlineKeyboardButton(f'{times[4]}', callback_data='time_5')
    button_6 = types.InlineKeyboardButton(f'{times[5]}', callback_data='time_6')
    button_7 = types.InlineKeyboardButton(f'{times[6]}', callback_data='time_7')
    button_8 = types.InlineKeyboardButton(f'{times[7]}', callback_data='time_8')
    markup.row(button_5, button_6, button_7, button_8)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f'Выбрана услуга <b>{type[t]}</b> на <b>{d}</b>\n'
                                      f'Можем предложить вам любое доступное время', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.send_message(message.chat.id, 'Если вы уже воспользовались нашей услугой, можете оставить свой отзыв здесь:')
    bot.register_next_step_handler(message, reply)


def reply(message):
    bot.send_message(message.chat.id, 'Спасибо за ваши теплые слова. Будем рады вас видеть снова')


@bot.message_handler()
def info(message):
    if message.text.lower() in ['старт', 'начать', 'restart', 'start', 'begin']:
        start(message)
    elif message.text.lower() in ['помощь', 'help']:
        help(message)
    elif message.text.lower() in ['перейти на сайт компании', 'сайт', 'веб сайт', 'site', 'website']:
        site(message)
    elif message.text.lower() in ['записаться на услугу', 'запись', 'записаться', 'sign up']:
        sign_up(message)
    elif message.text.lower() in ['оставить отзыв', 'отзыв', 'feedback']:
        feedback(message)
    else:
        bot.send_message(message.chat.id, 'Не понимаю, что вы хотите. Если нужна помощь, используйте /help')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global t, d
    if callback.data == 'type_1':
        t = 0
        dates(callback.message)
    elif callback.data == 'type_2':
        t = 1
        dates(callback.message)
    elif callback.data == 'type_3':
        t = 2
        dates(callback.message)
    elif callback.data == 'date_1':
        d = tconv(callback.message.date + 86400)
        day_times(callback.message)
    elif callback.data == 'date_2':
        d = tconv(callback.message.date + 172800)
        day_times(callback.message)
    elif callback.data == 'date_3':
        d = tconv(callback.message.date + 259200)
        day_times(callback.message)
    elif callback.data == 'time_1':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[0]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[1]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_3':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[2]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_4':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[3]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_5':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[4]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_6':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[5]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_7':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[6]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')
    elif callback.data == 'time_8':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, f'Запись прошла успешно.\n'
                                                   f'Будем ждать вас <b>{d}</b> в <em><b>{times[7]}</b></em> '
                                                   f'для оказания услуги <b>{type[t]}</b>', parse_mode='html')



bot.polling(none_stop=True)
