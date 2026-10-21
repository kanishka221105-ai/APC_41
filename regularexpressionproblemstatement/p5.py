#5.	Write a program to identify all spaces, tabs, and newline characters in a text.
import re
text = input("Enter text with spaces, tabs, or newlines: ")
matches = [m.group() for m in re.finditer(r"[\s]", text)]
print(matches)