import numpy as np


def fitness(chromosome):
    good_pairs_count = 0
    for i in range(len(chromosome) - 1):
        for j in range(i + 1, len(chromosome)):
            if chromosome[i] == j and chromosome[j] == i:
                good_pairs_count += 1
    return good_pairs_count


def main():
    # Input number of chromosomes
    n = int(input("Enter number of chromosomes:"))

    # Generate population
    population = [list(np.random.permutation(8)) for _ in range(n)]

    # Append the fitness for each chromosome
    for chromosome in population:
        chromosome.append(fitness(chromosome))

    # Find maximum fitness
    maximum_fitness = 0
    for chromosome in population:
        maximum_fitness = max(maximum_fitness, chromosome[-1])

    # Display chromosomes with maximum fitness
    for chromosome in population:
        if chromosome[-1] == maximum_fitness:
            print(chromosome)


main()
