using Plots

println("="^70)
println("MÉTODO DE DISCOS (REBANADAS)")
println("Plano XY VERTICAL: Y arriba, X a la derecha, Z hacia adelante")
println("="^70)
println()

# ============================================
# FUNCIONES AUXILIARES
# ============================================
function volumen_discos(f, a, b, n=1000)
    dx = (b - a) / n
    suma = sum(f(a + i*dx)^2 for i in 0:n-1)
    return π * suma * dx
end

# ============================================
# EJEMPLO 1: f(x) = x² ROTANDO EN EJE X
# ============================================
println("EJEMPLO 1: f(x) = x² rotando alrededor del eje X")
println("-"^70)

f1(x) = x^2
a1, b1 = 0.0, 1.0

V1 = volumen_discos(f1, a1, b1)
V1_exacto = π / 5
println("Intervalo: [0, 1]")
println("Volumen calculado: ", round(V1, digits=6))
println("Volumen exacto: ", round(V1_exacto, digits=6))
println()

# Gráfico 2D - Plano XY vertical (Z=0)
# Para que XY esté vertical: usamos (X, Z, Y) donde Y es la altura
x1_vals = range(a1, b1, length=200)

p1_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="f(x) = x² en plano XY vertical",
    camera=(60, 15), size=(800, 700), legend=:topright,
    xlims=(-0.1, 1.2), ylims=(-0.3, 0.3), zlims=(-0.1, 1.2))

# Dibujar función: X horizontal, Y vertical (en zlabel), Z=0
# Coordenadas: (x, 0, f(x))
plot!(p1_2d, x1_vals, zeros(length(x1_vals)), f1.(x1_vals),
    lw=4, color=:blue, label="y = x²")

# Eje X (horizontal)
plot!(p1_2d, [a1, b1], [0, 0], [0, 0],
    lw=3, color=:red, label="Eje X")

# Región sombreada
for i in 1:10:length(x1_vals)
    plot!(p1_2d, [x1_vals[i], x1_vals[i]], [0, 0], [0, f1(x1_vals[i])],
        color=:lightblue, alpha=0.3, label="")
end

# Discos (perpendiculares al eje X)
plot!(p1_2d, [b1, b1], [0, 0], [0, f1(b1)],
    lw=6, color=:red, label="Rebanadas")

for x_disc in [0.25, 0.5, 0.75]
    plot!(p1_2d, [x_disc, x_disc], [0, 0], [0, f1(x_disc)],
        lw=4, color=:orange, alpha=0.8, label="")
end

# Gráfico 3D - Sólido sobre eje X
# Paraboloide centrado en el origen, a lo largo del eje X
n_pts = 60
x_3d = range(a1, b1, length=n_pts)
θ_vals = range(0, 2π, length=n_pts)

# Generar superficie: (X, Z, Y) con rotación en YZ
X1_surf = [x for x in x_3d, θ in θ_vals]
Z1_surf = [f1(x) * cos(θ) for x in x_3d, θ in θ_vals]
Y1_surf = [f1(x) * sin(θ) for x in x_3d, θ in θ_vals]

p1_3d = surface(X1_surf, Z1_surf, Y1_surf, alpha=0.9,
    seriescolor=:blues, fill_z=X1_surf,
    colorbar=false, legend=false,
    title="Paraboloide (eje X)",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(800, 700))

# Eje X
plot!(p1_3d, [a1, b1], [0, 0], [0, 0], lw=3, color=:red)

# Círculos en extremos
θ_circ = range(0, 2π, length=100)
r_end = f1(b1)
plot!(p1_3d, fill(b1, 100), r_end .* cos.(θ_circ), r_end .* sin.(θ_circ),
    lw=4, color=:red)

# Líneas radiales
for θ in range(0, 2π, length=12)
    plot!(p1_3d, [b1, b1], [0, r_end*cos(θ)], [0, r_end*sin(θ)],
        lw=2, color=:red, alpha=0.7)
end

# Círculos intermedios
for x_s in [0.3, 0.6]
    r_s = f1(x_s)
    plot!(p1_3d, fill(x_s, 100), r_s .* cos.(θ_circ), r_s .* sin.(θ_circ),
        lw=2, color=:orange, alpha=0.6)
end

println("Mostrando Ejemplo 1...")
display(plot(p1_2d, p1_3d, layout=(1, 2), size=(1600, 700)))
println()
