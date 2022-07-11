# CommaCode

def CommaCode(parameter):
    string = ''
    for i, element in enumerate(parameter):  # splits the list in Index and value and returns it as a tuple
        if i == 0:
            string = string + element
        elif i == len(parameter) - 1:
            string = string + ', and ' + element
        else:     
            string = string + ', ' + element
    return string


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

print(CommaCode(spam))
