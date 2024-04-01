import numpy as np


def fitness(chromosome):
    # Counts the pairs (i, j) i < j for which chromosome[i] - chromosome[j] is even
    counter = 0
    for i in range(len(chromosome) - 1):
        for j in range(i + 1, len(chromosome)):
            if (chromosome[i] - chromosome[j]) % 2 == 0:
                counter += 1
    return counter


def main():
    # Input permutation size from keyboard
    permutation_size = int(input("Enter permutation size: "))

    # Generate population
    population = [list(np.random.permutation(permutation_size)) for _ in range(15)]

    # Append fitness to each chromosome
    for chromosome in population:
        chromosome.append(fitness(chromosome))

    # Create list with the fitness of each chromosome
    fitness_levels = [chromosome[-1] for chromosome in population]

    # Compute and print maximum fitness
    maximum_fitness = max(fitness_levels)
    print(f"Maximum fitness is {maximum_fitness}")


main()
