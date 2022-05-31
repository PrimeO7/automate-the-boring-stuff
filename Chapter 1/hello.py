# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')     # ask for their name

myName = input()

print('It is good to meet you, ' + myName + '.')
print(f'It is good to meet you, {myName}.')
print('The length of your name is:')
print(len(myName))
print('What is your age?')      # ask for their age
myAge = input()                # Input is always a String 
print('You will be ' + str(int(myAge) + 1) + ' in a year.')       # int() converts expression (value) inside brackets to integer
print(f'You will be {int(myAge) + 1 } in a year.')      # f string that I don't understand lol.