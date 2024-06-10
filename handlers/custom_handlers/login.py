from database.database import database
from keyboards.inline import promt_yes_no_buttons
from loader import bot
from states.login import LoginStates
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.reply import start_buttons, default_buttons, student_list_buttons
from utils.db import log_student, student_logout


@bot.message_handler(commands=['login'])
def login(message: Message) -> None:
    students = database.get_students_list(user_id=message.from_user.id)
    if students:
        # check if student has logged in
        logged_in = database.is_logged_in(user_id=message.from_user.id)
        if logged_in:
            text = f'Вы уже авторизованы как {logged_in.name} {logged_in.surname}\n' \
                   f'Хотите поменять студента?'
            bot.send_message(chat_id=message.chat.id, text=text,
                             reply_markup=promt_yes_no_buttons.gen_markup())
        else:
            bot.send_message(message.from_user.id, f'Выберите ученика из списка:',
                             reply_markup=student_list_buttons.gen_markup(students)
                             )
            bot.set_state(message.from_user.id, LoginStates.get_user_data, message.chat.id)
    else:
        bot.send_message(message.from_user.id, f'Вы ещё не создали не одного профиля')


@bot.message_handler(state=LoginStates.get_user_data)
def get_user_data(message: Message) -> None:

    name = message.text.strip().lower().split()[0]
    surname = message.text.strip().lower().split()[1]
    log_student(user_id=message.from_user.id, chat_id=message.chat.id, name=name, surname=surname)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(commands=['logout'], state=LoginStates.logout)
def logout(message: Message) -> None:
    student_logout(message.from_user.id, chat_id=message.chat.id)
