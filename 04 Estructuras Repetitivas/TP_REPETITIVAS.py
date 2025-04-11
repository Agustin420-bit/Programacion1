#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (100):#iteramos el numero desde 0 a 100 y luego mostramos por pantalla cada uno de sus valores 
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
contador=0
num=abs(int(input("ingrese un numero entero: ")))
while num!= 0:
   num= num // 10
   contador += 1
print(f"la cantidad de digitos es de digitos es {contador}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print("Ingresa 2 números y te daré la suma de los números que están entre esos números")

num1 = int(input("Ingresa el primer valor: ")) #ingresamos el primer valor y lo pasamos a numero
num2 = int(input("Ingresa el segundo valor: ")) #ingresamos el segundo valor y lo pasamos a numero

sumatoria = 0 #inicializamos la suma entre los numeros en 0

if num1 > num2: #En caso de que el primer numero sea mas grande que el segundo
    for i in range(num2 + 1, num1,1): #iteramos una variable desde el numero mas chico hacia el mas grande con paso 1 para ver los valores intermedios
        sumatoria += i # sumamos el numero que le sige al numero mas chico a la sumatoria total
else:
    for i in range(num1 + 1, num2,1): #En caso de que el segundo numero sea mas grande que el segundo
        sumatoria += i

print("La suma de los números entre", num1, "y", num2, "es:", sumatoria)
    
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

num=int(input("Ingrese numeros a sumar, si ingresa 0 le muestro la suma de los numeros ingresados: "))
sumatoria=0
while num!=0:
    sumatoria= sumatoria + num
    num= int(input("ingrese otro numero a suamr: "))
print(f"la sumatoria de los numeros ingresados es : {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_aletorio=random.randint(0,9)
intentos= 0
print("Adivina el numero aleatorio entre 0 y 9")
num_usuario= int(input("ingrese un numero: "))
while num_aletorio != num_usuario:
    intentos += 1
    num_usuario= int(input("icorrecto, ingrese otro numero: "))

print(f"el numero {num_usuario} ingresado es correcto, lo intentaste {intentos} veces")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100,0,-1):
    if i%2==0:
        print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num=int(input("ingrese un numero y te dare la sumatoria de numeros que hay entre 0 y ese numero: "))
sumatoria=0
for i in range (0,num,1):
    sumatoria= sumatoria + i
print(f"la sumatoria entre los numeros que estan entre 0 y {num} es : {sumatoria}")  

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

positivo=0
negativo=0
par=0
inpar=0
for i in range (0,100):
    nro= int(input("ingrese un numero: "))
    if nro>0:
        positivo +=1
    else:
        negativo +=1
    if nro%2==0:
        par +=1
    else:
        inpar +=1            


print(f"Tienes {positivo} numeros positivos,{negativo} negativos,{par} par,{inpar} impares")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma=0
nro=int(input("ingrese un numero: "))
for i in range (0,100):
    nro=int(input("ingrese otro numero: "))
    suma= suma+nro
media= suma//8
print(f"la media entre tus numeros es: {media}")  

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

nro_invertido=0
nro= int(input("ingrese un numero e inverire sus digitos: "))
while nro>0:
    digito= nro%10 #obtenemos el ultimo digito
    nro_invertido=nro_invertido*10+digito
    nro= nro//10 #quitamos el ultimo digito del numero
print(f"El numero invertido es : {nro_invertido}")
