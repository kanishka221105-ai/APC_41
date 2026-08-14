# 19.	Store names of students present in class.
# Display:
# •	Total students 
# •	Search a student's attendance 
# •	Add a new student 
# •	Remove an absent student 
students = ["Kanishka", "Manjiri", "Gauri", "Manasi"]

while True:
    print("\n1. Display Total Students")
    print("2. Search Student")
    print("3. Add New Student")
    print("4. Remove Absent Student")
    print("5. Display Student List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Total Students:", len(students))

    elif choice == 2:
        name = input("Enter student name to search: ").title()
        if name in students:
            print(name, "is present in class.")
        else:
            print(name, "is not present in class.")

    elif choice == 3:
        name = input("Enter new student name: ").title()
        students.append(name)
        print(name, "added successfully.")

    elif choice == 4:
        name = input("Enter absent student name: ")
        if name in students:
            students.remove(name)
            print(name, "removed successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Students Present:")
        for student in students:
            print(student)

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")