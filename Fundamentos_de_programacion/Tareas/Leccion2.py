import random

# 1. Generar una lista de 57 números aleatorios únicos entre 12 y 1632
lista_original = random.sample(range(12, 1633), 57)

total_efectividad = 0  # para ir acumulando los porcentajes

# 2. Repetir 100 veces
for _ in range(100):
    lista_mezclada = lista_original.copy()
    random.shuffle(lista_mezclada)
    
    # 2.2 Contar cuántos elementos cambiaron de posición
    X = sum(1 for i in range(len(lista_original)) if lista_mezclada[i] != lista_original[i])
    
    # 2.3 Calcular porcentaje de efectividad de esta iteración
    efectividad_iteracion = X * 100 / len(lista_original)
    
    total_efectividad += efectividad_iteracion  # Acumular

# 3. Calcular el porcentaje final (promedio)
efectividad_final = total_efectividad / 100

# Mostrar resultado
print(f"Porcentaje de efectividad final: {efectividad_final:.2f}%")