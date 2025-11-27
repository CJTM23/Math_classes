# # Actividad 1
# palabra1 = str(input("Palabra:")).lower()
# palabra1.replace(" ","")
# frase = ""
# total = 0
# while frase.lower() != "basta":
#     frase = input("Frase:")
#     frase.replace(",","")
#     frase.replace(".", "")
#     contador = frase.split(" ").count(palabra1)
#     total += contador
# print(total)

# # Actividad 2
import random as rd
# lrueda=["x"]*8+["rueda"]*4
# lchance =[]
# dinero =0
# ruedas = 0
# rd.shuffle(lrueda)
# print(lrueda)
# while len(lchance) <6 and ruedas != 4:
#     chance = int(input("Ingrese tu numero de la suerte: "))
#     while not 0 <= chance <= 11:
#         print(
#             "******************\nNumero no valido.\nIngrese un numero del 0 al 11.\nVuélvalo a intentar.\n******************")
#         chance = int(input("Ingrese tu numero de la suerte: "))
#     lchance.append(chance)
#     comparador = lrueda[int(chance)]
#     if comparador == "rueda":
#         dinero += 1000
#         ruedas +=1
#     print(f"Conseguiste: {ruedas} ruedas")
#
# if ruedas ==4:
#     print("¡Ganaste el premio mayor del carro!")
# else:
#     print(f"Ganaste: ${dinero} dólares")

#Actividad 3

cantidad_asientos_bus = int(input("Ingrese la cantidda de puestos dentro del bus: "))
asientos_vendidos = 0
while cantidad_asientos_bus - asientos_vendidos < 0:
    print(f" Puestos vendidos: {asientos_vendidos}/{cantidad_asientos_bus}")
    asientos_vendidos += rd.randint(1, 9)
    print(f"Puestos a vender: {asientos_vendidos}")
    print(f"Restando los puestos...")

print(f"ERROR. No se puede vender!!")
print(f"EL autobus está lleno. No se pueden vender más puestos.")
