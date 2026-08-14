#11.	Create a list of 10 numbers and display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Middle 4 elements 
# •	Alternate elements 
# •	Reverse list using slicing
num=[1,2,5,3,9,6,23,54,76,98]
print("First 5 elements:",num[:5])
print("Last 5 elements",num[5:])
print("Middle 4 elements:",num[3:7])
print("Alternate elements:",num[::2])
print("Reverse list using slicing",num[::-1])