import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"Two real roots:\n  x1 = {x1:.2f}\n  x2 = {x2:.2f}"

    elif discriminant == 0:
        x = -b / (2*a)
        result = f"One real root:\n  x = {x:.2f}"

    else:
        result = "No real roots (discriminant is negative)"

    # Save to text file
    with open("quadratic_output.txt", "w") as f:
        f.write("=== Quadratic Equation Solver ===\n")
        f.write(f"Equation     : {a}x^2 + {b}x + {c} = 0\n")
        f.write(f"Discriminant : {discriminant}\n\n")
        f.write(result + "\n")

    # Print to screen
    print("\n=== Quadratic Equation Solver ===")
    print(f"Equation     : {a}x^2 + {b}x + {c} = 0")
    print(f"Discriminant : {discriminant}")
    print(result)
    print("\nResults saved to quadratic_output.txt")


# Ask user for input
print("Solve: ax^2 + bx + c = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

quadratic_solver(a, b, c)