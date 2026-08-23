# 19.	Create two sets:
# •	Students present in the morning session 
# •	Students present in the afternoon session 
# Find:
# •	Students present in both sessions 
# •	Students present only in the morning 
# •	Students present only in the afternoon 
# •	Students present in at least one session

morning={"Amit","Rahul","Sneha","Priya","Neha"}
afternoon={"Sneha","Priya","Rohit","Kiran","Amit"}
print("Present in both sessions:",morning&afternoon)
print("Only in morning:",morning-afternoon)
print("Only in afternoon:",afternoon-morning)
print("Present in at least one session:",morning|afternoon)