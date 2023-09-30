list_of_numbers = input().split()
count_of_numbers_to_remove = int(input())
list_of_numbers_as_integers = []
small_numbers = 0

for element in list_of_numbers:
    list_of_numbers_as_integers.append(int(element))

for i in range(len(list_of_numbers_as_integers)):
    list_of_numbers_as_integers.remove(min(list_of_numbers_as_integers))
    small_numbers += 1

    if small_numbers >= count_of_numbers_to_remove:
        break

print(*list_of_numbers_as_integers, sep = ', ')