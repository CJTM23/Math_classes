
edad = 39 # variable de tipo entero :)
altura = 1.75 # variable de tipo float (decimales)
es_mayor_edad = True # variable de tipo booleano (valores de verdad)
es_profesor = True
estado_civil = "casado" # variable de tipo string (palabras / cadena de caracteres)
pais = "Ecuador"
nombre = "Frank Malo"

# nombre universidad = "espol" # NO , error
# "espol" = nombre # error
#1estudiante = "Frank" # error
#nom*bre = "Frank" # error


#variable = valor (dato quemado, resultado d una operacion, resultado de una funcion)
# temperatura = obtener_temperatura()
# total_pagar = (VU * C) * 1.15

#nombre, apellido = "Frank", "Malo" # correcto

# nombre, edad = "Frank", 2025-1986 # asignacion multiple

from datetime import datetime
año_actual =  datetime.now().year
edad = año_actual -1986

edad = miedad = 2025 -1986

cal_fp, cal_bd = 79.90, 87.65
cal_bd, cal_fp = cal_fp, cal_bd

# operaciones
# numeros (+, -, *, /, //, %, **)
# x = 11 % 2
# y = 11 // 2

# segundos_totales = 78000
# segundos_totales = 3665
# horas = segundos_totales // 3600
# minutos = (segundos_totales % 3600) // 60
# segundos = segundos_totales % 60
# print(horas, minutos, segundos)


# definan un script para verificar si puedo subirme al bus
# linea_bus = 50 #almacenado en mi cerebro
# bus = 70 # lo que ven mis ojos
# si_es_bus = linea_bus == bus

# definan un script para verificar si tengo dinero para subirme al bus
# bolsillo = 0.75 # lo que tengo
# costo_bus = 0.30 # lo que vale el bus
# me_alcanza = bolsillo >= costo_bus

# chofer_amigo = True
# #si_puedo_subir = si_es_bus and me_alcanza
# si_puedo_subir = linea_bus == bus and bolsillo >= costo_bus


# generar una script de descuento en promociones
# si compro más de 100 unidades  o si la compra supera los $1000 tengo un descuento del 10 %

# unidades = 50
# precio_unidad = 4
# total_venta = unidades * precio_unidad
# aplica_descuento = unidades > 100 or total_venta > 1000



# # input # funcion que sirve para ingresar datos por teclado
# nombre = input("INGRESE SU NOMBRE POR FAVOR: ")
# print("hola", nombre)



# cambiar el script para que se ingrese por teclado los datos
# linea_bus = 50 #almacenado en mi cerebro
# bus = input("Ingrese la linea del bus: ")
# bus = int(bus) # bus le asigno el entero de bus #CONVERSIONES DE DATOS
# si_es_bus = linea_bus == bus
# print(si_es_bus)

# si quiero convertir a entero int(variable)
# si quiero convertir a flotante float(variable)
# si quiero convertir a texto str(variable)


# from datetime import datetime
#
# año_actual = datetime.now().year
# año_nacimiento = input("Ingrese el año de nacimiento: ")
# edad = año_actual - int(año_nacimiento)
# print(edad)



# tarea par la siguiente clase, investigar la funcion format