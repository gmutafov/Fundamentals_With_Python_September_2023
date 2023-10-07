customer_type = ''
total_price_without_taxes = 0
while True:
    command = input()

    if command == 'special' or command == 'regular':
        customer_type = command
        break
    price = float(command)

    if price <= 0:
        print(f"Invalid price!")
        continue
    taxes = 0.2 * price
    total_price_without_taxes += price

if total_price_without_taxes == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_price_without_taxes * 0.2:.2f}$")
    print(f"-----------")
    total_price_with_taxes = total_price_without_taxes + (total_price_without_taxes * 0.2)

    if customer_type == 'special':
        total_price_with_taxes -= (total_price_with_taxes * 0.1)

    print(f"Total price: {total_price_with_taxes:.2f}$")