some_str = input()
final_str = ''
strength = 0

for index in range(len(some_str)):
    if strength > 0 and some_str[index] != '>':
        strength -= 1
    elif some_str[index] == '>':
        final_str += some_str[index]
        strength += int(some_str[index + 1])
    else:
        final_str += some_str[index]

print(final_str)