def decode_message(message, commands):
    for line in commands:
        tokens = line.split('|')
        instruction = tokens[0]
        if instruction == 'Move':
            num_of_letter = int(tokens[1])
            message = message[num_of_letter:] + message[:num_of_letter]
        elif instruction == 'Insert':
            index = int(tokens[1])
            value = tokens[2]
            message = message[:index] + value + message[index:]

        elif instruction == 'ChangeAll':
            substring = tokens[1]
            substitute = tokens[2]
            message = message.replace(substring, substitute)

        if instruction == 'Decode':
            print(f"The decrypted message is: {message}")


encrypted_message = input()
commands_list = []

while True:
    command = input()
    commands_list.append(command)
    if command == 'Decode':
        break


decode_message(encrypted_message, commands_list)