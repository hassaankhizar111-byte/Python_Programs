# Student Management System without OOP
students = []


def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    marks = int(input("Enter marks: "))
    gender = input("Enter gender: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade,
        "marks": marks,
        "gender": gender
    }

    students.append(student)
    print("✅ Student added successfully!")

def show_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"Name: {student["name"]}"
                f"Age: {student["age"]}"
                f"Grade: {student["grade"]}"
                f"Marks: {student["marks"]}"
                f"Gender: {student["gender"]}"
            )

def search_student():
    name = input("Enter name to search: ")
    found_students = (student for student in students if student["name"].lower() == name.lower())
    for student in found_students:
        print("Student found:")
        print(student)
        return
    print("Student not found.")

def update_student():
    name = input("Enter name to update: ")
    for student in students:
        if student["name"].lower() == name.lower():
            new_marks = int(input("Enter new marks: "))
            student["marks"] = new_marks
            print("✅ Student marks updated successfully!")
            return
    print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")
    for i, student in enumerate(students):
        if student["name"].lower() == name.lower():
            del students[i]
            print("✅ Student deleted successfully!")
            return
    print("Student not found.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()