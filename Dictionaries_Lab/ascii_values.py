list_of_char = input().split(', ')
char_dict = {char: ord(char) for char in list_of_char}

print(char_dict)