banned_list_words = input().split(', ')
text = input()

for word in banned_list_words:
    text = text.replace(word, '*' * len(word))

print(text)