numbers = input().split()
numbers_as_float = []
for number in numbers:
    numbers_as_float.append(abs(float(number)))
print(numbers_as_float)
