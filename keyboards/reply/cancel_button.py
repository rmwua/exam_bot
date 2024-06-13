from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def gen_markup():
    cancel_button = KeyboardButton(text='Отменить')
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(cancel_button)
    return keyboard
