PyQuiz - Quiz Generator
=======================

Renders the quizfile in the number and format given. Supported formats: TEXT, YAML

    Usage:      pyquiz.py QUIZFILE [SEED] [NUMBER] [OUTFORMAT]
                pyquiz.py --quizfile QUIZFILE [--seed SEED] [--number NUMBER] [--outformat OUTFORMAT]

Example: creating ten shuffled tests and split them into single markdown files; then, coverting to PDF.

    rm -f xx*; python pyquiz.py docs/quizexample.yaml --number 10 | csplit - '/^---$/' '{*}
    for MD in xx*; do md2pdf $MD --output test-$MD.pdf; done
