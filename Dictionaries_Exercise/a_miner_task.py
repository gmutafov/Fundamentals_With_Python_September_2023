resources = {}
while True:
    current_resources = input()
    if current_resources == 'stop':
        break

    quantity = int(input())
    if current_resources not in resources.keys():
        resources[current_resources] = 0
    resources[current_resources] += quantity

for resources, quantity in resources.items():
    print(f"{resources} -> {quantity}")