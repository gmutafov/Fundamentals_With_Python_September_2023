some_text = input().split()

filtered_text = [word for word in some_text if len(word) % 2 == 0]
print("\n".join(filtered_text))