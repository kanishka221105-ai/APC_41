#4.	Write a program to extract all uppercase letters from a given string. 
import re
text = "Welcome to Python Programming."
text = input("Enter a string: ")
upper_letters = re.findall(r"[A-Z]", text)
print(upper_letters)