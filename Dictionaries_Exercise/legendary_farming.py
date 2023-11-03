items = {'shards': 0, 'fragments': 0, 'motes': 0}
crafted = False

while not crafted:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items['shards'] >= 250:
            print(f"Shadowmourne obtained!")
            items['shards'] -= 250
            crafted = True
        elif items['fragments'] >= 250:
            print(f"Valanyr obtained!")
            items['fragments'] -= 250
            crafted = True
        elif items['motes'] >= 250:
            print(f"Dragonwrath obtained!")
            items['motes'] -= 250
            crafted = True
        if crafted:
            break

for material, quantity in items.items():
    print(f"{material}: {quantity}")