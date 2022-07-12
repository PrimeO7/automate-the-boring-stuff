# Practice Questions

1. What does the code for an empty dictionary look like?

       name = {}

2. What does a dictionary value with a key 'foo' and a value 42 look like?

        name = {'foo': 42}

3. What is the main difference between a dictionary and a list?
   
        A dictionary is unorderd, while a
        list is orderd. Dictonaries use Keys instead of Indexes, they dont have to be integers starting at 0.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
   
        KeyError because we are trying to access a key that does not exist in a dictionary.

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
   
       'cat' in spam checks in keys be default. It does the same as cat in spam.keys().

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
   
        The 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.
    
7. What is a shortcut for the following code?

    if 'color' not in spam:
    
    spam['color'] = 'black'

        spam.setdefault('color', 'black')

8. What module and function can be used to “pretty print” dictionary values?

        The PPrint Module with pprint.pprint()
        