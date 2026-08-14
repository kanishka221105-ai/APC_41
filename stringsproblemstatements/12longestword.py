#Find the longest word in a given sentence. 
sen=input("Enter a sentence:")
words=sen.split()
largest=len(words[0])
result=words[0]
for i in range(len(words)):
    if largest<len(words[i]):
        largest=len(words[i])
        result=words[i]
print(result)
    
