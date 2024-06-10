from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def gen_markup():
    register_button = KeyboardButton(text='Новый ученик')
    login_button = KeyboardButton(text='Войти')
    keyboard = ReplyKeyboardMarkup(row_width=2)
    keyboard.add(register_button, login_button)
    return keyboard

