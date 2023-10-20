import math

def main():
    # Number of entries in the table
    num_entries = 1000

    # Calculate the step size for x values
    step_size = 2 / (num_entries - 1)

    # Print table header
    print("x\t\t sin(x)")

    # Generate and print the table
    x = 0
    for _ in range(num_entries):
        sin_x = math.sin(x)
        print(f"{x:.4f}\t\t{sin_x:.4f}")
        x += step_size

if __name__ == "__main__":
    main()