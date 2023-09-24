qty_decoration = int(input())
rem_days = int(input())
ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
lights_price = 15
total_cost = 0
total_spirit = 0

for current_date in range(1, rem_days + 1):
    if current_date % 11 == 0:
        qty_decoration += 2
    if current_date % 2 == 0:
        total_cost += qty_decoration * ornament_price
        total_spirit += 5
    if current_date % 3 == 0:
        total_cost += qty_decoration * (tree_skirt_price + tree_garland_price)
        total_spirit += 13
    if current_date % 5 == 0:
        total_cost += qty_decoration * lights_price
        total_spirit += 17
        if current_date % 3 == 0:
            total_spirit += 30
    if current_date % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + lights_price + tree_garland_price
if rem_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}\nTotal spirit: {total_spirit}")