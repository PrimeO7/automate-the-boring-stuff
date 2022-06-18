# TheCollatzSequenz

def collatz(number):
    if number % 2 == 0:     # If number is even
        print(number // 2)
        return number // 2      # variable is destroyed after the function call. If its not returned it would refer to a variable that does not exist.
    elif number % 2 == 1:       # If number is uneven
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        a = int(input('Please give me a number: '))
        break

    except ValueError:
        print('Please put in a number(integer)')

while a != 1:
            a = collatz(a) # must be int