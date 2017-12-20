"""TDD of Loader class"""
import unittest
from quizzer.loader import Loader

class TddLoader(unittest.TestCase):
    """Loader's TDD"""

    def test_loader_add_list(self):
        """Testing the bare creation, adding and list"""
        loader = Loader()
        self.assertIsNotNone(loader)
        self.assertListEqual(loader.quizzes, [])
        loader.add(title='Title', description='Description', options=['opt1', 'opt2', 'opt3'])
        self.assertNotEqual(loader.quizzes, [])
