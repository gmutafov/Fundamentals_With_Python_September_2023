def all_characters(first: str, second: str) -> list:
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters


first_char = input()
second_char = input()
final_result = all_characters(first_char, second_char)
print(" ".join(final_result))