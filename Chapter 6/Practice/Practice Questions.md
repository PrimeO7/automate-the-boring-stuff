# Practice Questions

1. What are escape characters?

        \t Tab

        \n Newline(linebreak)
   
        \' Single quote
   
        \" Double quote

        \\ Backslash

2. Already answerd in first question.

3. How can you put a \ backslash character in a string?

        With \\ escape charackter or in a raw string
        example: r' This\is\a\ test\.  

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
   
        The single quote works because double quotes are used to mark the beginning and end of the string.

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

        with multiline strings

6. What do the following expressions evaluate to?

        'Hello, world!'[1] == 'e'
        'Hello, world!'[0:5] == 'Hello'
        'Hello, world!'[:5] == 'Hello'
        'Hello, world!'[3:] == 'lo, world!'

7. What do the following expressions evaluate to?

        'Hello'.upper() == 'HELLO'
        'Hello'.upper().isupper() == True
        'Hello'.upper().lower() == 'hello'

8. What do the following expressions evaluate to?

        'Remember, remember, the fifth of November.'.split() == ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

        '-'.join('There can be only one.'.split()) == 'There-can-be-only-one.'

9. What string methods can you use to right-justify, left-justify, and center a string?

        .rjust()
        .ljust()
        .center()

10. How can you trim whitespace characters from the beginning or end of a string?

        .rstrip()
        .lstrip()
        .strip() ---> removes all whitespaces left and right
        