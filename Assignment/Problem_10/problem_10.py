import numpy as np


def f(x, a):
    return round(a * sum(x), 2)


def generate_possible_solution():
    possible_solution = [np.random.choice([-1, 1]) for _ in range(10)]
    return possible_solution


def validate_candidate_solution(candidate_solution):
    if sum(candidate_solution) >= 0:
        return True
    return False


def main():
    # Input "a" from keyboard
    a = int(input("Enter value of 'a': "))
    n = int(input("Enter value of 'n': "))

    # Populate the solutions list
    solutions = []
    while len(solutions) < n:
        possible_solution = generate_possible_solution()
        if validate_candidate_solution(possible_solution):
            solutions.append(possible_solution)

    # Create a list with the fitness of all solutions
    fitness_levels = [f(solution, a) for solution in solutions]

    # Find maximum fitness
    maximum_fitness = max(fitness_levels)

    # Display solution with maximum fitness
    print(f"The maximum fitness is {maximum_fitness}")
    print("Solutions with maximum fitness:")
    for solution in solutions:
        if f(solution, a) == maximum_fitness:
            print(solution)


main()
