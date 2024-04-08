import numpy as np


def fitness(solution):
    counter = 0
    for i in range(len(solution)):
        if solution[i] < i:
            counter += 1
    return counter


def main():
    # Get input
    k = int(input("Enter value of k: "))

    # Generate population
    solutions = []
    while len(solutions) < 10:
        possible_solution = list(np.random.permutation(k))
        if possible_solution[0] == 0 and possible_solution[k - 1] == k - 1:
            solutions.append(possible_solution)

    # To each solution append its fitness
    for i in range(len(solutions)):
        solutions[i].append(fitness(solutions[i]))

    # Compute maximum fitness
    maximum_fitness = max([solution[-1] for solution in solutions])

    # Display maximum fitness
    print(f"Maximum fitness is {maximum_fitness}")


main()
