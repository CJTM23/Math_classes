palabra = input().lower()
total = 0
for pos, letra in enumerate(palabra):
    if letra in ("aeiou"):
        total -= pos
    else:
        total += pos
print(total)

palabra2 = input().lower()
pos2 = 0
for score in palabra2:
    letra2 = palabra2[pos2]
    if letra2 in ("aeiou"):
        score = -pos2
    else:
        score = +pos2
    score_total = score
    pos2 += 1
print(score_total)

#-------------------------------------
def calcularpuntaje(palabra):
    total = 0
    for pos, letra in enumerate(palabra):
        if letra in "aeiou":
            total -=pos
        else:
             total += pos
    return total