orders = {}

while True:
    command = input()
    if command == 'buy':
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in orders.keys():
        orders[name] = {'price': price, "quantity": quantity}
    else:
        orders[name]['price'] = price
        orders[name]['quantity'] += quantity

for product, price_qty in orders.items():
    total_price = price_qty['price'] * price_qty['quantity']
    print(f"{product} -> {total_price:.2f}")