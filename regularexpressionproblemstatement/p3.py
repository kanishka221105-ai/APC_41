#3.	Write a program to count the occurrences of vowels in a given string using regular expressions.
import re
text = input("Enter a string: ")
vowels = re.findall(r"[aeiouAEIOU]", text)
print(len(vowels))