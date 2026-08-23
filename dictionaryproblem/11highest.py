#11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students={"Gautmi":75,"Mrunal":88,"Kanishka":95,"Alisha":82}
student=max(students,key=students.get)
print("Student with highest marks:",student)
print("Highest marks:",students[student])