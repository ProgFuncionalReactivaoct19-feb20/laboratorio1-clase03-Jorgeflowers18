"""
    Problema 4
    author: @Jorgeflowers18
"""

# lista de tuplas a ser discriminadas
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), 
        (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

# lista vacia para ser llenadas de tuplas que cumplan con los
# requisitos
ans = []

#estructura para iterar las tuplas
for i in notas:

    # estructuras que seleccionan las tuplas requeridas y las 
    # adjuntan a la lista vacia ans
    if i[3] == "Regular":
        ans.append(i)

    
    if i[3] == "Bueno":
        ans.append(i)    

# impresión de la lista ya llenada
print(ans) 