# 26.	Store marks of 20 students in a list and determine:
# •	Highest marks 
# •	Lowest marks 
# •	Average marks 
# •	Number of students scoring above average 
# •	Number of students scoring below average
marks = [78, 65, 90, 45, 88, 72, 67, 95, 81, 76,
         69, 54, 87, 73, 62, 80, 91, 58, 70, 84]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_avg = 0
below_avg = 0

for mark in marks:
    if mark > average:
        above_avg += 1
    elif mark < average:
        below_avg += 1

print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Scoring Above Average:", above_avg)
print("Students Scoring Below Average:", below_avg)