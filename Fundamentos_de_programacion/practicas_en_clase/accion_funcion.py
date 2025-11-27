import funcion1 as f
import random as rd

#Generar una lista de 30 numeros aleatorios entre 6 y 340
lista_numeros = []
for i in range(30):
    numero = rd.randint(6,340)
    lista_numeros.append(numero)   
print("Lista de numeros generada:")
print(lista_numeros)        

#Buscar los numeros divisibles entre 7
ldivisor = []
for d in range(30):
    divisor = rd.randint(1,9)
    ldivisor.append(divisor)   
ldivisibles = f.buscar_divisibles(lista_numeros, divisor)
print("Lista de divisores generada:")
print(ldivisor)
print(f"Numeros divisibles entre {divisor}:")
print(ldivisibles)
