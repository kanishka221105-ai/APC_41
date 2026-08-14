s=input("Enter a string: ")
compressed=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        compressed+=s[i]+str(count)
        count=1
compressed+=s[-1]+str(count)
if len(compressed) < len(s):
    print("Compressed String:", compressed)
else:
    print("Original String:", s)