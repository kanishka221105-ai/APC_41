#Display the frequency of every character in a string. 
str=input("Enter a string:")
freq={}
for char in str:
    freq[char]=freq.get(char,0)+1
for char, count in freq.items():
    print({char},":",{count})
