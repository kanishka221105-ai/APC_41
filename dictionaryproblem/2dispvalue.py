#2.	Create a dictionary containing employee information and display the value associated with a specified key.
employee = {"id":101,"name":"Kanishka","age":21,"department":"CSE","salary":50000}
print("Employee Information:")
print(employee)
key = input("Enter the key to search:").lower()
if key in employee:
    print(key,":", employee[key])
else:
    print("Key not found")