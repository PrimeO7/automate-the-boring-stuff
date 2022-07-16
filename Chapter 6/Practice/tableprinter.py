#!/usr/bin/python3
'''tableprinter.py - Takes a list of lists of strings and displays it in a
well-organized table with each column right-justified.'''


# define function printTable()
def printTable(list):
    colWidths = [0] * len(list)
    ''' Creates colWidths[0, 0, 0]'''

    for i in range(len(list)):
        '''if unsure how it works run trough debugger'''
        for j in range(len(list[i])):
            if len(list[i][j]) > colWidths[i]:
                colWidths[i] = len(list[i][j])


    for x in range(len(list[0])):
        for y in range(len(list)):
            print(list[y][x].rjust(colWidths[y]), end = ' ')
        print(' ')


#Provided List
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
