# This is a guessing game program



def game_new():
    guess = input('Enter the guess word')
    word = 'love'
    while guess != word:
        guess = input('try again')

        while guess == word:
            print('You gorit!')
            ans = input('Want to try again')
            if ans == 'no':
                print('bye')
            else:
                game_new()
game_new()



