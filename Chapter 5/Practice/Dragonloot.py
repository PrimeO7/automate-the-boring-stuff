# Dragonloot


import FantasyGameInventory

def addToInventory(inventory, addItems):
    for i in addItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

inventory = {'gold coin': 42, 'rope': 1}

dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = addToInventory(inventory, dragonloot)

FantasyGameInventory.displayInventory(inventory)
