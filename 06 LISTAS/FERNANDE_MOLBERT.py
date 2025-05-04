### TRABAJO PRACTICO LISTAS ###
# Alumno: HERNAN GABRIEL FERNANDEZ MOLBERT

"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
"""
#Creación de lista
lista = list(range(4,101,4))
print(lista)

"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!"""
#Se crea una lista con colores
lista = ["Rojo", "Verde", "Amarillo", "Azul", "Gris"]
#Se imprime el penúltimo elemento con la posición del índice e indexing con nums negativo
print(lista[3])
print(lista[-2])

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior"""
#Se crea una lista vacia
canciones = []
#Se agregan elementos a la lista
canciones.append("Georgia on my mind")
canciones.append("Help!")
canciones.append("The dock of the bay")
#Se imprime la lista actualizada
print(canciones)

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!"""

animales = ["perro", "gato", "conejo", "pez"]
#Se modifican el segundo y último valor de la lista
animales[1] = "loro"
animales[-1] = "Oso"
#Se imprime la lista "animales" modificada
print(animales)

"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
"""Se define la lista con los números: 3, 15, 3, 22 y 7. Luego se pide que de esa lista se elimine el
número más grande. Por último, se imprime la lista "numeros" sin ese número eliminado (22)."""

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""
#Se crea una lista con números que vayan del 10 al 30 con paso 5
lista = list(range(10, 31, 5))
#Se imprimen los primeros dos elementos.
print(lista[0], lista[1])

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
"""
autos = ["sedan", "polo", "suran", "gol"]
#Se modifican los valores centrales de la lista (1 y 2)
autos [1] = "Xaris"
autos[2] = "Stepway"
#Se imprime la lista actualizada
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
"""
#Se crea la lista vacia
dobles = []
#Se agregan los dobles de 5, 10 y 15 a la lista con append 
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
#Se imprime la lista actualizada
print(dobles)

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#Se agrega jugo a la lista del 3er cliente
compras[2].append("jugo")
#Se reemplaza fideos por tallarines de la lista del 2do cliente
compras[1][1] = "Tallarines"
#Se elimina pan de la lista del 1er cliente
compras[0].remove("pan")
#Se imprime la lista resultante
print(compras)

"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""
#Se agregan los elementos de acuerdo al indice indicado en la consigna
lista_anidada = [15, True, [25.5,57.9,30.6],False]
#Se imprime la lista anidada
print(lista_anidada)
