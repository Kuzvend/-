import telebot
from constants import token
from telebot import types

bot = telebot.TeleBot(token)


class Anime:
    def __init__(self, zn):
        self.zn = zn


class Qwerty1:
    def __init__(self, zn):
        self.zn = zn


class Qwerty2:
    def __init__(self, zn):
        self.zn = zn


class Qwerty3:
    def __init__(self, zn):
        self.zn = zn


class Qwerty4:
    def __init__(self, zn):
        self.zn = zn


class Qwerty5:
    def __init__(self, zn):
        self.zn = zn


class Qwerty6:
    def __init__(self, zn):
        self.zn = zn


class Qwerty7:
    def __init__(self, zn):
        self.zn = zn


flag = Qwerty4
flag.zn = 0
zakaz = Qwerty5
zakaz.zn = 0
window = Qwerty6
window.zn = 0
code = Qwerty7
code.zn = 0


def log(message, answer):
    print("\n----------------------------------------------------------")
    from datetime import datetime
    t = ""
    print(t, datetime.now())
    code.zn = message.from_user.id
    print(" Сообщение от {0} {1}. id = {2} \n Текст - {3} \n"
          " Заказ - {8}; широта - {4}; "
          "долгота - {5}; квартира - {6}; "
          "этаж - {7}, Доставлено - {8}; Окно - {9}". format(message.from_user.first_name,
                                                             message.from_user.last_name,
                                                             str(code),
                                                             message.text,
                                                             latitude.zn, longitude.zn, flat.zn, floor.zn,
                                                             zakaz.zn, flag.zn, window.zn))
    print(" " + answer)


latitude = Anime
latitude.zn = -1
longitude = Qwerty1
longitude.zn = -1
flat = Qwerty2
flat.zn = -1
floor = Qwerty3
floor.zn = -1


@bot.message_handler(commands=['start'])
def handle_text(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить своё местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, если местоположение пункта назначения совпадает с"
                                      " твоим,"
                                      "иначе просто прикрепи геолокацию пункта назначения",
                     reply_markup=keyboard)
    answer = "Привет! Нажми на кнопку, если местоположение пункта назначения совпадает с твоим," \
             "иначе просто прикрепи геолокацию пункта назначения"
    log(message, answer)


@bot.message_handler(content_types=['location'])
def func_location(message):
    latitude.zn = message.location.latitude
    longitude.zn = message.location.longitude
    bot.send_message(message.from_user.id, "Напиши номер своего заказа")
    log(message, "Напиши номер своего заказа")
    bot.register_next_step_handler(message, get_zakaz)


@bot.message_handler(content_types=["text"])
def qwerty(message):
    if message.chat.id == "id" and message.text == 'open':  # id администратора
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Я открыл окно', callback_data='Window')
        keyboard.add(key_yes)
        bot.send_message(code.zn, "Коптер подлетел к вашему окну. Откройте, пожалуйста, окно.", reply_markup=keyboard)
    else:
        log(message, "Для начала работы бота пропишите команду /start")
        bot.send_message(message.from_user.id, "Для начала работы бота пропишите команду /start")


def get_zakaz(message):
    if message.chat.id == "id" and message.text == 'open':  # id администратора
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Я открыл окно', callback_data='Window')
        keyboard.add(key_yes)
        bot.send_message(code.zn, "Коптер подлетел к вашему окну. Откройте, пожалуйста, окно.", reply_markup=keyboard)
    else:
        if message.text.isdigit() is False:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            log(message, "Цифрами, пожалуйста")
            bot.register_next_step_handler(message, get_zakaz)
        else:
            zakaz.zn = int(message.text)
            bot.send_message(message.from_user.id, "Напиши номер своей квартиры")
            log(message, "Напиши номер своей квартиры")
            bot.register_next_step_handler(message, func)


def func(message):
    if message.chat.id == "id" and message.text == 'open':  # id администратора
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Я открыл окно', callback_data='Window')
        keyboard.add(key_yes)
        bot.send_message(code.zn, "Коптер подлетел к вашему окну. Откройте, пожалуйста, окно.", reply_markup=keyboard)
    else:
        if message.text.isdigit() is False:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            log(message, "Цифрами, пожалуйста")
            bot.register_next_step_handler(message, func)
        else:
            flat.zn = int(message.text)
            bot.send_message(message.from_user.id, "Напиши номер своего этажа")
            log(message, "Напиши номер своего этажа")
            bot.register_next_step_handler(message, get_floor)


def get_floor(message):
    if message.chat.id == "id" and message.text == 'open':  # id администратора
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Я открыл окно', callback_data='Window')
        keyboard.add(key_yes)
        bot.send_message(code.zn, "Коптер подлетел к вашему окну. Откройте, пожалуйста, окно.", reply_markup=keyboard)
    else:
        if message.text.isdigit() is False:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            log(message, "Цифрами, пожалуйста")
            bot.register_next_step_handler(message, get_floor)
        else:
            floor.zn = int(message.text)
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
            keyboard.add(key_yes)
            key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no)
            code.zn = message.from_user.id
            question = "Ваши данные: квартира - {0}, этаж - {1}, заказ - {2}?".format(flat.zn, floor.zn, zakaz.zn)
            bot.send_location(message.chat.id, latitude.zn, longitude.zn)
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
            log(message, question)
            bot.register_next_step_handler(message, qwerty)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Коптер прилетел', callback_data='YES')
    keyboard.add(key_yes)
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Котпер вылетел, ожидайте доставки")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Для изменения адреса перезапусти бота командой /start')
        log(call.message, 'Для изменения адреса перезапусти бота командой /start')
    elif call.data == "YES":
        bot.send_message(call.message.chat.id, 'Спасибо за то, что выбрали именно нашу доставку!, для офорления сле'
                                               'дующего заказа пропишите команду /start')
        log(call.message, 'Спасибо за то, что выбрали именно нашу доставку!, для офорления сле'
                          'дующего заказа пропишите команду /start')
        flag.zn = 1
        window.zn = 0
    elif call.data == 'Window':
        window.zn = 1
        bot.send_message(call.message.chat.id, 'Сейчас коптер залетит к вам в окно. Чтобы подтвердить доставку нажмите '
                                               'кнопку - Коптер прилетел', reply_markup=keyboard)
        log(call.message, "Коптер вылетел. Чтобы подтвердить доставку нажмите кнопку - Коптер прилетел")
        flag.zn = 0


bot.polling(none_stop=True, interval=0)
