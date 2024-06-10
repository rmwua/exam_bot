from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def gen_markup():
    logout_button = KeyboardButton(text='Выйти')
    view_scores_button = KeyboardButton(text='Посмотреть результаты')
    enter_scores_button = KeyboardButton(text='Добавить результаты')
    # delete_user = KeyboardButton(text='Удалить пользователя')
    # delete_score = KeyboardButton(text='Удалить результат')
    keyboard = ReplyKeyboardMarkup(row_width=3)
    keyboard.add(view_scores_button, enter_scores_button, logout_button)
    return keyboard
