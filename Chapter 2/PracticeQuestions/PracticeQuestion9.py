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
    if playerMove == 'Q' or 'q':
        sys.exit()   
    continue

    # How to loop if PlayeMove != to 'Q' or 'q' ?