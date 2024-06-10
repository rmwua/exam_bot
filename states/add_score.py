from telebot.handler_backends import State, StatesGroup


class AddScore(StatesGroup):
    module_list = ['география', 'литература', 'химия', 'русский язык',
                   'математика', 'обществознание', 'информатика',
                   'история', 'физика', 'биология', 'иностранный язык']

    add_module = State()
    add_score = State()
