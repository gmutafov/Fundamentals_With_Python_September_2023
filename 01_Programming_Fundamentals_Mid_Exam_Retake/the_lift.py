waiting_people = int(input())
current_state_of_lift = input().split()
state_of_lift_in_digits = []
for state_of_lift in current_state_of_lift:
    state_of_lift_in_digits.append(int(state_of_lift))
for wagon in range(len(state_of_lift_in_digits)):
    while state_of_lift_in_digits[wagon] < 4 and waiting_people> 0:
        state_of_lift_in_digits[wagon] += 1
        waiting_people -= 1

total_lift_size = len(state_of_lift_in_digits) * 4

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif total_lift_size > sum(state_of_lift_in_digits):
    print(f"The lift has empty spots!")
print(*state_of_lift_in_digits, sep=' ')