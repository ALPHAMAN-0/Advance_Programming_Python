students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def check_marks(marks):
    if len(marks) == 0:
        return "No marks found"
    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid mark " + str(mark)
    return "OK"


def calculate_average(marks):
    return sum(marks) / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    if len(students) == 0:
        print("No students found")
        return
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]
        status = check_marks(marks)
        if status != "OK":
            print(f"ID: {student_id}, Name: {name}, Error: {status}")
        else:
            average = calculate_average(marks)
            performance = classify_performance(average)
            print(f"ID: {student_id}, Name: {name}, Average: {average:.2f}, Performance: {performance}")


print("Student report:")
display_report(students)

print("\nTest 1: Equal marks in all assessments")
display_report([[205, "Tania", [80, 80, 80]]])

print("\nTest 2: Tied averages")
display_report([[206, "Karim", [70, 80, 90]], [207, "Sadia", [90, 80, 70]]])

print("\nTest 3: Invalid mark")
display_report([[208, "Rafi", [85, 120, 90]]])

print("\nTest 4: No marks")
display_report([[209, "Mitu", []]])

print("\nTest 5: Empty student list")
display_report([])
