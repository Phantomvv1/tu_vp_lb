text = input("Text: ")

dictionary: dict[str, int] = {}

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

print(dictionary)
