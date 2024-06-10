from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    name = State()
    surname = State()
    add_to_db = State()
