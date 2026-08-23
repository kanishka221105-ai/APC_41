#6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees={101:"Gauri",102:"Manasi",103:"Manjiri",104:"Kanishka"}
id=int(input("Enter employee ID: "))
if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")