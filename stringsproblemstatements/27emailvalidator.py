email = input("Enter email: ")
if ("@" in email and
    "." in email and
    email.index("@") > 0 and
    email.rindex(".") > email.index("@") + 1):
    print("Valid Email")
else:
    print("Invalid Email")