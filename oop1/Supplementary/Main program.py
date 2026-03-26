from Projectilemotion import projectilemotion_solver

# Inputs from the problem
velocity = 11.0  # m/s
angle = 20.0     # degrees

range_dist, height = projectilemotion_solver(velocity, angle)

print(f"Horizontal Distance: {range_dist:.2f} m")
print(f"Maximum Height: {height:.2f} m")