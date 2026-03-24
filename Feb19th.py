students = {
    "Student1": 85,
    "Student2": 78,
    "Student3": 92,
    "Student4": 67,
    "Student5": 88
}

topper = ""
highest = 0

for name, marks in students.items():
    if marks > highest:
        highest = marks
        topper = name

total = sum(students.values())
average = total / len(students)

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

for name, marks in students.items():
    print(name, ":", marks, ", Grade:", get_grade(marks))

print("\nTopper:", topper, "-", highest)
print("Class Average:", round(average, 2))