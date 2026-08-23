#4.	Create a dictionary containing student marks. Update the marks of a specified student.
marks = {"Kanishka":85,"Gauri":90,"Prachi":78,"Manasi": 88,"Manjiri":56}
print("Student Marks:")
print(marks)
name = input("Enter student name to update marks: ").title()
if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print("\nUpdated Dictionary:")
    print(marks)
else:
    print("Student not found")