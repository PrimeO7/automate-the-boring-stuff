# validateInput


while True:
    print ('Enter your Age!:')
    age = input()
    if age.isdecimal():
        break
    print ('Please enter a number for your age!')


while True:
    print('Choose a new password:')
    password = input()
    if password.isalnum():
        break
    print('Password can only contain letters and numbers!')
