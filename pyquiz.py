"""An utility to generate shuffled quizzes from a YAML definition"""
import fire
import yaml
from quizzer.loader import QuizzesLoader
from quizzer.printer import Printer


def _producer(quizfile: str, seed: int = 0, number: int = 1):
    with open(quizfile) as qfile:
        printer = Printer(QuizzesLoader(yamlbuffer=qfile.read()))
    return (printer.to_dict(seed + offset) for offset in range(number))

def to_yaml(quizfile: str, seed: int = 0, number: int = 1):
    """Return a YAML document with all the printed shuffled quizzes"""
    return yaml.safe_dump_all(_producer(quizfile, seed, number))

def main():
    """Main program"""
    fire.Fire(to_yaml)

if __name__ == '__main__':
    main()
