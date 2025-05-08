def calculate_pi_leibniz(iterations):
    approx_pi = 0
    for i in range(iterations):
        # Calculate the current term in the series
        term = (-1) ** i / (2 * i + 1)
        approx_pi += term

    # Multiply by 4 to get an approximation of π
    approx_pi *= 4
    return approx_pi

# Number of iterations to use for the approximation
iterations = int(input("Enter the number of iterations: "))

# Calculate and print the approximation of π
approximation = calculate_pi_leibniz(iterations)
print(f"Approximation of π after {iterations} iterations: {approximation}")
