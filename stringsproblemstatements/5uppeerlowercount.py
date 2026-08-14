#Count the number of uppercase and lowercase letters in a string. 
str=input("Enter a string:")
upper=0
lower=0
for ch in str:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("No. of uppercase:",upper)
print("No. of lowercase:",lower)