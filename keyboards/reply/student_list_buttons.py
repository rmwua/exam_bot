from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from database.database import database
from database.models import User


def gen_markup(students):
    keyboard = ReplyKeyboardMarkup()
    for student in students:
        text = f'{student.name} {student.surname}'
        button = KeyboardButton(text=text)
        keyboard.add(button)
    return keyboard
