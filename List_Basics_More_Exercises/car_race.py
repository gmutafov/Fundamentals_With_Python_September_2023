numbers = input().split()
int_numbers = [int(num) for num in numbers]
left_car = []
right_car = []
left_time = 0
right_time = 0
winner = ''

for i in range(len(int_numbers) // 2):

    left_car.append(int_numbers[i])

for j in range(len(int_numbers) // 2):

    right_car.append(int_numbers[-j-1])

for element in left_car:
    left_time += element

    if element == 0:
        left_time = 0.8 * left_time

for el in right_car:
    right_time += el

    if el == 0:
        right_time = 0.8 * right_time

if left_time > right_time:
    winner = 'right'
    print(f"The winner is {winner} with total time: {right_time:.1f}")

else:
    winner = 'left'
    print(f"The winner is {winner} with total time: {left_time:.1f}")