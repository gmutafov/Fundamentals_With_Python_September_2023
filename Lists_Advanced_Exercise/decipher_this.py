text = input().split()
for i in range(len(text)):
    current_string = [el for el in text[i]]
    temp_string = ''
    for el in text[i]:
        if el.isdigit():
            temp_string += el
        else:
            break

    current_string = list(filter(lambda x: not x.isdigit(), current_string))
    current_string.insert(0, chr(int(temp_string)))
    current_string[1], current_string[-1] = current_string[-1], current_string[1]
    text[i] = ''.join(current_string)

print(*text, sep=' ')
