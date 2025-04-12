"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
#Se crea un For desde 0 hasta 101. 
for i in range (101):
   print(i) 

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
#Se Solicita al usuario que ingrese un número entero.
#Se crea la variable contador y se iguala a 0
numero = input("Ingrese un número entero ")
contador = 0
#Se establece un "for" que itere hasta la cantidad de dígitos que tiene el número ingresado.
#Con cada iteración se suma uno a la variable contador
for i in range(len(numero)):
    contador += 1
#Se imprime el contador que indica la cantidad de veces que iteró el bucle y, a su vez, la cantidad de dígitos que tiene el número.
print(f"La cantidad de dígitos que contiene el número ingresado es: {contador}")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
#Se Pide al usuario que ingrese dos números y se crea una variable acumulador que se iguala a 0.
numero_uno = int(input("Ingrese el primer número (recuerde que debe ser menor al segundo.)"))
numero_dos = int(input("Ingrese el segundo número"))
acumulador = 0
#Se crea un if para evitar que se ingrese un numero mayor en el inicio
if numero_uno > numero_dos:
    print("Error. Por favor, reinicie el programa.")
else:
    #Se crea un for para que el acumulador sume los números comprendidos entre los proporcionados por el usuario
    for i in range(numero_uno + 1, numero_dos):
        acumulador = acumulador + i
#Se imprime el acumulador que, a su vez, es la suma de todos los números comprendidos entre los que se ingresaron
print(acumulador)

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
#Se crea una variable que sirva para deterner el ciclo y un acumulador que vaya guardando las sumas.
CONTROL = 0
acumulador = 0
num_uno = int(input("Ingrese un número o 0 para finalizar el programa "))
#Se crea un ciclo repetitivo que permita sumar los número ingresados por el usuario
while num_uno != CONTROL:
    acumulador += num_uno
    num_uno = int(input("Ingrese otro número para sumar "))
#Se imprime el resultado de la suma guardado en la variable "acumulador".
print(f"El resultado de la suma es: {acumulador}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
#Se importa la librería random
import random
#Se crea un número aleatorio y se crea una variable para contar los intentos
numero_aleatorio = random.randint(0,9)
intentos = 1
numero = int(input("Ingresa un número del 0 al 9 y adiviná el número "))
#Se crea un while para que repita el código hasta que el usuario adivine el número. Además se agregan mjs.
while numero != numero_aleatorio:
    intentos += 1
    numero = int(input("Intentalo de nuevo... "))
    if intentos == 3:
        print("Mmm... se esta poniendo dificil esto, no?")
    elif intentos == 4:
        print("Uy, que dificil!!!")
    elif intentos == 5:
        print("Creo que sos bastante malo en esto...")
    elif intentos == 6:
        print("Daleeeeeee, por favor!")
    elif intentos == 7:
        print("Me estas poniendo nervioso")
    elif intentos == 8:
        print("Cri cri cri cri")
    elif intentos == 9:
        print("Esto se llama tener mala suerte")
    elif intentos == 10:
        print("La probabilidad riéndose de vos: :)")

print(f"Felicitaciones!!! Adivinaste. EL número era {numero_aleatorio} y lo adivinaste en {intentos} intentos")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
#Se crea un for que vaya desde 100 hasta 0 decreciendo de a 2. También se podría hacer con if i % == 0: print(i) pero supondría más código
for i in range(100,0,-2):
        print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
#Se pide al usuario que ingrese un número y se crea la variable acumulador iniciada en 0.
numero = int(input("Ingresa un número entero "))
acumulador = 0
#Se crea el for que vaya desde 1 hasta el número ingresado por el usuario (+1 para que incluya también el número ingresado)
for i in range(1, numero+1):
    acumulador = i + acumulador
#Se imprime el resultado
print(f"El resultado de la suma de todos los números comprendidos entre {numero} y 0 es: {acumulador}")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
#Se crean las variables contadoras y una constante para poder probar el programa cambiando solo un numero
CANTIDAD_NUMEROS = 100
numero_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0
#Se crea el for para que el usuario ingrese los números y contar los positivos, negativos, pares e impares.
for i in range(1,CANTIDAD_NUMEROS+1):
    numero = int(input(f"Ingresa el numero {i}" ))
    if numero < 0:
        numeros_negativos += 1
    else:
        numeros_positivos += 1
    if numero % 2 == 0:
        numero_pares += 1
    else:
        numeros_impares += 1
#Se imprime los resultados.
print(f"CANTIDAD NUMEROS POSITIVOS: {numeros_positivos}")
print(f"CANTIDAD NUMEROS NEGATIVOS: {numeros_negativos}")
print(f"CANTIDAD NUMEROS PARES: {numero_pares}")
print(f"CANTIDAD NUMEROS IMPARES: {numeros_impares}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""
#Se ingresa una constante para poder cambiar solo ese valor y probar el programa y la variable suma para acumular la suma de los números ingresados.
CANTIDAD_NUMEROS = 100
suma = 0
#Se crea el for para que el usuario ingrese los números y se sumen
for i in range(1,CANTIDAD_NUMEROS+1):
    numero = int(input(f"Ingrese el numero {i }" ))
    suma = numero + suma
#Se imprime el promedio.
print(f"El promedio de los números ingresados es: {suma/CANTIDAD_NUMEROS}")

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""
#Se pide al usuario que ingrese un número y se crea una variable String vacía.
numero = input("Ingresa un número ")
numero_invertido =""
#Se crea un for que vaya desde la cantidad de caracteres de numero hasta -1 y vaya guardando el numero al reves.
for i in range(len(numero)-1,-1,-1):
    numero_invertido = numero_invertido + numero[i]
    print(numero_invertido)



