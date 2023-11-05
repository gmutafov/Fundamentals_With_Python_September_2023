n = int(input())

grades = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for student, grade in grades.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")