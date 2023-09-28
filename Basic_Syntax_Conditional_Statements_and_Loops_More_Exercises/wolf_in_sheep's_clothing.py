animals = input().split(", ")
an_list = list(animals)

if an_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    result = an_list.index("wolf")
    print(f"Oi! Sheep number {(len(an_list) - 1) - result}! You are about to be eaten by a wolf!")