#22.	Create two sets representing technical skills of two employees. Find:
# •	Common skills 
# •	Skills unique to Employee 1 
# •	Skills unique to Employee 2 
# •	All available skills

available_books={"Python Basics","Data Science","Machine Learning","Java Programming"}
requested_books={"Python Basics","Machine Learning","C++ Programming"}
print("Requested books available:",available_books&requested_books)