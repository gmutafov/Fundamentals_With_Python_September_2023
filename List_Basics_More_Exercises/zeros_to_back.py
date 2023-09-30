numbers = input().split(', ')
numbers_as_digits = []

for element in numbers:
    numbers_as_digits.append(int(element))

for i in numbers_as_digits:

    if i == 0:
        numbers_as_digits.append(numbers_as_digits.pop(numbers_as_digits.index(i)))

print(numbers_as_digits)