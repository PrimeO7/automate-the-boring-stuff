# sameNameError

def spam():
    print(eggs)     #Error!
    eggs = 'spam local'     # This error happens because Python sees that there is
                            # an assignment statement for eggs
                            # in the spam() function and, therefore,
                            # considers eggs to be local. But because print(eggs) is executed
                            # before eggs is assigned anything, the local variable eggs doesn’t exist.
                            # Python will not fall back to using the global eggs variable 

eggs = 'global'
spam()
