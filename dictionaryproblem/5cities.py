#5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities={"Kolhapur":20000000,"Pune":7000000,"Mapusa":2000000,"Sangli":600000}
city=input("Enter city to remove: ")
cities.pop(city)
print(cities)