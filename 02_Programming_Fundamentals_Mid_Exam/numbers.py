numbers = input().split()
numbers_as_integers = []

for number in numbers:
    numbers_as_integers.append(int(number))

avg_num = int(sum(numbers_as_integers) / len(numbers_as_integers))
if len(numbers_as_integers) >= 5:

    biggest_numbers = []
    for i in numbers_as_integers:
        if i > avg_num:
            biggest_numbers.append(str(i))
    biggest_numbers = sorted(biggest_numbers, reverse=True)[:5]
    result = ' '.join(biggest_numbers)
    print(result)
else:
    print('No')