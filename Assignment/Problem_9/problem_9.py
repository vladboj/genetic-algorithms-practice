import numpy as np


def fitness(chromosome):
    consecutive_equal_pairs = 0
    for i in range(len(chromosome) - 1):
        if chromosome[i] == chromosome[i + 1]:
            consecutive_equal_pairs += 1
    return consecutive_equal_pairs


def main():
    # Input chromosome size
    k = int(input("Enter chromosome size: "))

    # Generate population
    population = []
    for _ in range(10):
        chromosome = [np.random.choice([0, 1]) for _ in range(k)]
        # To each chromosome append its fitness
        chromosome.append(fitness(chromosome))
        population.append(chromosome)

    # Ascendingly sort population based on the fitness of the chromosomes
    population.sort(key=lambda chromosome: chromosome[-1])

    # Display all chromosomes in ascending order of their fitness
    print(population)


main()
