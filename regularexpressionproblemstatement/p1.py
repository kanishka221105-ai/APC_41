#1.	Write a Python program using regular expressions to extract all digits from a given string.
import re
text = "The order 450 and 15%"
print(re.findall(r"\d", text))
print(re.findall(r"\d+", text)) 