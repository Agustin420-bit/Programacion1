#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.

list= list(range(4,101,4))  #creamos una lista desde el 4 hasta el 100 con paso 4
print(list)  #imprimimos la lista

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

lista= [1,2,3,4,5]  #creamos la lista
print(lista[3])     #Imprimimos en pantalla el penultimo valor que se encuentra en la posicion "3"

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo: lista_vacia = []

lista=[]    #creamos una lista vacia
lista.append([1,2,3])   #agregamos 3 elementos
print(lista)  #imprimimos la lista

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]  #creamos la lista con sus elementos
animales[1]= "loro"   #Reemplazamos el elemento gato por loro
animales[3]= "oso"    #Reemplazamos el elementos pez por oso
print(animales)       #Imprimimos la lista

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#1)Calcula el máximo valor de la lista numeros usando max(numeros).
#2)Elimina ese valor máximo de la lista usando remove().

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

lista= list(range(10,31,5))   #Creamos una lista de numeros del 10 al 30 con saltos de 5 en 5 
print(lista[0:2])    #Imprimimos los 2 primeros valores

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

autos[1]= "kangoo"   #Cambiamos el elemento polo por kangoo
autos[2]= "fiat uno" #Cambiamos el elemento suran por fiat uno

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

dobles=[]   #Creamos la lista vacia 
dobles.append(2*5) #Agregamos el doble de 5 a la lista
dobles.append(2*10) #Agregamos el doble de 10 a la lista
dobles.append(2*15) #Agregamos el doble de 15 a la lista
print(dobles) #Imprimimos la lista

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")  #agregamos jugo a la tercer lista
compras[1][1]= "Tallarines" #Reemplazamos fideos por tallarines
compras[0].remove("pan") #Eliminamos pan de la primer lista
print (compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada = [15,True,[25.5, 57.9, 30.6],False]                    
print(lista_anidada)