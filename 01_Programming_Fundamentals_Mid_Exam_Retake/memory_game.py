twins = input().split()
moves = 0
command = input()

while command != 'end':
    ind1, ind2 = command.split()
    ind1 = int(ind1)
    ind2 = int(ind2)
    moves += 1
    out_of_range = False
    if ind1 not in range(len(twins)) or ind2 not in range(len(twins)):
        out_of_range = True
    if ind1 == ind2 or out_of_range:
        twins.insert((len(twins) // 2), f"-{moves}a")
        twins.insert((len(twins) // 2), f"-{moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif twins[ind1] == twins[ind2]:
        remove_element = twins[ind1]
        twins.pop(twins.index(remove_element))
        print(f"Congrats! You have found matching elements - {twins.pop(twins.index(remove_element))}!")
    else:
        print('Try again!')
    if len(twins) == 0:
        print(f"You have won in {moves} turns!")
        break

    command = input()


else:
    print(f"Sorry you lose :(")
    print(*twins, sep=' ')