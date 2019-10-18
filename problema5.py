"""
    Problema 5
    author : @Jorgeflowers18
"""
# lista a discriminar
edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

def comparacion (x): 
    # lista de valores no permitidos
    black_edades = [10, 14, 30, 32, 40, 16]
    # discriminación
    if x in black_edades:
        return False
    else:
        return True
# presentacion filtrado y listado  de valores discriminados
print(list(filter(comparacion, edades)))