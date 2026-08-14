#Write a program to input a string and display its length without using the len() function.
str=input("Enter a string: ")
count=0
for i in str:
    count+=1
print("Length of string is: ",count)