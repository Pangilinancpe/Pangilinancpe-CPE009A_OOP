import math

def projectilemotion_solver(v_i, theta):
    g = 9.8  # Acceleration due to gravity (m/s^2)
    # Convert degrees to radians
    theta_rad = math.radians(theta)
    
    # Range formula: R = (v_i^2 * sin(2 * theta)) / g
    horizontal_range = (v_i**2 * math.sin(2 * theta_rad)) / g
    
    # Max Height formula: h = (v_i^2 * (sin(theta))^2) / (2 * g)
    max_height = (v_i**2 * (math.sin(theta_rad)**2)) / (2 * g)
    
    return horizontal_range, max_height