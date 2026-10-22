n = input("Number: ")

numbers = list(n)
numbers.sort()

tuple1 = tuple(numbers)
tuple2 = tuple1[::-1]

print("Numbers in ascending order:", tuple1)
print("Numbers in descending order:", tuple2)
