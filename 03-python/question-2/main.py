# Input & Analyze Students
class Student:
    def __init__(self, name, roll_no, department, address, gender, marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.address = address
        self.gender = gender
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = self.total_marks / len(marks)

def main():
    students = []
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        print(f"--- STUDENT {i+1} ---")
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        department = input("Enter department: ")
        address = input("Enter address: ")
        gender = input("Enter gender: ")
        marks = list(map(int, input("Enter marks in three subjects separated by space: ").split()))
        
        student = Student(name, roll_no, department, address, gender, marks)
        students.append(student)

    max_marks_student = max(students, key=lambda s: s.total_marks)
    min_marks_student = min(students, key=lambda s: s.total_marks)
    failed_students = [s.name for s in students if any(mark < 10 for mark in s.marks)]

    print(f"\nStudent Details:\n")
    for student, i in students:
        print(f"--- STUDENT {i+1} ---")
        print(f"Name: {student.name}\nTotal Marks: {student.total_marks}\nPercentage: {student.percentage:.2f}%")
    
    print(f"\nStudent with Maximum Marks: {max_marks_student.name}")
    print(f"Student with Minimum Marks: {min_marks_student.name}")
    print(f"Failed Students: {', '.join(failed_students) if failed_students else 'None'}")

if __name__ == "__main__":
    main()
