# globalStatement

def spam():
    global eggs     # If you have a line such as global eggs at the top of a function, it tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.”
    eggs = "spam"

eggs = 'global'
spam()
print(eggs)