#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
city=["Kolhapur","Nagpur","Mapusa","Anjuna","Mumbai","Latur","Solapur","Pandharpur"]
target=input("Enter a city:").title()
nf=0
for i in range(0,len(city)):
    if city[i]==target:
        nf=1
        print("City is present in the list!")
        break
if nf==0:
    print("City not found!")  

