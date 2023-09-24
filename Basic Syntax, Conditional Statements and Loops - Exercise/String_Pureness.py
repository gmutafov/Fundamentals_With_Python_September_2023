n = int(input())
for current_string in range(n):
    pure_or_not = input()
    if "," in pure_or_not or \
            "." in pure_or_not or \
            "_" in pure_or_not:
        print(f"{pure_or_not} is not pure!")
    else:
        print(f"{pure_or_not} is pure.")