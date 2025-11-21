# Te han proporcionado el siguiente string con información de varios desarrolladores. Cada desarrollador está separado por ; y cada dato (nombre, edad, lenguaje favorito) está separado por ::

datos = "Ana:25:Python;Luis:30:JavaScript;María:28:Java;Carlos:35:Python;Lucía:29:C++"
# Actividades
# Separar todos los elementos individuales en una lista plana
# Paso 1: separar por ";"
separados = datos.split(";")

# Paso 2: separar cada grupo por ":"
lelementos = []
for grupo in separados:
    lelementos.extend(grupo.split(":"))

print(lelementos)
# Separa el string en una lista llamada lelementos, que contenga cada valor individual como un elemento (nombre, edad, lenguaje, nombre, edad, lenguaje...). Ejemplo

lelementos= ['Ana', '25', 'Python', 'Luis', '30', 'JavaScript', 'María', '28', 'Java', 'Carlos', '35', 'Python', 'Lucía', '29', 'C++']

 

# 2.- Obtener sublistas por slicing

# Usando slicing sobre elementos, crea tres nuevas listas:

# lnombres: contiene cada 3er elemento empezando desde el índice 0.

# ledades: cada 3er elemento empezando desde el índice 1.

# llenguajes: cada 3er elemento desde el índice 2.
lnombres = lelementos[0::3]    # nombre cada 3 elementos
ledades = lelementos[1::3]     # edad cada 3 elementos
llenguajes = lelementos[2::3]  # lenguaje cada 3 elementos

print(lnombres)
print(ledades)
print(llenguajes)
 

# 3.- Unir los nombres en un solo string separado por comas

# A partir de la lista lnombres, crea un string cadena_nombres con los nombres separados por comas.

cadena_nombres = ", ".join(lnombres)
print(cadena_nombres)

# 4.- Contar cuántos usan "Python" como lenguaje favorito

# A partir de la lista llenguajes, calcula cuántos "Python" hay y guárdalo en python_count.
python_count = llenguajes.count("Python")
print(python_count)
# 5.- Obtener los datos del tercer desarrollador

# Usando indexamiento y slicing sobre elementos, guarda en variables:

# nombre_3

# edad_3

# lenguaje_3
nombre_3 = lelementos[6]
edad_3 = lelementos[7]
lenguaje_3 = lelementos[8]

print(nombre_3, edad_3, lenguaje_3)