# Validate a password based on these conditions: 
# Minimum 8 characters 
# At least one uppercase letter 
# One lowercase letter 
# One digit 
# One special character
password = input("Enter Password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
if (len(password) >= 8 and
    has_upper and
    has_lower and
    has_digit and
    has_special):
    print("Valid Password")
else:
    print("Invalid Password")
    if len(password) < 8:
        print("- Password must be at least 8 characters long")
    if not has_upper:
        print("- Password must contain at least one uppercase letter")
    if not has_lower:
        print("- Password must contain at least one lowercase letter")
    if not has_digit:
        print("- Password must contain at least one digit")
    if not has_special:
        print("- Password must contain at least one special character")
            

