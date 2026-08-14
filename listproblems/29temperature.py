# 29.	Store the temperature of 30 days and determine:
# •	Hottest day 
# •	Coldest day 
# •	Average temperature 
# •	Days above average temperature 
# •	Days below average temperature
temperatures = [30, 32, 31, 29, 35, 36, 34, 33, 30, 31,
                32, 37, 38, 36, 35, 34, 33, 32, 31, 30,
                29, 28, 27, 30, 32, 34, 35, 36, 37, 38]

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above_avg = 0
below_avg = 0

for temp in temperatures:
    if temp > average:
        above_avg += 1
    elif temp < average:
        below_avg += 1

print("Temperatures:", temperatures)
print("Hottest Day Temperature:", hottest)
print("Coldest Day Temperature:", coldest)
print("Average Temperature:", average)
print("Days Above Average Temperature:", above_avg)
print("Days Below Average Temperature:", below_avg)