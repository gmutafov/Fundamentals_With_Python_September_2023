numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))

minimum_number = lambda x: min(x)
maximum_number = lambda x: max(x)
sum_numbers = lambda x: sum(x)


print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_numbers}")