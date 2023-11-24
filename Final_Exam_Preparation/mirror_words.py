import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
matches = re.findall(pattern, data)
mirrored_words = []
pairs_count = len(matches)

for pair in matches:
    if pair[1] == pair[3][::-1]:
        mirrored_words.append(f"{pair[1]} <=> {pair[3]}")

if pairs_count > 0:
    print(f'{pairs_count} word pairs found!')
    if not mirrored_words:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join(mirrored_words))
else:
    print(f"No word pairs found!")
    print(f"No mirror words!")