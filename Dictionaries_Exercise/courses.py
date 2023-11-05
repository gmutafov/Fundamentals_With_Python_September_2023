courses = {}

while True:
    command = input()
    if command == 'end':
        break

    line = command.split(" : ")
    course_name = line[0]
    student_name = line[1]

    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)

    else:
        courses[course_name].append(student_name)

for course_name in courses:
    print(f"{course_name}: {len(courses[course_name])}")
    for element in courses[course_name]:
        print(f"-- {element}")