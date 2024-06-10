from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup():
    yes_button = InlineKeyboardButton(text='да', callback_data='yes')
    no_button = InlineKeyboardButton(text='нет', callback_data='no')
    keyboard = InlineKeyboardMarkup()
    keyboard.add(yes_button, no_button)
    return keyboard