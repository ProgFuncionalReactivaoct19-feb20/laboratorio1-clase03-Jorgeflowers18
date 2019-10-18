"""
    Problema 3
    author: @Jorgeflowers18
"""
# datos a procesar
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

# funcion anónima para sumar los enteros dentro de las tuplas
f = (lambda x: x[0] + x[1] + x[2])

# presentación de la información
print(list(map(f, notas)))

