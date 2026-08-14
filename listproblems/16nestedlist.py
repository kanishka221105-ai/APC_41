#16.	Create a nested list storing:
# •	Student Name 
# •	Roll Number 
# •	Marks 
# Display all student details.
students=[]
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    roll=int(input("Enter roll number: "))
    marks=float(input("Enter marks: "))
    students.append([name,roll,marks])
print("\nStudent Details:")
for nlist in students:
    print("Name:",nlist[0])
    print("Roll Number:",nlist[1])
    print("Marks:",nlist[2])
    print()