#respuestas 
#1:
#contador de 1 a 100
for i in range(0, 101):
 print(i)
#2:
#contador de digitos 
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len (str ( numero ))
print("la cantidad de digitos es de ", cantidad_digitos) 
#3:
#contador de numeros
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero : "))
suma = 0
for i in range( a + 1, b):
 suma += i
 print("La suma de los números entre", a, "y", b, "es:", suma)
4#
suma = 0 
while True:
    numero = int ( input("Ingrese un número (o '0' para terminar): "))
    if numero == 0:
        break
    suma = numero + suma
print("La suma es:", suma)
5#
#adivinar numero 
int(input("Ingrese un número entre 0 y 9: "))
import random
numero_aleatorio = random.randint(0, 9)
while True:
    numero_usuario = int(input("Adivine el número (entre 0 y 9): "))
    if numero_usuario == numero_aleatorio:
        print("¡Felicidades! Has adivinado el número.")
        break
    else:
        print("Número incorrecto. Inténtalo de nuevo.")
#6#
# 0 a 100 pares decreciente
for i in range(100, -1, -2):
    print(i)            
#7
numero_final = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, numero_final + 1):
    suma += i   
print("La suma de los números desde 1 hasta", numero_final, "es:", suma)    
#8 pares, impares, positivos y negativos
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(100):
    numero = int(input( "ingrese un numero entero (hasta 100) para saber si es par, impar, positivo o negativo:" ))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("Cantidad de números pares:", pares)      
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
#9 suma y media de 100 numeros
suma = 0    
for i in range(100):
    numero =  int(input("Ingrese un número entero (hasta 100): "))
    suma += numero
media = suma / 100
print("La media de los números ingresados es:", media)
#10
numero = int(input("Ingrese un número entero: "))
numero_invertido = 0        
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print("El número invertido es:", numero_invertido)
