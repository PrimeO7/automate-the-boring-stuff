# FantasyGameInventory


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():  # loops through each pair.
        print(v, k)
        item_total = item_total + v  
        # adds the value from each Key-Value pair together with each Iteration.
    print('Total number of items: ' + str(item_total))

if __name__ == '__main__':
    # if __name__ == “main”: is used to execute some code only if the file was
    # run directly, and not imported.

    inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6,
    'dagger': 1}

    displayInventory(inventory)
