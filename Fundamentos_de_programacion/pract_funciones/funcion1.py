def buscar_divisibles(numeros, divisor):
    ldivisibles = []
    for numero in numeros:
        residuo = numero % divisor
        if residuo == 0:
            ldivisibles.append(numero)
    return ldivisibles


def Imprimeuniversidades(l):
    luniversiades = []
    for direccion in l:
        lpalabras = direccion. lower().split(".")
        if "edu" in lpalabras:
            pos = lpalabras.index("edu")
            universidad = lpalabras[pos -1]
            if universidad not in luniversiades:
                luniversiades. append (universidad)
    print(universidad)
    for pos, u in enumerate (luniversiades) :
        print(str(pos + 1) + ".)" + universidad)