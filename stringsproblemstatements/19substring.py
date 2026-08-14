#Check whether a given substring exists in the main string.
main=input("Enter a string:")
sub=input("Enter a substring to check:")
if sub in main:
    print(sub,"is present in the main string.")
else:
    print(sub,"is not present in the main string.")