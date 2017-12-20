"""TDD of QuizzesLoader class"""
import unittest
from quizzer.loader import QuizzesLoader, repeatable_random_list
from quizzer.printer import Printer

class TddQuizzesLoader(unittest.TestCase):
    """QuizzesLoader's TDD"""

    TESTYAML = """
        title: Prova
        description: Provella

        quizzes:
            - text: Question1
              multi: True
              options:
                - opt1
                - opt2
                - opt3
            - text: Question2
              multi: False
              options:
                - opt1
                - opt2
                - opt3
            - text: Question3
              options:
                - opt1
                - opt2
                - opt3
    """

    def test_loader_repeatable_random_list(self):
        """Repeatable random"""
        self.assertListEqual(repeatable_random_list(10, 10), repeatable_random_list(10, 10))
        self.assertNotEqual(repeatable_random_list(10, 10), repeatable_random_list(5, 10))

    def test_loader_add_list(self):
        """Adding and listing"""
        loader = QuizzesLoader('Prova', 'Provella')
        self.assertEqual(loader.title, 'Prova')
        self.assertEqual(loader.description, 'Provella')
        self.assertListEqual(loader.list_quizzes(), [])
        loader.add(text='Text', options=['opt1', 'opt2', 'opt3'])
        self.assertNotEqual(loader.list_quizzes(), [])

    def test_loader_yaml(self):
        """Loading and dumping from/to YAML"""
        loaded = QuizzesLoader()
        loaded.load(self.TESTYAML)
        self.assertTrue(loaded.list_quizzes())
        reloaded = QuizzesLoader(yamlbuffer=loaded.dump())
        self.assertEqual(loaded, reloaded, msg='{0}\n!=\n{1}'.format(loaded, reloaded))


class TddPrinter(unittest.TestCase):
    """Printer's TDD"""

    def test_printer(self):
        """Testing the output"""
        loaded = QuizzesLoader(yamlbuffer=TddQuizzesLoader.TESTYAML)
        printer = Printer(loaded)
        self.assertTrue(printer.to_dict())
        self.assertDictEqual(printer.to_dict(), printer.to_dict())
        self.assertNotEqual(printer.to_dict(1), printer.to_dict(2))
    