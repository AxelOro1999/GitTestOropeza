import math

l1 = float(input("Ingresa el lado 1 del triangulo: "))
l2 = float(input("Ingresa el lado 2 del triangulo: "))
l3 = float(input("Ingresa el lado 3 del triangulo: "))

s = (l1+l2+l3)/2

area = math.sqrt(s*(s-l1)*(s-l2)*(s-l3))

print(area)
