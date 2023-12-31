# import re
#
# pattern = r'(\#|\|)([A-Za-z]+\s?[A-Za-z]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1'
# text_string = input()
# matches = re.findall(pattern, text_string)
#
# calories = 0
# products = []
#
# for match in matches:
#     item_name = match[1]
#     exp_date = match[2]
#     cals = match[3]
#     calories += int(cals)
#     products.append(f'Item: {item_name}, Best before: {exp_date}, Nutrition: {cals}')
#
# days_cals = calories // 2000
#
# print(f"You have food to last you for: {days_cals} days!")
# print('\n'.join(products))
import re

pattern = r'(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)'

info = input()
matches = re.findall(pattern, info)

total_calories = sum([int(match[5]) for match in matches])
days = total_calories // 2000
print(f'You have food to last you for: {days} days!')

for element in matches:
    item_name = element[1]
    exp_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}")