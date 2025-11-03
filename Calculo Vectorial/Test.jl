using Plots

# Define the range for x and y, avoid x = 0
xr = vcat(range(-5, -0.1, length=10), range(0.1, 5, length=10))
yr = range(-5, 5, length=20)

# Define the gradient components
# ∇f = [∂f/∂x, ∂f/∂y] = [1/x, 0]
grad_x(x, y) = 1/x
grad_y(x, y) = 0

# Create grids
X = [xi for xi in xr, yi in yr]
Y = [yi for xi in xr, yi in yr]

# Evaluate vector components on the grid
U = [grad_x(xi, yi) for xi in xr, yi in yr]
V = [grad_y(xi, yi) for xi in xr, yi in yr]

# Create a quiver plot (vector field)
quiver(
    X,
    Y,
    quiver=(U, V),
    title="Gradient Field of ln(3x)",
    xlabel="x",
    ylabel="y"
)

# Set plot limits
xlims!(-5, 5)
ylims!(-5, 5)
# Create a 3D surface plot of ln(3x)
zr = [log(3*abs(x)) for x in xr, y in yr]
surface!(X, Y, zr, alpha=0.3)  # alpha controls transparency