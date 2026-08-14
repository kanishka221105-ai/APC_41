# 27.	Store salaries of employees and determine:
# •	Highest salary 
# •	Lowest salary 
# •	Average salary 
# •	Employees earning above ₹50,000 
# •	Employees earning below ₹30,000 
salaries = [25000, 55000, 42000, 68000, 29000,
            75000, 33000, 52000, 27000, 61000]

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1

print("Salaries:", salaries)
print("Highest Salary: ₹", highest)
print("Lowest Salary: ₹", lowest)
print("Average Salary: ₹", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)