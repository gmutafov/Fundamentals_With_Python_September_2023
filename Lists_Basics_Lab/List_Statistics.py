n = int(input())
positive_list = []
negative_list = []
for _ in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive_list.append(numbers)
    elif numbers < 0:
        negative_list.append(numbers)

print(f"{positive_list}\n"
      f"{negative_list}\n"
      f"Count of positives: {len(positive_list)}\n"
      f"Sum of negatives: {sum(negative_list)}")