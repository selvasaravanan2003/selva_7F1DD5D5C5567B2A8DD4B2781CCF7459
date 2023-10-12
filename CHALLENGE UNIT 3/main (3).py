class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Use the sorted function to sort the list of students by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.6),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7),
]

students2 = [
    Student("Eva", "E005", 3.5),
    Student("Frank", "F006", 3.4),
    Student("Grace", "G007", 3.7),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

# Print the sorted lists of students
print("Sorted Students 1:")
for student in sorted_students1:
    print(f"{student.name} ({student.roll_number}) - CGPA: {student.cgpa}")

print("\nSorted Students 2:")
for student in sorted_students2:
    print(f"{student.name} ({student.roll_number}) - CGPA: {student.cgpa}")
