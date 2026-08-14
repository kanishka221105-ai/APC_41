#21.	Accept two lists and merge them into a single list.
list1 = []
list2 = []

n1 = int(input("Enter number of elements in List 1: "))
for i in range(n1):
    item = input("Enter element: ")
    list1.append(item)

n2 = int(input("Enter number of elements in List 2: "))
for i in range(n2):
    item = input("Enter element: ")
    list2.append(item)

merged_list = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)