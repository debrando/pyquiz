"""Loader of quizzes"""
from typing import List, Generator
import copy
import yaml
import hashlib

def repeatable_random(seed: int, unique=True):
    """Repeatable random sequence

    from: https://stackoverflow.com/a/18992474/2004580
    """
    produced = set()
    mdseed = bytes(range(seed, seed+64))
    while True:
        mdseed = hashlib.md5(mdseed).digest()
        consumeme = mdseed
        while len(consumeme) >= 4:
            astep = int.from_bytes(consumeme[:4], byteorder='big')
            if unique and astep in produced:
                continue
            yield astep
            produced.add(astep)
            consumeme = consumeme[4:]

def repeatable_random_list(seed: int, size: int):
    """Returns a list of repeatable random numbers"""
    thegen = repeatable_random(seed)
    return [next(thegen) for _ in range(size)]

def shuffle_list(thelist: List, randgen: Generator):
    """Returns a shuffled copy of given list"""
    return [copy.deepcopy(elem) for _, elem in sorted(zip(randgen, thelist))]


class QuizzesLoader(object):
    """The Loader of Quizzes"""

    def __init__(self, title=None, description=None, yamlbuffer=None):
        self._quizzes = []
        self.title = title
        self.description = description
        if yamlbuffer:
            self.load(yamlbuffer)
            # If given, they override the yaml
            self.title = self.title or title
            self.description = self.description or description

    def list_quizzes(self, seed: int = 0):
        """Returns a copy of the quiz list.

        The list and content is shuffled if nonzero seed is provided.
        """
        if seed != 0:
            randgen = repeatable_random(seed)
            qzz = shuffle_list(self._quizzes, randgen)
            for aquiz in qzz:
                aquiz['options'] = shuffle_list(aquiz['options'], randgen)
        else:
            qzz = copy.deepcopy(self._quizzes)
        return qzz


    def add(self, text: str, options: List[str], multi: bool = False):
        """Add a quiz dictionary"""
        self._quizzes.append(dict(text=text, options=copy.deepcopy(options), multi=multi))

    def load(self, yamlbuffer):
        """Load a quiz from a YAML content"""
        source = yaml.load(yamlbuffer)
        self.title = source['title']
        self.description = source['description']
        self._quizzes = []
        for quiz in source['quizzes']:
            self.add(**quiz)

    def dump(self):
        """Return the YAML representation of the quiz"""
        return yaml.dump(dict(
            title=self.title,
            description=self.description,
            quizzes=self._quizzes))

    def __str__(self):
        """Plains string"""
        return self.dump()

    def __repr__(self):
        """Useful representation"""
        return '{0}:{1}'.format(self.title or '-missing-', len(self._quizzes))

    def __hash__(self):
        """Hash for comparison"""
        return hash(self.dump())

    def __eq__(self, other):
        return hash(self) == hash(other)
