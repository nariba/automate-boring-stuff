#!/usr/bin/python3

stuff = \
    {'allow' : 12, 'gold coin' : 42, 'rope' : 1, 'torch' : 6, 'shuriken' : 1}

def display_inventory(stuff):
    count = 0
    for k, v in stuff.items():
        print(str(v) + ' : ' + k)
        count += v
    print('The number of inventory : ' + str(count))

if __name__ == "__main__":
    display_inventory(stuff)