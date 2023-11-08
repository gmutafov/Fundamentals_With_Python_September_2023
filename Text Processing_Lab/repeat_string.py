# some_strings = input().split()
# result = ''
# for word in some_strings:
#     length = len(word)
#     result += word * length
#
# print(result)
text = input().split()
result = [txt * len(txt) for txt in text]
print(''.join(result))