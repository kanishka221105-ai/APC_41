s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
max_char = max(freq, key=freq.get)
print("Most Frequent Character:", max_char)
print("Frequency:", freq[max_char])