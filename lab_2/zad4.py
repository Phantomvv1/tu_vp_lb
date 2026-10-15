n = int(input("Въведете число: "))

if n < 2:
    print("Числото не е просто")
else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Числото е просто")
    else:
        print("Числото не е просто")
