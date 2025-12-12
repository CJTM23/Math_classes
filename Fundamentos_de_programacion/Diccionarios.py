# # # # #resumen de que hacen los diccionarios y sus propiedades: 
# # # # #se actualizan valores, no claves. No tienen orden y no se pueden indexar
# # # # #la clave es la unica via para cambiar el valor
# # # # #se usa para asignar una regla de correspondencia entre claves "nobmres" y valores "objetos", como un conjuntos.
# # # # #diccionario: conjunto de pares clave-valor

import random as rd
# # # # d ={}
# # # # for _ in range(100):
# # # #     n = rd.randint(5,25)
# # # #     if n in d: #n pregunta si n es una clave del diccionario
# # # #         d[n] += 1
# # # #     else:
# # # #         d[n] = 1
# # # # print(d)

# # lpalabras = ['hola','mundo','hola','fundamentos','fiec','python']
# # # #hacer funcion llamada generar GeneraFrecuencia que:
# # # #generar un ciclo de 50 repeticiones y en cada ciclo va a escoger una palabra aleatoria
# # # #Y agregarla a un diccionario junto con su cantidad de apariciones

# # # def GeneraFrecuencia(lpalabras):
# # #     import random as rd
# # #     d = {}
# # #     for _ in range(50):
# # #         palabra = rd.choice(lpalabras)
# # #         if palabra in d:
# # #             d[palabra] += 1
# # #         else:
# # #             d[palabra] = 1
# # #     return d

# # # d={}
# # # x = d.get('clave_no_existe',0) #si la clave no existe, devuelve un valor arbitrario
# # # print(x)

# # def GeneraFrecuencia():
# #     lpalabras = ['hola','mundo','hola','fundamentos','fiec','python']
# #     import random as rd
# #     d = {}
# #     for _ in range(50):
# #         palabra = rd.choice(lpalabras)
# #         d[palabra] = d.get(palabra,0) + 1
# #     return d
# # print(GeneraFrecuencia())
# # # La diferencia entre usar "if palabra in d" y "d.get(palabra,0)" es que el primero verifica 
# # # la existencia de la clave antes de actualizar su valor, mientras que el segundo obtiene el 
# # # valor actual o un valor predeterminado (0) si la clave no existe, permitiendo una actualización 
# # # directa en una sola línea.

# # d={}
# # for palabra in lpalabras:
# #     tamaño = len(palabra)
# #     d[tamaño] = d.get(tamaño,[]) + [palabra]
# # print(d) 
# # for palabra in d:
# #     if palabra.startswith('f'):
# #         print(palabra, d[palabra])
# #     if d[palabra] > 2:
# #         print(palabra)
# #si quiero buscar algun valor o clave, tengo que recorrer (for)
# d={1:rd.randint(10,8544),2:rd.randint(10,8544),3:rd.randint(10,8544)}
# print(d)
# for palabra, numero in d.item():
#     if numero > 0:
#         print(numero)


materias = {a:['estructura','algoritmos','ingles'],b:['calculo','algebra'],c:['fisica1','fisica2','ingles']}
for estudiante 