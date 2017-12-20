PyQuiz - Quiz Generator
=======================

Renders the quizfile in the number and format given. Supported formats: TEXT, YAML

    Usage:       pyquiz.py QUIZFILE [SEED] [NUMBER] [OUTFORMAT]
                pyquiz.py --quizfile QUIZFILE [--seed SEED] [--number NUMBER] [--outformat OUTFORMAT]

Example:

    python pyquiz.py docs/quizexample.yaml 1 3 TEXT
    # Prova
    [code: 1]
    Provella

    ## Q001 (single):
    Question3

    - [ ] opt2
    - [ ] opt3
    - [ ] opt1

    ## Q002 (multi):
    Question1

    - [ ] opt1
    - [ ] opt2
    - [ ] opt3

    ## Q003 (single):
    Question2

    - [ ] opt2
    - [ ] opt3
    - [ ] opt1


    ---
    # Prova
    [code: 2]
    Provella

    ## Q001 (multi):
    Question1

    - [ ] opt2
    - [ ] opt3
    - [ ] opt1

    ## Q002 (single):
    Question3

    - [ ] opt2
    - [ ] opt3
    - [ ] opt1

    ## Q003 (single):
    Question2

    - [ ] opt1
    - [ ] opt2
    - [ ] opt3


    ---
    # Prova
    [code: 3]
    Provella

    ## Q001 (single):
    Question2

    - [ ] opt3
    - [ ] opt1
    - [ ] opt2

    ## Q002 (single):
    Question3

    - [ ] opt2
    - [ ] opt1
    - [ ] opt3

    ## Q003 (multi):
    Question1

    - [ ] opt3
    - [ ] opt1
    - [ ] opt2