"""The printer"""
from quizzer.loader import QuizzesLoader


class Printer(object):
    """Printer of Quizzes"""

    def __init__(self, quizzes: QuizzesLoader, seed: int = 0):
        self.quizzes = quizzes
        self.seed = seed

    def to_dict(self, customseed=None):
        """dictionary of the printable quizzes"""
        seed = customseed if customseed is not None else self.seed
        diz = dict(title=self.quizzes.title, description=self.quizzes.description, quizzes=[])
        for num, quiz in enumerate(self.quizzes.list_quizzes(seed), start=1):
            quiz['id'] = 'Q{0:03d}'.format(num)
            diz['quizzes'].append(quiz)
        return diz
