list_of_nums = [int(x) for x in input().split()]

while True:
    command = input().split()

    if command[0] == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        list_of_nums[index_one], list_of_nums[index_two] = list_of_nums[index_two], list_of_nums[index_one]
    if command[0] == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])
        list_of_nums[index_one] = list_of_nums[index_one] * list_of_nums[index_two]
    if command[0] == "decrease":
        list_of_nums = [x - 1 for x in list_of_nums]
    if command[0] == "end":
        break

print(", ".join(map(str, list_of_nums)))
