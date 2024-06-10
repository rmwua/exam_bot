from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.database import database


def gen_markup():
    keyboard = InlineKeyboardMarkup(row_width=2)
    for module in database.module_list:
        button = InlineKeyboardButton(text=module, callback_data=module)
        keyboard.add(button)
    return keyboard

