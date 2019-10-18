"""
    Prblema 3
    author: @Jorgeflowers18
"""
# frase a discriminar
st = "No hay medicina que cure lo que no cura la felicidad"

# funcion donde se recibe informacion x
def words (x):

# estructura para separar las palabras que tengan un tamaño menor 
# o igual a 3 
    if len(x) <= 3:
        return True
    else:
        return False

# presentación del proceso con filter para seleccionar solo las \
# palabras que obtengan True en la discriminación y List \
# para hacer la info visible al ojo humano
print(list(filter(words, st.split(" "))))