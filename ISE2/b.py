#Write a program to handle divisionby zero using try excpect
def division(n,d):
    try:
        result=n/d
        return result
    except ZeroDivisionError:
        return "Error: Can't divide by zero!"   
print(division(42,2))  
print(division(6,0))  
