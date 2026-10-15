a = float(input("Въведете първото число: "))
b = float(input("Въведете второто число: "))

print("Изберете действие: +, -, *, /")
operation = input("Действие: ")

if operation == "+":
    print("Резултат:", a + b)
elif operation == "-":
    print("Резултат:", a - b)
elif operation == "*":
    print("Резултат:", a * b)
elif operation == "/":
    if b != 0:
        print("Резултат:", a / b)
    else:
        print("Грешка: деление на нула!")
else:
    print("Невалидно действие!")
