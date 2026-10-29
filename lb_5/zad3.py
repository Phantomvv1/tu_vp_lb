words = input("Enter words separated by a space: ").split()
k = int(input("Enter k: "))

result: list[str] = []

for word in words:
    if len(word) >= k:
        result.append(word)

resultTuple = tuple(result)

print("Резултат:", resultTuple)
