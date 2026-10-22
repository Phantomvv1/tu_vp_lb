import random

n = int(input("Number of elements: "))

numbers: list[int] = []

for i in range(n):
    numbers.append(random.randint(1, 10))

print("Starting list: ", numbers)

result: list[int] = []

for i in range(len(numbers)):
    result.append(numbers[i])

    if i < len(numbers) - 1:
        result.append(numbers[i] + numbers[i + 1])

print("New list: ", result)
