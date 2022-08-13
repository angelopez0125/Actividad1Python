import math

print("Ingrese el primer cateto")
cateto1 = float(input())
print("Ingrese el segundo cateto")
cateto2 = float(input())
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print("La Hipotenusa es: " , hipotenusa)
