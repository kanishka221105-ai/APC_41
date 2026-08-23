#12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.
students={"Amit":75,"Rahul":88,"Sneha":95,"Priya":62}
student=min(students,key=students.get)
print("Student with lowest marks:",student)
print("Lowest marks:",students[student])