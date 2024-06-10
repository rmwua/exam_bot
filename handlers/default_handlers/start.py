from telebot.types import Message
from loader import bot
from keyboards.reply import start_buttons, default_buttons
from database.database import database


@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    student = database.is_logged_in(user_id=message.from_user.id)
    if student:
        text = f"Привет! Вы вошли как {student.name} {student.surname}"
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=default_buttons.gen_markup())
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Приветствую, {message.from_user.full_name}!",
                         reply_markup=start_buttons.gen_markup())
