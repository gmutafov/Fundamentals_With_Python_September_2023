treasure = input().split("|")
commands = input()
sum_of_treasure = 0


while commands != "Yohoho!":
    commands = commands.split()
    if commands[0] == "Loot":
        for num in range(1, len(commands)):
            if commands[num] not in treasure:
                treasure.insert(0, commands[num])

    elif commands[0] == "Drop":
        if int(commands[1]) < len(treasure):
            drop = treasure.pop(int(commands[1]))
            treasure.append(drop)

    elif commands[0] == "Steal":
        stolen = treasure[-int(commands[1]):]
        print(", ".join(stolen))
        if len(treasure) > int(commands[1]):
            left_treasure = len(treasure) - int(commands[1])
            treasure = treasure[:left_treasure]
        else:
            treasure = []

    commands = input()

if len(treasure) > 0:
    for i in treasure:
        sum_of_treasure += len(i)
    avg_gain = sum_of_treasure / len(treasure)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")