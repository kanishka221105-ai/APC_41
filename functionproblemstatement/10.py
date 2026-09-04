#10.	Define a function that accepts a string and returns the number of vowels present in it.
def vow(str):
    count=0
    for i in str:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
    return count
str=input("Enter a string:").lower()
print("Number of vowels:",vow(str))