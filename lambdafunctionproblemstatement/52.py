# 52.	Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
# a)	Find the length of every word. 
# b)	Extract words having more than five characters. 
# c)	Sort words according to their length.
words=[]
n=int(input("Enter number of words: "))
for i in range(n):
    word=input("Enter word: ")
    words.append(word)
def word_lengths(data):
    return list(map(lambda x:len(x),data))
def long_words(data):
    return list(filter(lambda x:len(x)>5,data))
def sort_words(data):
    return sorted(data,key=lambda x:len(x))
print("\nLength of Each Word:")
print(word_lengths(words))
print("\nWords Having More Than 5 Characters:")
print(long_words(words))
print("\nWords Sorted By Length:")
print(sort_words(words))
