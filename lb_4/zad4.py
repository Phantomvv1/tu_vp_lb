n = int(input("Number: "))

numbers = list(range(1, n + 1))
reversed_numbers = numbers[::-1]

dictionary: dict[int, int] = {}

for i in range(n):
    dictionary[numbers[i]] = reversed_numbers[i]

print("List: ", numbers)
print("Dictionary: ", dictionary)
