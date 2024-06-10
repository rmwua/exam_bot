from keyboards.reply import default_buttons, start_buttons
from loader import bot
from states.login import LoginStates
from telebot.types import Message, ReplyKeyboardRemove
from database.database import database


@bot.message_handler(commands=['view_scores'])
def view_scores(message: Message):
    if database.is_logged_in(message.from_user.id):
        student_id = database.is_logged_in(user_id=message.from_user.id).student_id
        scores = database.get_scores(student_id=student_id)
        if scores:
            text = ''
            for score in scores:
                text += f'{score.module_name}: {score.score}\n'

            bot.send_message(chat_id=message.chat.id,
                             text=text,
                             reply_markup=default_buttons.gen_markup())
        else:
            bot.send_message(chat_id=message.chat.id,
                             text='Вы еще ничего не добавили',
                             reply_markup=default_buttons.gen_markup())
    else:
        text = 'Войдите в аккаунт, чтобы просматривать данные.'
        bot.send_message(message.from_user.id, text=text,
                         reply_markup=start_buttons.gen_markup())