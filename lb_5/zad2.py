text = input("Text: ")

symbols: dict[str, int] = {}

for char in text:
    if char != " ":
        if char in symbols:
            symbols[char] += 1
        else:
            symbols[char] = 1

if symbols:
    most_common: str = max(symbols, key=lambda char: symbols[char])
    print("Most frequent char:", most_common)
    print("Number of occurrences:", symbols[most_common])
else:
    print("There aren't any symbols to count")
