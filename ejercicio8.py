import re

print("Ingrese un texto")
texto = input()

print('El texto tiene: ',re.findall('[aeiouáéíóíúü]', texto, re.IGNORECASE))
