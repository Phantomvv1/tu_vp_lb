a = int(input("Въведете долната граница: "))
b = int(input("Въведете горната граница: "))

count = 0

for _ in range(a, b):
    if count >= 10:
        break

    count += 1

print("Броят на числата в интервала е:", count)
