#!/usr/bin/python3

stuff = \
    {'allow' : 12, 'gold coin' : 42, 'rope' : 1, 'torch' : 6, 'shuriken' : 1}

dragon_loot = ['gold coin', 'shuriken', 'gold coin', 'gold coin', 'ruby']

def display_inventory(stuff):
    count = 0
    for k, v in stuff.items():
        print(str(v) + ' : ' + k)
        count += v
    print('The number of inventory : ' + str(count))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1

if __name__ == "__main__":
    display_inventory(stuff)
    add_to_inventory(stuff, dragon_loot)
    display_inventory(stuff)