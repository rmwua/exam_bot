from loader import bot
from states.register_user import UserInfoState
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.reply import cancel_button
from utils.db import add_user


@bot.message_handler(commands=['register'])
def register(message: Message) -> None:
    bot.send_message(message.from_user.id, f'Введите имя',
                     reply_markup=ReplyKeyboardRemove()
                     )
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if message.text.isalpha():
        with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
            data['name'] = message.text.strip().lower()
        bot.send_message(message.from_user.id, 'Теперь введите фамилию')
        bot.set_state(message.from_user.id, UserInfoState.surname, message.chat.id)
    else:
        bot.send_message(message.from_user.id, f'Имя может содержать только буквы')


@bot.message_handler(state=UserInfoState.surname)
def get_surname(message: Message) -> None:
    if message.text.isalpha():
        with bot.retrieve_data(user_id=message.from_user.id) as data:
            data['surname'] = message.text.strip().lower()
            add_user(user_id=message.from_user.id, data=data, chat_id=message.chat.id)
    else:
        bot.send_message(message.from_user.id, f'Фамилия может содержать только буквы')




