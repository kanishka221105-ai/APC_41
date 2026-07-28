#print the performance of the student based on the percentage 
# percentage>=90 -> Excellent Performance
# percentage>=80 -> Very Good Performance
# percentage>=70 -> Good Performance
# percentage>=60 -> Average Performance
# else -> Poor Performance
per=float(input("Enter your percentage(out of 100):"))
if(per>=90):
    print("Excellent Performance.")
elif(per>=80):
    print("Very Good Performace.")
elif(per>=70):
    print("Good Performace.")
elif(per>=60):
    print("Average Performace.")
else:
    print("Poor Performace.")