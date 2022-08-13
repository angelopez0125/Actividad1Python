import re

print("Ingrese un texto")
texto = input()

print('La Letra "S" se repite: ', len(re.findall('s', texto)))
