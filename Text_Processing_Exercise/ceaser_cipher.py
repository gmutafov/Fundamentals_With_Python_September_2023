message = input()
encrypted_msg = ''

for char in message:
    encrypted_char = chr(ord(char) + 3)
    encrypted_msg += encrypted_char
    
print(encrypted_msg)