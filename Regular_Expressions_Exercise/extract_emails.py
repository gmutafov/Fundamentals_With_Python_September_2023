import re


sentence = input()

pattern = r' (([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
extracted = re.findall(pattern, sentence)

for email in extracted:
    print(email[0])