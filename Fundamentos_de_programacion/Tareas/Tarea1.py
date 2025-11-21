# input = str('Nombre completo:  ')
# input = ('Edad:  ')
# input = ('Estatura en metros:  ')
# input = float('Peso en kilogramos:  ')
# input = bool('¿Realiza actividad física al menos 3 veces por semana? (sí/no):  ')
# input = bool('¿Duerme al menos 7 horas por día? (sí/no):  ')
# input = bool('¿Fuma regularmente? (sí/no):  ')
# input = bool('¿Consume frutas y verduras a diario? (sí/no):  ')
# Convertir todas las entradas necesarias a los tipos de datos correctos (int, float, bool).

Nombre = str(input('Nombre completo:  '))
Edad = int(input('Edad:  '))
Estatura = float(input('Estatura en metros: '))
Peso = float(input('Peso en kilogramos:  '))
Actividad_Fisica = input('¿Realiza actividad física al menos 3 veces por semana? (si/no):  ').strip().lower() == 'si'
Duerme_Bien = input('¿Duerme al menos 7 horas por día? (si/no):  ').strip().lower() == 'si'
Fuma = input('¿Fuma regularmente? (si/no):  ').strip().lower() == 'si'
Consume_Frutas_Verduras = input('¿Consume frutas y verduras a diario? (si/no):  ').strip().lower == 'si'

IMC = Peso / (Estatura ** 2)

# Si el usuario es mayor de edad (edad >= 18)
es_mayor_de_edad = Edad >= 18
print("Mayoria de edad:" , es_mayor_de_edad)

# Años restantes para cumplir 100 años
anos_restantes = 100 - Edad
print('Le faltan', anos_restantes, 'años para cumplir 100 años.')

# Si la estatura está dentro del rango saludable (1.50 m a 2.00 m)
rang_saludable_estatura = 1.50 <= Estatura <= 2.00
print("Tiene estatura saludable:", rang_saludable_estatura)

# Si tiene bajo peso (IMC < 18.5)
bajo_peso = IMC < 18.5 
print("Tiene bajo peso:", bajo_peso)

# Si tiene sobrepeso (IMC > 25)
sobrepeso = IMC > 25
print("Tiene sobrepeso:", sobrepeso)

# Si el IMC está dentro del rango saludable (18.5 ≤ IMC ≤ 24.9)
imc_saludable = 18.5 <= IMC <= 24.9
print("Tiene IMC saludable:", imc_saludable)

# finalmente debe mostrar su perfil de salud de acuerdo a lo siguiente lógica 
# Cumple las 5 condiciones su perfil es óptimo y saludable
# Cumple 4 condiciones: su perfil saludable
# Cumple 2 o 3 condiciones su perfil está en riesgo
# Cumple 1 o ninguna condición su perfil es crítico 

condiciones = [
    Actividad_Fisica,
    Duerme_Bien,
    not Fuma,
    Consume_Frutas_Verduras,
    imc_saludable
]

# Sumamos los valores booleanos (True = 1, False = 0)
puntaje = sum(condiciones)

# Determinar perfil de salud
if puntaje == 5:
    perfil = "Óptimo y saludable"
elif puntaje == 4:
    perfil = "Saludable"
elif 2 <= puntaje <= 3:
    perfil = "En riesgo"
else:
    perfil = "Crítico"

print("Usted tiene un perfil ", perfil)