# allmyCats2

# The right way of doing lists

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + # length of list is 0, +1 is added and put out as a string.
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concateation

print('The cat names are:')
for name in catNames:
    print(' ' + name)
    