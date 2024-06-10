from telebot.handler_backends import State, StatesGroup


class LoginStates(StatesGroup):
    login = State()
    get_user_data = State()
    logout = State()