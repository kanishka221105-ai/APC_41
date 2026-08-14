paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word Frequencies:")
for word, count in freq.items():
    print(word, ":", count)