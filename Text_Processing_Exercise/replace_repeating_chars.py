text = input()
final_msg = ''
last_added_char = ''

for current_char in text:
    if current_char != last_added_char:
        final_msg += current_char
        last_added_char = current_char

print(final_msg)