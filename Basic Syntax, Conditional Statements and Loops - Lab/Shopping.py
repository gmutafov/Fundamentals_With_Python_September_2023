budget = int(input())
command = input()
total_price = 0
while command != 'End':
    price = int(command)
    total_price += price
    if total_price > budget:
        break
    command = input()
if total_price > budget:
    print(f"You went in overdraft!")
else:
    print(f"You bought everything needed.")