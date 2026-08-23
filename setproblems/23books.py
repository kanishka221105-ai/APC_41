#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
day1={101,102,103,104,105}
day2={104,105,106,107,108}
print("Unique visitors:",day1|day2)
print("Returning visitors:",day1&day2)
print("Visitors only on first day:",day1-day2)
print("Visitors only on second day:",day2-day1)