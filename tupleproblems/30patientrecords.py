# 30.	Create a tuple containing patient records:
# •	Patient ID 
# •	Name 
# •	Age 
# •	Blood Group 
# Perform the following operations:
# •	Display all records 
# •	Search for a patient by ID 
# •	Count the total number of patients 
# •	Display patients with a specific blood group 
patients = (
    (111,"Meeshali",25,"O+"),
    (112,"Resha",30,"A+"),
    (113,"Manasi",28,"B+"),
    (114,"Vidya",35,"A+")
)
print("Patient Records:")
for p in patients:
    print(p)
search_id=int(input("\nEnter Patient ID to search: "))
found=False
for p in patients:
    if p[0]==search_id:
        print("\nPatient Found:")
        print("ID:",p[0])
        print("Name:",p[1])
        print("Age:",p[2])
        print("Blood Group:",p[3])
        found=True
        break
if not found:
    print("Patient not found.")
print("\nTotal Patients:",len(patients))
blood_group=input("\nEnter Blood Group to search: ")
print("\nPatients with Blood Group",blood_group)
for p in patients:
    if p[3]==blood_group:
        print(p)
