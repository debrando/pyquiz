"""Loader of quizzes"""
import copy
from typing import List

class Loader(object):
    """The Loader of Quizzes"""

    def __init__(self):
        self._quizzes = []

    @property
    def quizzes(self):
        """Returns a copy of the quiz list"""
        return copy.deepcopy(self._quizzes)

    def add(self, title: str, description: str, options: List[str], multi: bool = False):
        """Add a quiz dictionary"""
        self._quizzes.append(dict(title=title, description=description,
                                  options=copy.deepcopy(options), multi=multi))
