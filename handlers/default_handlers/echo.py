from telebot.types import Message
from loader import bot
from handlers.custom_handlers import register, login, view_scores, delete_score, delete_user, enter_scores
from utils import db
from database.database import database


@bot.message_handler(func=lambda message: True)
def echo_all(message) -> None:
    if message.text == 'Новый ученик':
        register.register(message)

    if message.text == 'Посмотреть результаты':
        view_scores.view_scores(message)

    if message.text == 'Добавить результаты':
        enter_scores.new_score(message)

    if message.text == 'Назад':
        bot.delete_state()
    if message.text == 'Войти':
        if database.is_logged_in(message.from_user.id):
            pass
        else:
            login.login(message)
    if message.text == 'Выйти':
        login.logout(message)

