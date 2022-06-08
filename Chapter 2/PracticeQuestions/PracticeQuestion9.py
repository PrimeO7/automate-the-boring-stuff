# test

import random, sys

while True:
    spam = random.randint(1,10)
    print(spam)


    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings')
    print('Press Q to exit')
    playerMove = input()
    if playerMove == 'Q' or playerMove == 'q':  # Previous Issue was playerMove == 'Q' or 'q' | since the string 'q' is not empty it is true and would always trigger the exit with every input.
        print('fuvk')
        sys.exit()
        