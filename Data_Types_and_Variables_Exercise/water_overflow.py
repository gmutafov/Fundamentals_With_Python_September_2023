capacity = 255
n = int(input())
total_water = 0
for line in range(n):
    liters = int(input())
    if capacity - liters < 0:
        print(f"Insufficient capacity!")
        continue
    capacity -= liters
    total_water += liters
print(total_water)