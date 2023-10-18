# twins = input().split()
# moves = 0
# command = input()
#
# while command != 'end':
#     ind1, ind2 = command.split()
#     ind1 = int(ind1)
#     ind2 = int(ind2)
#     moves += 1
#     out_of_range = False
#     if ind1 not in range(len(twins)) or ind2 not in range(len(twins)):
#         out_of_range = True
#     if ind1 == ind2 or out_of_range:
#         twins.insert((len(twins) // 2), f"-{moves}a")
#         twins.insert((len(twins) // 2), f"-{moves}a")
#         print(f"Invalid input! Adding additional elements to the board")
#     elif twins[ind1] == twins[ind2]:
#         remove_element = twins[ind1]
#         twins.pop(twins.index(remove_element))
#         print(f"Congrats! You have found matching elements - {twins.pop(twins.index(remove_element))}!")
#     else:
#         print('Try again!')
#     if len(twins) == 0:
#         print(f"You have won in {moves} turns!")
#         break
#
#     command = input()
#
#
# else:
#     print(f"Sorry you lose :(")
#     print(*twins, sep=' ')
def main():
    sequence_of_elements = input().split()
    count_of_moves = 0

    while True:
        count_of_moves += 1
        command = input()
        if command == 'end':
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break
        index1, index2 = map(int, command.split())

        if is_invalid_input(index1, index2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, count_of_moves)
        else:
            handle_valid_input(index1, index2, sequence_of_elements, count_of_moves)


def is_invalid_input(index1, index2, sequence):
    return (
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence)
        or index2 >= len(sequence)
    )


def handle_invalid_input(sequence, count_of_moves):
    mid_index = len(sequence) // 2
    sequence.insert(mid_index, f"-{count_of_moves}a")
    sequence.insert(mid_index, f"-{count_of_moves}a")
    print(f"Invalid input! Adding additional elements to the board")


def handle_valid_input(index1, index2, sequence, count_moves):
    if sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        second_element = sequence[index2]
        sequence.pop(index1)
        sequence.remove(second_element)
    else:
        print(f"Try again!")

    if len(sequence) == 0:
        print(f"You have won in {count_moves} turns!")
        exit()


main()
