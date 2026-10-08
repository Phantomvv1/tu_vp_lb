import math

r = float(input("Въведете радиуса r: "))

area = math.pi * r**2
perimeter = 2 * math.pi * r

print(f"Лице: {area:.3f}")
print(f"Периметър: {perimeter:.3f}")
