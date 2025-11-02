using Plots   # librería para gráficos

# Definimos la función
f(x, y) = sin(x) * cos(y)

# Rango de valores
x = -π:0.1:π
y = -π:0.1:π

# Construimos la grilla
Z = [f(xi, yi) for xi in x, yi in y]

# Graficamos la superficie
plt = plot(x, y, Z, st = :surface,
           title = "Superficie z = sin(x)*cos(y)",
           xlabel = "x", ylabel = "y", zlabel = "z")
display(plt)