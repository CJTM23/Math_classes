# Str-vacio + primera letra Str-list-for-palabra-pos0 Crear una variable con cada inicial de la frase, e imprimir las primeras letras en mayuscula. el yin y el yang son conceptos filosoficos de la cultira china
# p = palabra Diccionario de letras recorreo con un for letra por letra pos index de la lista abecedario, encuentra la posicion e indexa en la lsita de puntajes y eso te da el valor.


# Actividad 1
frase = input("Ingrese una frase chevere: ")
ifrase = frase.split(" ")
print(ifrase)
lletras = []
pos = 0
for _ in ifrase:
    caracter = ifrase[pos][0].upper()
    lletras.append(caracter)
    pos += 1
    frassefinal = "".join(lletras)
print(lletras)
print("Resultado final: ", frassefinal)




# actividad 2
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lpuntaje = [1, 3, 3, 2, 1, 4, 2, 4, 1, 9, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 9, 4, 10]
palabra = input("Ingrese una palabra a evaluar: ").upper()
puntajefinal = 0
for letra in palabra:
    pos = abecedario.find(letra)
    puntaje = lpuntaje[pos]
    puntajefinal += puntaje
print("Puntaje: ", puntajefinal)