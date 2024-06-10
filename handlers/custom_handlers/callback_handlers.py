from keyboards.reply import default_buttons
from loader import bot
from states.add_score import AddScore
from telebot.types import Message, ReplyKeyboardRemove
from database.database import database


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call) -> None:
    if call.data == 'yes':
        database.remove_logged_user(user_id=call.from_user.id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id)
        bot.send_message(call.message.chat.id, 'Вызовите команду:', reply_markup=ReplyKeyboardRemove())
        bot.send_message(call.message.chat.id, '/login')
    elif call.data == 'no':
        bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.id)
        bot.send_message(chat_id=call.message.chat.id, text='Доступные действия:\n',
                         reply_markup=default_buttons.gen_markup())

    elif call.data in database.module_list:
        bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.id)
        # if database.score_exists(call.data):
        #     bot.send_message(call.from_user.id, f' Ошибка')
        bot.send_message(call.from_user.id, f'Введите балл по предмету {call.data}',
                         reply_markup=ReplyKeyboardRemove())
        bot.set_state(call.from_user.id, AddScore.add_score, call.message.chat.id)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['module'] = call.data

