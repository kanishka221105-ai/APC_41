# Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
import numpy as np
marks = np.array([65, 70, 82, 90, 55, 48, 77, 88, 92, 60, 74, 81, 85, 58, 79, 91, 68, 72, 84, 76])
avg = marks.mean()
print("Class Average:", avg)
print("Marks above average:", marks[marks > avg])