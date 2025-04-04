#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad=int(input("Ingrese su edad: "))
if edad>18:
    print("Es mayor de edad")
else:
    pass

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

Nota= int(input("Ingrese su nota: "))
if Nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

nro= int(input("Ingrese un numero par: "))
if nro%2==0:
    print("ha ingresado un numero par")
else:
    print("Por favor,ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad: "))
categoria= "nada"
if edad<12:
    categoria= "Niño/a"
elif edad>=12 and edad<18:
    categoria= "Adolescente"
elif edad>=18 and edad<30:
    categoria= "Adulto/a joven"
elif edad>=30:
    categoria="Adulto/a"
print(f"Su categoria es {categoria}")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python

Contraseña= input("introduzca una contraseña de entre 8 y 14 caracteres: ")
nrocaracteres= len(Contraseña)
if nrocaracteres>=8 and nrocaracteres<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana =median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
sesgo = "nada"
if media>mediana and mediana>moda:
    sesgo= "Positivo"
elif media<mediana and mediana<moda:
    sesgo= "Negativo"
else:
    sesgo="Sin sesgo" 
print(f"El sesgo es: {sesgo}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro

nombre= input("Ingrese su nombre: ")
print ("1"" si quiere su nombre todo en mayusculas")
print ("2"" si quiere su nombre en minisculas")
print ("3"" si quiere su nombre con la primer letra en mayusculas")
opcion= str(input("Ingrese la opcion deseada: "))
if opcion == "1":
    nombre = nombre.upper()
elif opcion == "2":
    nombre = nombre.lower()
elif opcion == "3":
    nombre = nombre.title()
print (nombre)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).

#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

mTerremoto = float(input("ingrese la magnitud del terremoto: "))
terremoto="."
if mTerremoto<3:
    terremoto= "Muy leve (imperceptible)"
elif mTerremoto>=3 and mTerremoto<4:
    terremoto= "leve (ligeramente perceptible)"
elif mTerremoto>=4 and mTerremoto<5:
    terremoto= "Moderado (sentido por personas, pero generalmente no causa daños)."
elif mTerremoto>=5 and mTerremoto<6:
    terremoto= "Fuerte (puede causar daños en estructuras débiles)."
elif mTerremoto>=6 and mTerremoto<7:
    terremoto= "Muy Fuerte (puede causar daños significativos)."
elif mTerremoto>=7:
    terremoto= "Extremo (puede causar graves daños a gran escala)."
print (terremoto)

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertir mes y día a un número único para simplificar la comparación
fecha = mes * 100 + dia

# Determinar estación según hemisferio
if hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha no válida"
elif hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha no válida"
else:
    estacion = "Hemisferio no válido"

# Mostrar resultado
print(f"La estación del año es: {estacion}")



