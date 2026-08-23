#30.	Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students={"Amit":"CSE","Rahul":"IT","Sneha":"CSE","Priya":"ENTC","Rohit":"IT"}
departments={}
for name,department in students.items():
    if department not in departments:
        departments[department]=[]
    departments[department].append(name)
print(departments)