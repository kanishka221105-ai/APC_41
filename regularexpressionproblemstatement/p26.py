#26.	Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.
import re
ref = input("Enter research reference text: ")
dois = re.findall(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", ref)
years = re.findall(r"\b(19|20)\d{2}\b", ref)
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", ref)
urls = re.findall(r"https?://[^\s<>\"']+", ref)
print("DOIs:", dois)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)