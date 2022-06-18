#sameNameLocalGlobal

def spam():
    global eggs
    eggs = 'spam'   # this is global

def bacon():
    eggs = 'bacon'  # this is local

def ham():
    print(eggs)     # this is global because we didn't assign a local variable or global statement for it in that function.

eggs = 42           # this is global
spam()
print(eggs)
