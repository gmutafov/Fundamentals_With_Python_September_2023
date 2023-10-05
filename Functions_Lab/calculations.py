def solve(operator, a, b):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


operator = input()
a = int(input())
b = int(input())
result = solve(operator, a, b)

print(result)
