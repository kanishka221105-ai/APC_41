s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_freq) >= 2:
    print("Second Most Frequent Character:", sorted_freq[1][0])
    print("Frequency:", sorted_freq[1][1])
else:
    print("No second most frequent character found.")