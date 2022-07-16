#!/usr/bin/python3
''' bulletpointadder.py - Adds wikipedia bullet points
to the start of each line of text in the clipboard. '''


import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')  
'''splits the multiline string along the linebreaks and returns a list'''
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add a star to each string in "lines" list

text = '\n'.join(lines) 
''' joins together the list of strings into a single string.
Method is called on string '\n' and gets passed the List 'Lines'
'\n' is inserted between each string of the list argument. '''
pyperclip.copy(text)
