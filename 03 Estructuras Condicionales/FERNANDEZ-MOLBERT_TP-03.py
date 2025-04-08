"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""
#Se pide al usuario que ingrese su edad
"""edad = int(input("Ingrese su edad "))
#Se ingresa una estructura condicional para decidir si es o no mayor de edad
if edad >= 18 and edad < 110:
    print("Es mayor de edad")
elif edad < 18 and edad > 0:
    print("Es menor de edad")
else:
    print("Ingrese una edad adecuada")"""

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""
#Se pide al usuario que ingrese su nota.
"""nota = float(input("Ingrese su nota "))
#Se define la estructura condicional.
if nota >= 6 and nota <= 10:
    print("Aprobado")
elif nota < 6 and nota > 0:
    print("Desaprobado")
else: 
    print("Ingrese una nota válida.") """

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par"."""
#Se pide al usuario que ingrese un número par.
"""number = int(input("Ingrese un número par "))
#Se define la estructura condicional.
if number % 2 == 0:
    print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par")"""

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

#Se pide al usuario que ingrese su edad.
"""edad = int(input("Ingrese su edad "))
#Se define la estructura condicional para definir la categoría.
if edad < 12 and edad > 0:
    print("Es Niño/a")
elif edad >= 12 and edad < 18:
    print("Es Adolescente")
elif edad >= 18 and edad < 30: 
    print("Es Adulto/a Joven")
else:
    print("Es Adulto/a")"""

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"."""
#Se pide al usuario que cree una contraseña.
"""contrasena = input("Ingrese una contraseña entre 8 y 14")
#Se crea una estructura condicional para establecer si la contraseña es correcta.
if len(contrasena) >= 8 and len(contrasena) <= 14: 
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")"""

"""6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana +
y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Imprimir el resultado por pantalla."""
# Se importan las librerías necesarias.
"""import random
from statistics import mode, median, mean
# Se generan los números aleatorios
numeros_aleatorios = [random.randint(0,100) for i in range(50)]
# Definición de variables que van a guardan la moda, mediana y promedio.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#Se establece la estructura condicional para definir los sesgos.
if media > mediana and mediana > moda:
    print("Sesgo Positivo")
elif media < mediana and mediana < moda: 
    print("Sesgo Negativo")
else:
    print("Sin Sesgo")"""

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""
#Se pide al usuario que ingrese una frase o palabra
"""frase = input("Ingrese una frase o palabra ")
#Se accede a la última letra
ultima_letra = frase[-1].lower()
#Se crea la estructura condicional establecer que si finaliza en vocal se agregue un signo de exclamación.
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(frase)"""

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla."""
#Se pide al usuario que ingrese su nombre y una opción
"""nombre = input("Ingrese su nombre ")
opcion = int(input("Ingrese: 1. Si quiere su nombre en mayúscula, 2. Si quiere su nombre en minúscula, 3. Si quiere la primera letra en mayúscula "))

#Se crea la estructura condicional
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())
else:
    print("Opción Incorrecta. Vuelva a intentarlo.")"""

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""
#Se pide al usuario que ingrese la magnitud del terremoto.
"""magnitud = float(input("Ingrese la magnitud del terremoto, según la escala Richter. "))
#Se crea la estructura condicional para establecer la gravedad del terremoto.
if magnitud < 0:
    print("Ingrese un Valor Válido")
else: 
    if magnitud < 3:
        print("Muy leve (Imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas pero gralmente. no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles.)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")"""

"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año,
escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""
hemisferio = input("Ingrese en qué hemisferio se encuentra (N/S) ").lower()
mes = int(input("Ingrese el mes "))
dia = int (input("Ingrese el día "))

if hemisferio == "n":
    if mes == 12 and (dia >= 21 and dia <= 31) or mes == 1 and (dia >= 1 and dia <= 31) or mes == 2 and (dia >= 1 and dia <= 28) or mes == 3 and (dia >=1 and dia <= 21):
        print("Estación Invierno")
    elif mes == 3 and (dia >= 21 and dia <= 31) or mes == 4 and (dia >= 1 and dia <= 30) or mes == 5 and (dia >= 1 and dia <= 31) or mes == 6 and (dia >= 1 and dia <= 20):
        print("Estación Primavera")
    elif mes == 6 and (dia >= 21 and dia <= 31) or mes == 7 and (dia >= 1 and dia <= 31) or mes == 8 and (dia >= 1 and dia <= 31) or mes == 9 and (dia >= 1 and dia <= 20):
        print("Estación Verano")
    elif mes == 9 and (dia >= 21 and dia <= 30) or mes == 10 and (dia >= 1 and dia <= 31) or mes == 11 and (dia >= 1 and dia <= 30) or mes == 12 and (dia >= 1 and dia <= 20):
        print("Estación Otoño")
elif hemisferio == "s":
    if mes == 12 and (dia >= 21 and dia <= 31) or mes == 1 and (dia >= 1 and dia <= 31) or mes == 2 and (dia >= 1 and dia <= 28) or mes == 3 and (dia >=1 and dia <= 21):
        print("Estación Verano")
    elif mes == 3 and (dia >= 21 and dia <= 31) or mes == 4 and (dia >= 1 and dia <= 30) or mes == 5 and (dia >= 1 and dia <= 31) or mes == 6 and (dia >= 1 and dia <= 20):
        print("Estación Otoño")
    elif mes == 6 and (dia >= 21 and dia <= 31) or mes == 7 and (dia >= 1 and dia <= 31) or mes == 8 and (dia >= 1 and dia <= 31) or mes == 9 and (dia >= 1 and dia <= 20):
        print("Estación Invierno")
    elif mes == 9 and (dia >= 21 and dia <= 30) or mes == 10 and (dia >= 1 and dia <= 31) or mes == 11 and (dia >= 1 and dia <= 30) or mes == 12 and (dia >= 1 and dia <= 20):
        print("Estación Primavera")
