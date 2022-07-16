#!/usr/bin/python3
'''tableprinter.py - Takes a list of lists of strings and displays it in a
well-organized table with each column right-justified.'''
import numpy as np

#Define Function printTable()
def printTable(table):
    """Organizing List"""
    t = np.array(table).T
    mylen = np.vectorize(len)
    length = np.amax(mylen(t), axis=0)
    for row in t:
        for element, l in zip(row, length):
            print(element.rjust(l + 1), end='')
        print()


#Provided List
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)