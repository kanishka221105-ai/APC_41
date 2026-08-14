# 28.	Store scores of a batsman in 10 matches and calculate:
# •	Highest score 
# •	Lowest score 
# •	Total runs 
# •	Average runs 
# •	Number of centuries (≥100) 
# •	Number of half-centuries (50–99)
scores = [45, 120, 78, 102, 56, 34, 150, 89, 67, 110]

highest = max(scores)
lowest = min(scores)
total_runs = sum(scores)
average_runs = total_runs / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50 and score <= 99:
        half_centuries += 1

print("Scores:", scores)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total_runs)
print("Average Runs:", average_runs)
print("Number of Centuries:", centuries)
print("Number of Half-Centuries:", half_centuries)