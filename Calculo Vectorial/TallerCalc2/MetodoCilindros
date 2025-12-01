using Plots

println("="^70)
println("MÉTODO DE ARANDELAS - ROTACIÓN ALREDEDOR DE y = k")
println("Ejemplo del libro: Rotación alrededor de y = 2")
println("="^70)
println()

# ============================================
# FUNCIONES DEL EJEMPLO
# ============================================
# x = 4 - y²  (función exterior)
# x = y² + 2y (función interior)
# Rotación alrededor de y = 2

f(y) = 4 - y^2      # Radio exterior desde y=2
g(y) = y^2 + 2*y    # Radio interior desde y=2
k = 2.0             # Recta de rotación y = 2

# Intervalo de integración
c, d = -2.0, 1.0

println("Funciones:")
println("  f(y) = 4 - y²")
println("  g(y) = y² + 2y")
println("  Rotación: y = ", k)
println("  Intervalo: [", c, ", ", d, "]")
println()

# ============================================
# CÁLCULO DEL VOLUMEN
# ============================================
# Radio = |y - k| = |y - 2| = 2 - y (para y < 2)
# V = 2π ∫ |y-k| [f(y) - g(y)] dy

function volumen_arandelas_k(f, g, k, c, d, n=1000)
    dy = (d - c) / n
    suma = sum(abs((c + i*dy) - k) * (f(c + i*dy) - g(c + i*dy)) for i in 0:n-1)
    return 2π * suma * dy
end

V = volumen_arandelas_k(f, g, k, c, d)
println("Volumen calculado: ", round(V, digits=6))
println()

# ============================================
# GRÁFICO 2D - Región en plano XY vertical
# ============================================
y_vals = range(c, d, length=200)

p_2d = plot(xlabel="X", ylabel="Z", zlabel="Y",
    title="Región entre x=4-y² y x=y²+2y (rotación en y=2)",
    camera=(60, 15), size=(900, 700), legend=:topright,
    xlims=(-1, 5), ylims=(-0.5, 0.5), zlims=(-2.5, 2.5))

# Función exterior f(y) = 4 - y²
plot!(p_2d, f.(y_vals), zeros(length(y_vals)), y_vals,
    lw=4, color=:blue, label="x = 4-y²")

# Función interior g(y) = y² + 2y
plot!(p_2d, g.(y_vals), zeros(length(y_vals)), y_vals,
    lw=4, color=:red, label="x = y²+2y")

# Recta de rotación y = 2 (horizontal en el espacio 3D)
plot!(p_2d, [0, 5], [0, 0], [k, k],
    lw=3, color=:green, ls=:dash, label="y = 2 (eje)")

# Región sombreada entre las curvas
for i in 1:15:length(y_vals)
    plot!(p_2d, [g(y_vals[i]), f(y_vals[i])], [0, 0], [y_vals[i], y_vals[i]],
        color=:yellow, alpha=0.3, label="")
end

# Mostrar algunos cascarones (líneas desde y=2 hasta las funciones)
for y_shell in [-1.5, -0.5, 0.5]
    r = abs(y_shell - k)  # distancia a y=2
    h = f(y_shell) - g(y_shell)  # altura del cascarón
    
    # Línea desde y=2 hasta y_shell (mostrando el radio)
    plot!(p_2d, [0, 0], [0, 0], [k, y_shell],
        lw=3, color=:orange, alpha=0.7, label=(y_shell == -1.5 ? "Cascarones" : ""))
    
    # Segmento horizontal mostrando la altura h
    plot!(p_2d, [g(y_shell), f(y_shell)], [0, 0], [y_shell, y_shell],
        lw=4, color=:orange, alpha=0.8, label="")
end

# ============================================
# GRÁFICO 3D - Sólido de revolución
# ============================================
println("Generando sólido 3D...")

n_pts = 60
y_3d = range(c, d, length=n_pts)
θ_vals = range(0, 2π, length=n_pts)

# Para cada y, el radio desde y=2 es r = |y - 2| = 2 - y
# Las superficies se generan rotando alrededor de y=2

# Superficie exterior: x = f(y) = 4 - y²
# Coordenadas cilíndricas centradas en y=2
X_ext = [(f(y) - g(y))/2 + g(y) + (f(y) - g(y))/2 * cos(θ) for y in y_3d, θ in θ_vals]
Z_ext = [abs(y - k) * sin(θ) for y in y_3d, θ in θ_vals]
Y_ext = [abs(y - k) * cos(θ) + k for y in y_3d, θ in θ_vals]

# Mejor: usar coordenadas correctas
# El sólido rota alrededor de y=2 (horizontal)
# Para un punto (x, y), su distancia a y=2 es r = |y-2|

# Superficie exterior en coordenadas (X, Z, Y)
X_ext = [f(y) for y in y_3d, θ in θ_vals]
Z_ext = [abs(y - k) * sin(θ) for y in y_3d, θ in θ_vals]
Y_ext = [k + abs(y - k) * cos(θ) for y in y_3d, θ in θ_vals]

# Superficie interior
X_int = [g(y) for y in y_3d, θ in θ_vals]
Z_int = [abs(y - k) * sin(θ) for y in y_3d, θ in θ_vals]
Y_int = [k + abs(y - k) * cos(θ) for y in y_3d, θ in θ_vals]

p_3d = surface(X_ext, Z_ext, Y_ext, alpha=0.8,
    seriescolor=:blues, fill_z=Y_ext,
    colorbar=false, legend=false,
    title="Sólido rotando en y=2",
    xlabel="X", ylabel="Z", zlabel="Y",
    camera=(35, 20), size=(900, 700))

# Superficie interior
surface!(p_3d, X_int, Z_int, Y_int, alpha=0.7,
    seriescolor=:reds, fill_z=Y_int)

# Recta de rotación y=2
plot!(p_3d, [0, 5], [0, 0], [k, k], lw=3, color=:green, ls=:dash)

# Algunos círculos mostrando los cascarones
θ_circ = range(0, 2π, length=100)
for y_c in [-1.5, 0, 0.5]
    r_c = abs(y_c - k)
    x_ext_c = f(y_c)
    x_int_c = g(y_c)
    
    # Círculo exterior
    plot!(p_3d, fill(x_ext_c, 100), r_c .* sin.(θ_circ), k .+ r_c .* cos.(θ_circ),
        lw=2, color=:orange, alpha=0.6)
    
    # Círculo interior
    plot!(p_3d, fill(x_int_c, 100), r_c .* sin.(θ_circ), k .+ r_c .* cos.(θ_circ),
        lw=2, color=:orange, alpha=0.6)
end

# ============================================
# VISUALIZACIÓN FINAL
# ============================================
println("Mostrando visualización...")
display(plot(p_2d, p_3d, layout=(1, 2), size=(1800, 700)))
println()

println("="^70)
println("EJEMPLO DEL LIBRO COMPLETADO")
println("Fórmula usada: V = 2π∫ |y-k| [f(y) - g(y)] dy")
println("donde r = |y-2| = 2-y, h = f(y) - g(y)")
println("="^70)