#2.	Accept a sentence and display all words beginning with the letter A or a.
import re
sentence = input("Enter a sentence: ")
words = re.findall(r"\b[Aa]\w*", sentence)
print(words)