from peewee import IntegrityError
from telebot.types import ReplyKeyboardRemove

from keyboards.reply import default_buttons, start_buttons
from keyboards.inline import promt_yes_no_buttons
from loader import bot
from database.database import database
from database.models import User, LoggedUsers


def add_user(user_id: int, data: dict, chat_id: int) -> None:
    try:
        user = database.user_exists(user_id=user_id,
                                    name=data["name"],
                                    surname=data["surname"])
        if user:
            raise IntegrityError
    except IntegrityError:
        bot.send_message(chat_id=chat_id,
                         text='Пользователь с таким именем уже существует',
                         reply_markup=start_buttons.gen_markup())
    else:
        database.add_user(user_id=user_id,
                          name=data['name'],
                          surname=data['surname'])
        text = f'Добавлен новый пользователь {data["name"]} {data["surname"]}'
        bot.send_message(user_id,
                         text=text,
                         reply_markup=start_buttons.gen_markup())
    finally:
        bot.delete_state(user_id=user_id)


def print_users_list(user_id: int, chat_id: int) -> None:
    bot.send_message(chat_id=chat_id,
                     text='Список всех созданных вами пользователей:\n',
                     reply_markup=ReplyKeyboardRemove())
    users = User.select().where(User.user_id == user_id)
    if users:
        text = ''
        for user in users:
            text += f'{user.student_id}. {user.name} {user.surname} \n'

        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_markup=start_buttons.gen_markup())


def log_student(user_id: int, chat_id: int, name: str, surname: str) -> None:
    user = database.user_exists(user_id=user_id,
                                name=name.lower().strip(),
                                surname=surname.lower().strip())
    if user is not None:
        database.add_logged_user(user.student_id, user.user_id, user.name, user.surname)
        text = f'Вы успешно вошли как {user.name} {user.surname}'
        bot.send_message(chat_id=chat_id, text=text,
                         reply_markup=default_buttons.gen_markup())
    elif user is None:
        text = f'Пользователя не существует'
        bot.send_message(chat_id=chat_id, text=text,
                         reply_markup=start_buttons.gen_markup())


def student_logout(user_id: int, chat_id: int) -> None:
    database.remove_logged_user(user_id=user_id)
    print('successfully logged out')
    bot.send_message(chat_id=chat_id, text='вы вышли из аккаунта',
                     reply_markup=start_buttons.gen_markup())


def add_score_to_db(user_id: int, data: dict, chat_id: int) -> None:
    student_id = database.get_student_id_from_logged_user(user_id=user_id)
    module = data['module']
    exists = database.score_exists(module_name=module, student_id=student_id)
    if exists:
        #     database.update_score(score_id=exists.score_id, student_id=student_id, score=data['score'])
        #     print(f'updated {module} {exists.score_id}')
        bot.send_message(chat_id=chat_id,
                         text=f'Предмет уже есть в списке',
                         reply_markup=default_buttons.gen_markup())
    else:
        database.add_score(student_id=student_id,
                           user_id=user_id,
                           module=module,
                           score=data['score'])
        bot.send_message(chat_id=chat_id,
                         text=f'Балл по предмету {module} добавлен',
                         reply_markup=default_buttons.gen_markup())

