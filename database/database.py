from database.models import User, Scores, LoggedUsers


class Database:
    def __init__(self) -> None:
        self.module_list = ['география', 'литература', 'химия', 'русский язык',
                            'математика', 'обществознание', 'информатика',
                            'история', 'физика', 'биология', 'иностранный язык']

    @staticmethod
    def add_user(user_id: int, name: str, surname: str) -> None:
        User.create(
            user_id=user_id,
            name=name,
            surname=surname,
        )

    @staticmethod
    def delete_user(user_id: int, student_id: int) -> None:
        pass

    @staticmethod
    def user_exists(user_id: int, name: str, surname: str) -> None:
        return User.get_or_none(User.user_id == user_id,
                                User.name == name,
                                User.surname == surname)

    @staticmethod
    def add_score(student_id: int, user_id: int, module: str, score: str) -> None:
        # check if score exists
        Scores.create(user_id=user_id,
                      student_id=student_id,
                      module_name=module,
                      score=score)

    @staticmethod
    def score_exists(module_name: str, student_id: int) -> bool:
        query = Scores.select().where(Scores.module_name == module_name, Scores.student_id == student_id)
        # return Scores.get_or_none(query)
        if query.exists():
            return True
        else:
            return False


    @staticmethod
    def delete_score(student_id: int, module: str, score_id: int) -> None:
        query = Scores.get(Scores.module_name == module,
                           Scores.student_id == student_id,
                           Scores.score_id == score_id)
        print(query.score_id)
        query.delete_instance()

    @staticmethod
    def update_score(student_id: int, score_id: int, score: str) -> None:
        query = Scores.update(score=score).where(Scores.score_id == score_id, Scores.student_id == student_id)
        query.execute()

    @staticmethod
    def get_scores(student_id):
        return Scores.select().where(Scores.student_id == student_id)

    @staticmethod
    def get_module_by_name(module_name: str):
        return Scores.get(Scores.module_name).where(module_name == Scores.module_name)

    @staticmethod
    def add_logged_user(student_id: int, user_id: int, name: str, surname: str) -> None:
        LoggedUsers.create(student_id=student_id,
                           user_id=user_id,  # telegram user id
                           name=name,
                           surname=surname)

    @staticmethod
    def get_student_id_from_logged_user(user_id: int):
        return LoggedUsers.select(LoggedUsers.student_id).where(user_id == LoggedUsers.user_id)

    @staticmethod
    def get_students_list(user_id: int) -> None:
        return User.select().where(User.user_id == user_id)

    @staticmethod
    def remove_logged_user(user_id: int) -> None:
        query = LoggedUsers.delete().where(LoggedUsers.user_id == user_id)
        query.execute()

    @staticmethod
    def is_logged_in(user_id: int) -> None:
        query = LoggedUsers.select().where(LoggedUsers.user_id == user_id)
        return LoggedUsers.get_or_none(query)


database = Database()
