#lanzar los dados hasta que las 2 caras de ambos sean iguales.
import random as rd
dado1 =rd.randint(1,6)
dado2 =rd.randint(1,6)

while dado1 != dado2:
    dado1 =rd.randint(1,6)
    dado2 =rd.randint(1,6)
print(dado1,dado2)

palabra = 'fundamentos'
#necesito una vocal aleatoria
# letra = rd.choice(palabra)
# while letra not in 'aeiou':
#     letra = rd.choice(palabra)
# print(letra)

# def colatz(n):
#     while n != 1:
#         print(n,end=' ')
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#     print(n)

# lcontadores = []
# for n in range(1,10000):
#     cont = colatz(n)
#     lcontadores.append(cont)

# numero = lcontadores.index(max(lcontadores)) + 1
# print(numero)

#numero feliz
n=int(input('Dame un numero: '))
s=0
n=list(str(n))
lsecuencia_n = []
for i in n:
    i = int(i)
    s += i**2
    lsecuencia_n.append(s)
while s != 1 and s not in lsecuencia_n[:-1]:
    n = list(str(s))
    s = 0
    for i in n:
        i = int(i)
        s += i**2
    lsecuencia_n.append(s)
print(lsecuencia_n)

for digito in str(n):
    s += int(digito)**2
n = int(s)
lsecuencia_n.append(n)
while n != 1 and n not in lsecuencia_n:
    for digito in str(n):
    s += int(digito)**2
    n = int(s)
    lsecuencia_n.append(n)
print(lsecuencia_n)