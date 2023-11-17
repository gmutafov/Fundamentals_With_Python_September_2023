import re

some_string = input()

while some_string:
    pattern = r'\d+'
    matches = re.findall(pattern, some_string)
    if matches:
        print(' '.join(matches), end=' ')

    some_string = input()
