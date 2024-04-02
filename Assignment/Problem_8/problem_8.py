import numpy as np


def fitness(chromosome):
    return sum(abs(gene) for gene in chromosome)


def main():
    # Input chromosome size
    k = int(input("Enter chromosome size: "))

    # Generate population
    population = []
    for _ in range(10):
        chromosome = list(np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k))
        while sum(chromosome) <= 0:
            chromosome = list(np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k))
        # To each chromosome append its fitness
        chromosome.append(fitness(chromosome))
        population.append(chromosome)

    # Find minimum fitness
    minimum_fitness = min([chromosome[-1] for chromosome in population])

    # Display the least fit chromosomes
    for chromosome in population:
        if chromosome[-1] == minimum_fitness:
            print(chromosome)


main()
