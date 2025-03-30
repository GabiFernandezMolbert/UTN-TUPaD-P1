#Alumno: Hernán Gabriel Fernández Molbert


#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.'''
nombre = input("Ingresa Tu Nombre: ")
print(f"Hola, {nombre}!")

'''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.'''
print ("Ingresá los Siguientes Datos: ")
nombre = input("Nombre ")
apellido = input("Apellido ")
edad = input("Edad ")
residencia = input("Lugar de Residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
radio = float(input("Ingresá el radio del círculo "))
pi = math.pi
area = round(pi * (radio**2),2)
perimetro = 2 * pi * radio
print(f"El area del círculo es {area} y su perimetro {perimetro}")

'''5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale'''
segundos = int(input("Ingrese la Cantidad de Segundos "))
horas = round(segundos / 3600, 1)
print(f"Cantidad de horas contenidas en {segundos} segundos: {horas} horas")

'''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.'''
#Sería + fácil realizarlo con un for pero supongo que lo hacemos así para que sepamos que las variables se pueden modificar
numero = int(input("Ingresá un Número"))
resultado = numero * 1
print(f"{numero} * 1 = {resultado}")
resultado = numero * 2
print(f"{numero} * 2 = {resultado}")
resultado = numero * 3
print(f"{numero} * 3 = {resultado}")
resultado = numero * 4
print(f"{numero} * 4 = {resultado}")
resultado = numero * 5
print(f"{numero} * 5 = {resultado}")
resultado = numero * 6
print(f"{numero} * 6 = {resultado}")
resultado = numero * 7
print(f"{numero} * 7 = {resultado}")
resultado = numero * 8
print(f"{numero} * 8 = {resultado}")
resultado = numero * 9
print(f"{numero} * 9 = {resultado}")
resultado = numero * 10
print(f"{numero} * 10 = {resultado}")

'''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
'''
primer_numero = int(input("Ingresá el Primer Número "))
segundo_numero = int(input("Ingresá el Segundo Número (No puede ser cero) "))

resultado = primer_numero + segundo_numero
print(f"{primer_numero} + {segundo_numero} = {resultado}")

resultado = primer_numero - segundo_numero
print(f"{primer_numero} - {segundo_numero} = {resultado}")

resultado = primer_numero * segundo_numero
print(f"{primer_numero} * {segundo_numero} = {resultado}")

resultado = primer_numero / segundo_numero
print(f"{primer_numero} / {segundo_numero} = {resultado}")

'''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. '''
print("Ingresá los Siguientes Datos: ")
peso = float(input("Peso en Kg.: "))
altura = float(input("Altura en metros: "))

imc = peso / altura**2
print(f"Tu IMC es de: {imc}")

'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit.'''

grados_celsius = float(input("Ingresá los grados Celsius para reailzar la conversión. "))

grados_fahrenheit = 9/5 * grados_celsius + 32 

print(f"{grados_celsius} Celsius equivalen a {grados_fahrenheit} Fahrenheit")

'''10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.'''
primer_numero = int(input("Ingresá el primer número "))
segundo_numero = int(input("Ingresá el segundo número "))
tercer_numero = int(input("Ingresá el tercer número "))
promedio = (primer_numero + segundo_numero + tercer_numero) / 3 
print(f"El promedio de los números ingresados es: {promedio}")