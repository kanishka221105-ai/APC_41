# 35.	Accept a paragraph and create a dictionary where:
# •	Key = word length 
# •	Value = number of words having that length.

paragraph=input("Enter a paragraph: ")
words=paragraph.split()
result={}
for word in words:
    length=len(word)
    result[length]=result.get(length,0)+1
print(result)