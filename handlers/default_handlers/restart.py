from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["restart"])
def bot_start(message: Message):
    bot.delete_state(message.from_user.id, message.chat.id)
