#Parte 1
resultado = """Resultado de Laboratorio 'Su Salud' 
Nombre del paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma medico responsable Dr. Juan Pozo"""
separacion = resultado.split()
indicadores = []
for i,palabra in enumerate(separacion):
    if palabra.isupper():
        indicadores.append(separacion[i:i+3])

indicadores[-1][-1] = indicadores[-1][-1].replace(".", "")
medico = " ".join(separacion[separacion.index("responsable")+2:])
recomendacion = 0

print("INFORME DE LABORATORIO\n**********************\n")
for indicador,valor,unidad in indicadores:
    if indicador == "BGT":
        if float(valor) > 150.00:
            print(f"{indicador:<10}{valor:<15}{unidad}**")
            recomendacion = 1
        else:
            print(f"{indicador:<10}{valor:<15}{unidad}")
    else:
        print(f"{indicador:<10}{valor:<15}{unidad}")
print(f"\nMédico: {medico}")
if recomendacion == 1:
    print(f"** Su nivel de azúcar es alto. Se recomienda ir al endocrinólogo")

#Parte 2
def es_perfecto(n):
    if n<=1:
        return False
    divisores = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            divisores+=i
    return divisores==n

n=int(input("Ingresa un numero: "))
if es_perfecto(n):
    print(f"El número {n} es perfecto")
else:
    print(f"El número {n} no es perfecto")