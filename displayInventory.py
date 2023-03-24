stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    total_items = 0
    print("Inventory:")
    for key,value in inventory.items():
        print(f"{value} {key}")
        total_items += value
    print(f"Total number of items: {total_items}")


if __name__ == "__main__":
    displayInventory(stuff)
