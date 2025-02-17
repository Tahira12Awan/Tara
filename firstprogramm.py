
#  Student Information Management System

# Initialize an empty dictionary to store student information
students = {}

def register_student():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    students[roll_number] = {"name": name}
    print("Student registered successfully!")

def search_student():
    roll_number = input("Enter student's roll number: ")
    if roll_number in students:
        print("Student's name:", students[roll_number]["name"])
    else:
        print("Student not found!")

def update_student():
    roll_number = input("Enter student's roll number: ")
    if roll_number in students:
        name = input("Enter new name: ")
        students[roll_number]["name"] = name
        print("Student's information updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll_number = input("Enter student's roll number: ")
    if roll_number in students:
        del students[roll_number]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def mark_attendance():
    roll_number = input("Enter student's roll number: ")
    if roll_number in students:
        attendance = input("Enter attendance (P/A): ")
        students[roll_number]["attendance"] = attendance
        print("Attendance marked successfully!")
    else:
        print("Student not found!")

def mark_grade():
    roll_number = input("Enter student's roll number: ")
    if roll_number in students:
        grade = input("Enter grade: ")
        students[roll_number]["grade"] = grade
        print("Grade marked successfully!")
    else:
        print("Student not found!")

def main():
    while True:
        print("\nStudent Information Management System")
        print("1. Register Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Mark Attendance")
        print("6. Mark Grade")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            mark_attendance()
        elif choice == "6":
            mark_grade()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()