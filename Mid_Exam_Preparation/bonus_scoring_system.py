students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus_points = 0
max_student_attendances = 0

for student in range(students_count):
    students_attendances = int(input())
    total_bonus = students_attendances / lectures_count * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        max_student_attendances = students_attendances

print(f"Max Bonus: {round(max_bonus_points)}.\nThe student has attended {max_student_attendances} lectures.")