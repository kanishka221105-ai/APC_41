#Find the shortest word in a sentence. 
sen=input("Enter a sentence:")
words=sen.split()
shortest=len(words[0])
result=words[0]
for i in range(len(words)):
    if shortest>len(words[i]):
        shortestest=len(words[i])
        result=words[i]
print(result)