# 30.	Store patient names and ages using lists.
# Perform:
# •	Add a patient 
# •	Delete a patient 
# •	Search a patient 
# •	Display all patients 
# •	Count total patients
patients = ["Prachi", "Shriya", "Indumati", "Resha", "Meeshali"]
ages = [25, 30, 45]

while True:
    print("\n1. Add Patient")
    print("2. Delete Patient")
    print("3. Search Patient")
    print("4. Display All Patients")
    print("5. Count Total Patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ").title()
        age = int(input("Enter patient age: "))
        patients.append(name)
        ages.append(age)
        print("Patient added successfully.")

    elif choice == 2:
        name = input("Enter patient name to delete: ").title()
        if name in patients:
            index = patients.index(name)
            patients.pop(index)
            ages.pop(index)
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

    elif choice == 3:
        name = input("Enter patient name to search: ")
        if name in patients:
            index = patients.index(name)
            print("Patient Found")
            print("Name:", patients[index])
            print("Age:", ages[index])
        else:
            print("Patient not found.")

    elif choice == 4:
        print("\nPatient Records:")
        for i in range(len(patients)):
            print("Name:", patients[i], " Age:", ages[i])

    elif choice == 5:
        print("Total Patients:", len(patients))

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")