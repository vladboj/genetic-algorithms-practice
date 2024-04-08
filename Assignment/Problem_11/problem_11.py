import numpy as np


def f(solution):
    return round(solution[-1] * solution[0] ** 2 - 2 * solution[1] * solution[2], 2)


# Check the given constraint
def validate_possible_solution(possible_solution):
    return possible_solution[-1] == possible_solution[0] + possible_solution[1] - possible_solution[2]


# Generate list of 4 random real number between -2 and 2
def generate_possible_solution():
    return [round(np.random.uniform(-2, 2), 2) for _ in range(4)]


def main():
    # Get keyboard input
    n = int(input("Enter number of solutions to be generated: "))

    # Generate solutions
    solutions = []
    while len(solutions) < n:
        possible_solution = generate_possible_solution()
        if validate_possible_solution(possible_solution):
            solutions.append(possible_solution)

    # Compute maximum fitness
    maximum_fitness = max([f(solution) for solution in solutions])

    # Display maximum fitness
    print(f"Maximum fitness is {maximum_fitness}")

main()
