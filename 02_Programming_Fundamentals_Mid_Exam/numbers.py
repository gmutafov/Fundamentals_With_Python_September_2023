
numbers = list(map(int, input().split()))
topNumbers = []

if len(numbers) < 5:
    print("No")
    exit()

sumNum = sum(numbers)
averageNumIs = sumNum * 1.00 / len(numbers)

for currentNum in numbers:
    if currentNum > averageNumIs:
        topNumbers.append(currentNum)

if len(topNumbers) > 5:
    topNumbers.sort(reverse=True)
    for num in topNumbers[:5]:
        print(num, end=" ")
else:
    topNumbers.sort(reverse=True)
    for num in topNumbers:
        print(num, end=" ")