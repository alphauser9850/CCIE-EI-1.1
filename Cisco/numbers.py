# Program to count the frequency of each word in a string

from collections import Counter

# Read input string from user
input_str = input("Enter a string: ")



# Split the string into words
words = input_str.split()

# Count the frequency of each word
word_count = Counter(words)

# Print the frequency of each word
print("Frequency of each word in the string:")
for word, count in word_count.items():
    print(word, ":", count)
