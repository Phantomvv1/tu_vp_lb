numbers = [1, 2, 2, 3, 1, 4, 2]

new_list: list[int] = []

for x in numbers:
    if x not in new_list:
        new_list.append(x)

print("Original list: ", numbers)
print("List without duplicates: ", new_list)
