from loader import bot
from states.add_score import AddScore
from telebot.types import Message, ReplyKeyboardRemove
from keyboards.inline import module_list_buttons
from keyboards.reply import start_buttons
from utils import db
from database.database import database


@bot.message_handler(commands=['enter_scores'])
def new_score(message: Message) -> None:
    if database.is_logged_in(message.from_user.id):
        bot.set_state(message.from_user.id, AddScore.add_module, message.chat.id)
        text = f'{message.from_user.username} Выберите предмет из списка'
        bot.send_message(message.from_user.id, text=text,
                         reply_markup=module_list_buttons.gen_markup())
    else:
        text = 'Войдите в аккаунт, чтобы добавлять данные.'
        bot.send_message(message.from_user.id, text=text,
                         reply_markup=start_buttons.gen_markup())


@bot.message_handler(state=AddScore.add_score)
def enter_score(message: Message) -> None:
    score = message.text.strip()
    if score.isdigit() and 0 <= int(score) <= 100:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["score"] = score
            db.add_score_to_db(user_id=message.from_user.id, data=data, chat_id=message.chat.id)
        bot.delete_state(message.from_user.id)
    else:
        bot.send_message(message.chat.id, f'Неправильный ввод данных. Попробуйте ввести число от 0 до 100')


