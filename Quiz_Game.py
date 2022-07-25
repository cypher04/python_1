# this is a simple multiple choice quiz game

from classes import Question

question_ini = [
    "what is the color of a ball? \n(a)red \n(b)blue \n(c)green\n\n",
    "what is the color of a pen? \n(a)red \n(b)blue \n(c)green\n\n",
    "what is the color of a goat? \n(a)red \n(b)blue \n(c)green\n\n"
]

questions = [
    Question(question_ini[0], 'a'),
    Question(question_ini[1], 'b'),
    Question(question_ini[2], 'c')
]

def laslas(questions):
    score = 0
    for fin_question in questions:
        ans = input(fin_question.prompt)
        if ans == fin_question.answer:
            score += 1
    print('you got' + str(score) + '/' + str(len(questions)) + 'correct')

laslas(questions)



