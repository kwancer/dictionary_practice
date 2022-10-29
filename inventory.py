"""file with the inventory function"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    """function which displays the user's inventory as a friendly list"""
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(k)+ " "+ str(v))
        item_total+=1
    print("Total number of items: " + str(item_total))

display_inventory(stuff)
