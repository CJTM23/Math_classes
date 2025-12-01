#tema1
import random as rd
jugador = input('ingrese judador: ')
cantidad = int(input('ingrese cantidad de ticket comprados: '))
premios = [10.5,3.75,100.99]
if cantidad < 6:
    premios.append('joker')
ganados_premios = rd.sample(premios, k=cantidad)
if 'joker' in ganados_premios:
    print(f'{jugador}ha ganado $0.0')
else:
    total = sum(ganados_premios)
    print(f'{jugador} ha ganado ${total}:.2f')
    print(f'Valor maximo obtenido: ${max(ganados_premios):.2f}')

#tema2
def analiza_expresion(expresion):
    loperadores = ['=','+','-','*','/']
    lsimbolos = expresion.split(' ')
    lerrores = []
    pos = 0
    for simbolo in lsimbolos:
        if pos  % 2 == 0 and not simbolo.isdigit():
            lerrores.append(simbolo)
        if pos % 2 != 0 and simbolo not in loperadores:
            lerrores.append(simbolo)
        pos += 1
    return lerrores
x = ('x = 5 + 3 - 2 * 4 / 2')
errores = analiza_expresion(x)
print ('Errores encontrados: ', errores)

#tema 3
cantidad = int(input('Cantida de empleados: '))
ldias = []
lconflicto = []
for i in range(cantidad):
    dia = int(input(str(i+1) + 'Ingrese el dia del mes: '))
    if dia in ldias and dia not in lconflicto:
        lconflicto.append(dia)
    ldias.append(dia)    
lconflicto.sort()
print('Dias con conflicto de vacaciones: ', lconflicto)
