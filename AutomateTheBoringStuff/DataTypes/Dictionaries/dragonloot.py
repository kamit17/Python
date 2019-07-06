

#dragonLoot = {'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'}
inv = {'rope': 1, 'gold coin': 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addItems):
    for k in range(len(addItems)):
        if addItems[k] in inventory.keys():
            inventory[addItems[k]] += 1
        else:
            inventory.setdefault(addItems[k], 1)
    return inventory


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)  # printing the inverntory list
        item_total += v    # keep increasing the count of the value till the whole sum is calculated

    print('Total number of items:  ' + str(item_total))


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
