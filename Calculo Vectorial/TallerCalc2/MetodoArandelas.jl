using Plots

println("="^70)
println("MÉTODO DE ARANDELAS (WASHERS)")
println("Dos funciones f(x) ≥ g(x) rotando, generando sólido con hueco")
println("Fórmula: V = π∫[a,b] [f(x)² - g(x)²] dx")
println("="^70)
println()

# ============================================
# FUNCIÓN PARA CALCULAR VOLUMEN POR ARANDELAS
# ============================================
function volumen_arandelas(f, g, a, b, n=1000)
    dx = (b - a) / n
    suma = sum((f(a + i*dx)^2 - g(a + i*dx)^2) for i in 0:n-1)
    return π * suma * dx
end

# ============================================
# EJEMPLO 1: ROTACIÓN EN EJE X
# f(x) = 2, g(x) = x en [0, 1]
# ============================================
println("EJEMPLO 1: Rotación en eje X")
println("-"^70)

f1(x) = 2.0
g1(x) = x
a1, b1 = 0.0, 1.0

V1 = volumen_arandelas(f1, g1, a1, b1)
println("f(x) = 2, g(x) = x en [0, 1]")
println("Volumen calculado: ", round(V1, digits=6))
println()

# Gráfico 2D - Plano XY vertical
x1_vals = range(a1, b1, length=200)

p1_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="Región entre f(x)=2 y g(x)=x",
    camera=(60, 15), size=(800, 700), legend=:topright,
    xlims=(-0.2, 1.3), ylims=(-0.3, 0.3), zlims=(-0.2, 2.3))

# Función exterior (f)
plot!(p1_2d, x1_vals, zeros(length(x1_vals)), f1.(x1_vals),
    lw=4, color=:blue, label="f(x) = 2")

# Función interior (g)
plot!(p1_2d, x1_vals, zeros(length(x1_vals)), g1.(x1_vals),
    lw=4, color=:red, label="g(x) = x")

# Eje X
plot!(p1_2d, [a1, b1], [0, 0], [0, 0],
    lw=3, color=:black, label="Eje X")

# Región sombreada entre las curvas
for i in 1:10:length(x1_vals)
    plot!(p1_2d, [x1_vals[i], x1_vals[i]], [0, 0], [g1(x1_vals[i]), f1(x1_vals[i])],
        color=:green, alpha=0.3, label="")
end

# Arandelas (discos con hueco)
for x_disc in [0.3, 0.6, 0.9]
    plot!(p1_2d, [x_disc, x_disc], [0, 0], [g1(x_disc), f1(x_disc)],
        lw=5, color=:orange, alpha=0.8, label="")
end

# Gráfico 3D - Sólido con hueco
n_pts = 60
x_3d = range(a1, b1, length=n_pts)
θ_vals = range(0, 2π, length=n_pts)

# Superficie exterior
X1_ext = [x for x in x_3d, θ in θ_vals]
Z1_ext = [f1(x) * cos(θ) for x in x_3d, θ in θ_vals]
Y1_ext = [f1(x) * sin(θ) for x in x_3d, θ in θ_vals]

# Superficie interior (hueco)
X1_int = [x for x in x_3d, θ in θ_vals]
Z1_int = [g1(x) * cos(θ) for x in x_3d, θ in θ_vals]
Y1_int = [g1(x) * sin(θ) for x in x_3d, θ in θ_vals]

p1_3d = surface(X1_ext, Z1_ext, Y1_ext, alpha=0.8,
    seriescolor=:blues, fill_z=X1_ext,
    colorbar=false, legend=false,
    title="Arandela (eje X)",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(800, 700))

# Superficie interior
surface!(p1_3d, X1_int, Z1_int, Y1_int, alpha=0.7,
    seriescolor=:reds, fill_z=X1_int)

# Eje X
plot!(p1_3d, [a1, b1], [0, 0], [0, 0], lw=3, color=:black)

# Círculos en extremo
θ_circ = range(0, 2π, length=100)
r1_ext = f1(b1)
r1_int = g1(b1)
plot!(p1_3d, fill(b1, 100), r1_ext .* cos.(θ_circ), r1_ext .* sin.(θ_circ),
    lw=3, color=:blue)
plot!(p1_3d, fill(b1, 100), r1_int .* cos.(θ_circ), r1_int .* sin.(θ_circ),
    lw=3, color=:red)

println("Mostrando Ejemplo 1...")
display(plot(p1_2d, p1_3d, layout=(1, 2), size=(1600, 700)))
println()

# ============================================
# EJEMPLO 2: ROTACIÓN EN EJE X
# f(x) = e^(-x/2) + 1, g(x) = 0.5 en [0, 3]
# ============================================
println("EJEMPLO 2: Rotación en eje X")
println("-"^70)

f2(x) = exp(-x/2) + 1
g2(x) = 0.5
a2, b2 = 0.0, 3.0

V2 = volumen_arandelas(f2, g2, a2, b2)
println("f(x) = e^(-x/2)+1, g(x) = 0.5 en [0, 3]")
println("Volumen calculado: ", round(V2, digits=6))
println()

x2_vals = range(a2, b2, length=200)

p2_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="Región entre f(x)=e^(-x/2)+1 y g(x)=0.5",
    camera=(60, 15), size=(800, 700), legend=:topright,
    xlims=(-0.3, 3.3), ylims=(-0.3, 0.3), zlims=(-0.2, 2.3))

plot!(p2_2d, x2_vals, zeros(length(x2_vals)), f2.(x2_vals),
    lw=4, color=:blue, label="f(x) = e^(-x/2)+1")
plot!(p2_2d, x2_vals, zeros(length(x2_vals)), f2.(x2_vals) .* 0 .+ g2(0),
    lw=4, color=:red, label="g(x) = 0.5")
plot!(p2_2d, [a2, b2], [0, 0], [0, 0], lw=3, color=:black, label="Eje X")

for i in 1:15:length(x2_vals)
    plot!(p2_2d, [x2_vals[i], x2_vals[i]], [0, 0], [g2(x2_vals[i]), f2(x2_vals[i])],
        color=:green, alpha=0.3, label="")
end

for x_disc in [0.5, 1.5, 2.5]
    plot!(p2_2d, [x_disc, x_disc], [0, 0], [g2(x_disc), f2(x_disc)],
        lw=5, color=:orange, alpha=0.8, label="")
end

x_3d2 = range(a2, b2, length=n_pts)
X2_ext = [x for x in x_3d2, θ in θ_vals]
Z2_ext = [f2(x) * cos(θ) for x in x_3d2, θ in θ_vals]
Y2_ext = [f2(x) * sin(θ) for x in x_3d2, θ in θ_vals]
X2_int = [x for x in x_3d2, θ in θ_vals]
Z2_int = [g2(x) * cos(θ) for x in x_3d2, θ in θ_vals]
Y2_int = [g2(x) * sin(θ) for x in x_3d2, θ in θ_vals]

p2_3d = surface(X2_ext, Z2_ext, Y2_ext, alpha=0.8,
    seriescolor=:blues, fill_z=X2_ext,
    colorbar=false, legend=false,
    title="Arandela (eje X)",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(800, 700))
surface!(p2_3d, X2_int, Z2_int, Y2_int, alpha=0.7,
    seriescolor=:reds, fill_z=X2_int)
plot!(p2_3d, [a2, b2], [0, 0], [0, 0], lw=3, color=:black)

println("Mostrando Ejemplo 2...")
display(plot(p2_2d, p2_3d, layout=(1, 2), size=(1600, 700)))
println()

# ============================================
# EJEMPLO 3: ROTACIÓN EN EJE Y
# f(y) = 3, g(y) = y en [0, 2]
# ============================================
println("EJEMPLO 3: Rotación en eje Y")
println("-"^70)

f3(y) = 3.0
g3(y) = y
a3, b3 = 0.0, 2.0

V3 = volumen_arandelas(f3, g3, a3, b3)
println("f(y) = 3, g(y) = y en [0, 2]")
println("Volumen calculado: ", round(V3, digits=6))
println()

y3_vals = range(a3, b3, length=200)

p3_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="Región entre f(y)=3 y g(y)=y",
    camera=(60, 15), size=(800, 700), legend=:topright,
    xlims=(-0.3, 3.5), ylims=(-0.3, 0.3), zlims=(-0.3, 2.5))

plot!(p3_2d, f3.(y3_vals), zeros(length(y3_vals)), y3_vals,
    lw=4, color=:blue, label="f(y) = 3")
plot!(p3_2d, g3.(y3_vals), zeros(length(y3_vals)), y3_vals,
    lw=4, color=:red, label="g(y) = y")
plot!(p3_2d, [0, 0], [0, 0], [a3, b3], lw=3, color=:black, label="Eje Y")

for i in 1:15:length(y3_vals)
    plot!(p3_2d, [g3(y3_vals[i]), f3(y3_vals[i])], [0, 0], [y3_vals[i], y3_vals[i]],
        color=:green, alpha=0.3, label="")
end

for y_disc in [0.5, 1.0, 1.5]
    plot!(p3_2d, [g3(y_disc), f3(y_disc)], [0, 0], [y_disc, y_disc],
        lw=5, color=:orange, alpha=0.8, label="")
end

y_3d3 = range(a3, b3, length=n_pts)
X3_ext = [f3(y) * cos(θ) for y in y_3d3, θ in θ_vals]
Z3_ext = [f3(y) * sin(θ) for y in y_3d3, θ in θ_vals]
Y3_ext = [y for y in y_3d3, θ in θ_vals]
X3_int = [g3(y) * cos(θ) for y in y_3d3, θ in θ_vals]
Z3_int = [g3(y) * sin(θ) for y in y_3d3, θ in θ_vals]
Y3_int = [y for y in y_3d3, θ in θ_vals]

p3_3d = surface(X3_ext, Z3_ext, Y3_ext, alpha=0.8,
    seriescolor=:blues, fill_z=Y3_ext,
    colorbar=false, legend=false,
    title="Arandela (eje Y)",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(800, 700))
surface!(p3_3d, X3_int, Z3_int, Y3_int, alpha=0.7,
    seriescolor=:reds, fill_z=Y3_int)
plot!(p3_3d, [0, 0], [0, 0], [a3, b3], lw=3, color=:black)

println("Mostrando Ejemplo 3...")
display(plot(p3_2d, p3_3d, layout=(1, 2), size=(1600, 700)))
println()

# ============================================
# EJEMPLO 4: ROTACIÓN EN EJE Y
# f(y) = 2y, g(y) = y en [0, 1.5]
# ============================================
println("EJEMPLO 4: Rotación en eje Y")
println("-"^70)

f4(y) = 2*y
g4(y) = y
a4, b4 = 0.0, 1.5

V4 = volumen_arandelas(f4, g4, a4, b4)
println("f(y) = 2y, g(y) = y en [0, 1.5]")
println("Volumen calculado: ", round(V4, digits=6))
println()

y4_vals = range(a4, b4, length=200)

p4_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="Región entre f(y)=2y y g(y)=y",
    camera=(60, 15), size=(800, 700), legend=:topright,
    xlims=(-0.3, 3.5), ylims=(-0.3, 0.3), zlims=(-0.2, 1.8))

plot!(p4_2d, f4.(y4_vals), zeros(length(y4_vals)), y4_vals,
    lw=4, color=:blue, label="f(y) = 2y")
plot!(p4_2d, g4.(y4_vals), zeros(length(y4_vals)), y4_vals,
    lw=4, color=:red, label="g(y) = y")
plot!(p4_2d, [0, 0], [0, 0], [a4, b4], lw=3, color=:black, label="Eje Y")

for i in 1:15:length(y4_vals)
    plot!(p4_2d, [g4(y4_vals[i]), f4(y4_vals[i])], [0, 0], [y4_vals[i], y4_vals[i]],
        color=:green, alpha=0.3, label="")
end

for y_disc in [0.4, 0.8, 1.2]
    plot!(p4_2d, [g4(y_disc), f4(y_disc)], [0, 0], [y_disc, y_disc],
        lw=5, color=:orange, alpha=0.8, label="")
end

y_3d4 = range(a4, b4, length=n_pts)
X4_ext = [f4(y) * cos(θ) for y in y_3d4, θ in θ_vals]
Z4_ext = [f4(y) * sin(θ) for y in y_3d4, θ in θ_vals]
Y4_ext = [y for y in y_3d4, θ in θ_vals]
X4_int = [g4(y) * cos(θ) for y in y_3d4, θ in θ_vals]
Z4_int = [g4(y) * sin(θ) for y in y_3d4, θ in θ_vals]
Y4_int = [y for y in y_3d4, θ in θ_vals]

p4_3d = surface(X4_ext, Z4_ext, Y4_ext, alpha=0.8,
    seriescolor=:greens, fill_z=Y4_ext,
    colorbar=false, legend=false,
    title="Arandela (eje Y)",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(800, 700))
surface!(p4_3d, X4_int, Z4_int, Y4_int, alpha=0.7,
    seriescolor=:reds, fill_z=Y4_int)
plot!(p4_3d, [0, 0], [0, 0], [a4, b4], lw=3, color=:black)

println("Mostrando Ejemplo 4...")
display(plot(p4_2d, p4_3d, layout=(1, 2), size=(1600, 700)))
println()

println("="^70)
println("MÉTODO DE ARANDELAS COMPLETADO")
println("4 ejemplos: 2 rotando en eje X, 2 rotando en eje Y")
println("="^70)