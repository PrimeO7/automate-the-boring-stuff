# picnicTable


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicitems = {'Sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 9001}
printPicnic(picnicitems, 13, 5)
printPicnic(picnicitems, 20, 6)
