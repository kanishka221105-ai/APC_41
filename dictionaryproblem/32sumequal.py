#32.	Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
numbers=[2,7,11,15]
target=9
seen={}
for number in numbers:
    required=target-number
    if required in seen:
        print("Numbers:",required,number)
        break
    seen[number]=True