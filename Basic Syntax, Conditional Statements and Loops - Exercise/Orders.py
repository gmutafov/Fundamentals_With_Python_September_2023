n = int(input())
days_counter = 0
total_price = 0
for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if price > 100 or price < 0.01:
        continue
    if days > 31 or days < 1:
        continue
    if capsules > 2000 or capsules < 1:
        continue
    current_price = (price * capsules) * days
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${total_price:.2f}")