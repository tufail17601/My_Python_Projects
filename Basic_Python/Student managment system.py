students = []
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        print('Fail')

def add_student():
    name = input('Enter student name:')
    student_Id = input('Enter student ID:')
    marks = float(input('Enter student marks:'))

    student = {
        'name' : name,
        'id' : student_Id,
        'marks' : marks,
        'grade' : calculate_grade(marks)
}
    students.append(student)
    print("Student added successfuly:")

def view_student():
    if not students:
        print('No student found')
        return
    for s in students:
            print(f"Name:{s['name']},ID:{s['id']},Marks:{s['marks']},Grade:{s['grade']}")

def search_student():
    sid = input("Enter student id to search:").strip().lower()
    for s in students:
        if s['id'] == sid:
            print(f"Found: {s['name']},ID:{s['id']},Marks:{s['marks']},Grade:{s['grade']}\n")
            return
    print("student not found!\n")

while True:
    print("\n--- student Managment Menu ---")
    print("press (1): For add student")
    print("press (2): For View all students")
    print("press (3): For search student by id")
    print("press (4): For Exit:")

    choice = input("Enter a choice:")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Good By")
        break
    else:
        print("Invalid option ! Try again.")
        
    
