### TP3: CONDICIONALES ###
# Alumno: Hernán Gabriel Fernández Molbert

"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""
#Se crea la variable para que el usuario ingrese su edad
"""Edad_usuario = int(input("Por favor, ingrese su edad "))
#Se crea la estructura condicional
if Edad_usuario >= 18:
    print("ES MAYOR DE EDAD")"""

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""
#Se pide que se ingrese la nota al usuario
"""nota = int(input("Ingrese su nota "))
#Se asegura que la nota se ingrese bien
if nota < 0 or nota > 10:
    print("Las notas deben ser del 0 al 10")
else:
#Se crea la estructura condicional para determinar si esta o no aprobado
    if nota >= 6:
        print("APROBADO")
    else:
        print("DESAPROBADO")"""

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""
#Se pide al usuario que ingrese un numero
"""numero = int(input("Ingresá un número par "))
#Se define la condición y hace el cálculo para saber si el número es o no par.
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")"""

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""
#Se pide al usuario que ingrese su edad
"""edad = int(input("Ingresá tu edad "))
#Se crea la estructura condicional para determinar a qué categoria pertenece la persona.
if edad < 12: 
    print("NIÑO/A")
elif edad >= 12 and edad < 18:
    print("ADOLESCENTE")
elif edad >= 18 and edad < 30:
    print("ADULTO")
elif edad >= 30:
    print("ADULTO MAYOR")"""

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string."""
#Se pide al usuario que ingrese la contraseña
"""contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres")
#Se crea la condición que establece si la contraseña es correcta o no
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")"""

"""8) Escribir un programa que tome la lista numeros_aleatorios, 
calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""
#Se importan las bibliotecas necesarias (random y statics)
"""from statistics import mode, median, mean
import random
#Se generan los numeros aleatorios
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#Se crean las variables y se calculan la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#Se crea un condicional para establecer los sesgos
if media > mediana and mediana > moda:
    print("SESGO POSITIVO O A LA DERECHA")
elif media < mediana and mediana < moda:
    print("SESGO NEGATIVO O A LA IZQUIERDA")
elif media == mediana and mediana == moda:
    print("SIN SESGO")
else:
    print("No se puede inferir el sesgo")"""

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""
#Se pide al usuario una frase o palabra
"""frase = input("Ingresá una frase o palabra ")
#Se crea la condicion para determinar si la frase o palabra termina en vocal
if frase[-1] in ("aeiouAEIOU"):
    print(f"{frase}! ")
else:
    print(frase)"""

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
"""
#Se pide que ingrese su nombre al usuario
"""nombre = input("Ingresa tu nombre ")
#Se pide que ingrese la opción
opc = int(input("Ingresa si queres\n1. Tu nombre en Mayúscula\n2. En Minúscula\n3. Con la primera letra en mayúscula "))
#Se crea la estructura condicional con sus respectivas funciones (upper, lower y capitalize)
if opc == 1:
    print(nombre.upper())
elif opc == 2:
    print(nombre.lower())
elif opc == 3:
    print(nombre.capitalize())
else:
    print("Opción Inválida!")"""

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
#Se pide al usuario que ingrese el dato en float
"""magnitud = float(input("Ingrese la magnitud del terremoto "))
#Se crea la condicional para determinar y clasificar el terremoto
if magnitud < 3:
    print("Muy leve (imperteptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")"""

"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
#Se pide al usuario que ingrese en que hemisferio se encuentra
hemisferio = input("En qué hemisferio te encontrás (N: Norte, S: Sur) ")
dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
#Se crea la estructura condicional para determinar la estación del año de acuerdo a la inf aportada
if hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("VERANO")
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("OTOÑO")
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("INVIERNO")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("PRIMAVERA")
elif hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("INVIERNO")
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("PRIMAVERA")
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("VERANO")
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("OTOÑO")
