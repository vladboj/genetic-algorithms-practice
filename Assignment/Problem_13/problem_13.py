import numpy as np


def f(a, solution):
    return round(sum([ai * xi for ai, xi in zip(a, solution)]), 2)


def validate_possible_solution(possible_solution):
    return sum(possible_solution) <= 10


def generate_possible_solution():
    return [round(np.random.uniform(-10, 10), 2) for _ in range(7)]


def main():
    # Get input list as a string
    a_string = input("Enter the input list separated by spaces: ")

    # Convert input list to floats
    a = [float(string_number) for string_number in a_string.split(" ")]

    # Generate solutions
    solutions = []
    while len(solutions) < 10:
        possible_solution = generate_possible_solution()
        if validate_possible_solution(possible_solution):
            solutions.append(possible_solution)

    # Compute maximum fitness
    maximum_fitness = max(f(a, solution) for solution in solutions)

    # Display maximum_fitness along with a solution with maximum fitness
    for solution in solutions:
        if f(a, solution) == maximum_fitness:
            print(f"{solution} -> {maximum_fitness}")
            break


main()
