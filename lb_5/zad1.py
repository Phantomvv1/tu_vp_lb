sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)
sorted_words = sorted(unique_words)

print("Number of unique words", len(unique_words))
print("Unique words: ", sorted_words)
