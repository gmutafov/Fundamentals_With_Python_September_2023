n = int(input())

for i in range(n):
    num = int(input())
    if not num % 2 == 0:
        print(f"{num} is odd!")
        break
if num % 2 == 0:
    print(f"All numbers are even.")