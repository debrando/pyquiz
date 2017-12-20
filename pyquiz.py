"""An utility to generate shuffled quizzes from a YAML definition"""
import fire
import yaml
from typing import Generator
from quizzer.loader import QuizzesLoader
from quizzer.printer import Printer


def _producer(quizfile: str, seed: int = 0, number: int = 1):
    with open(quizfile) as qfile:
        printer = Printer(QuizzesLoader(yamlbuffer=qfile.read()))
    return (printer.to_dict(seed + offset) for offset in range(number))

def render_yaml(gen: Generator):
    """YAML renderer"""
    return yaml.safe_dump_all(gen)

def render_text(gen: Generator):
    """YAML renderer"""
    def totext(doc):
        """Convert a single document into text"""
        txt = '# {}\n[code: {}]\n{}\n\n'.format(doc['title'], doc['seed'], doc['description'])
        for quiz in doc['quizzes']:
            txt += '## {} ({}):\n{}\n\n'.format(quiz['id'], 'multi' if quiz['multi'] else 'single', quiz['text'])
            for opt in quiz['options']:
                txt += ' - [ ] {}\n'.format(opt)
            txt += '\n'
        return txt

    return '\n---\n'.join(totext(adoc) for adoc in gen)

def renderer(quizfile: str, seed: int = 0, number: int = 1, outformat: str = 'YAML'):
    """Renders the quizfile in the number and format given.
    
    Supported formats: TEXT, YAML
    """
    if outformat == 'YAML':
        rend = render_yaml
    elif outformat == 'TEXT':
        rend = render_text
    else:
        raise Exception("Unknown output format " + outformat)
    return rend(_producer(quizfile, seed, number))


def main():
    """Main program"""
    fire.Fire(renderer)

if __name__ == '__main__':
    main()
