sequence_of_numbers = input().split()
string = [i for i in input()]
message = ''

for num in sequence_of_numbers:

    index = sum([int(digit) for digit in num])

    if index > len(string):
        index = index - len(string)
    message += string[index]
    string.remove(string[index])

print(message)