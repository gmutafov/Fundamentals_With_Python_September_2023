def is_palindrome(some_number_as_string:str) -> bool:
    # if some_number_as_string == some_number_as_string[:: -1]:
    #     return True
    # return False
    return some_number_as_string == some_number_as_string[:: - 1]


numbers_as_string = input().split(', ')
for number_as_string in numbers_as_string:
    print(is_palindrome(number_as_string))