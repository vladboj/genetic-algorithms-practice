import numpy as np


def fitness(chromosome):
    integer_value_of_chromosome = 0
    for bit in chromosome:
        integer_value_of_chromosome = (integer_value_of_chromosome << 1) | bit
    return integer_value_of_chromosome


def main():
    # Input number of chromosomes in the population
    n = int(input("Enter number of chromosomes: "))

    # Generate population
    population = []
    for _ in range(n):
        number_of_ones = np.random.randint(0, 4) * 2 + 1
        chromosome = [1] * number_of_ones + [0] * (8 - number_of_ones)
        np.random.shuffle(chromosome)
        population.append(chromosome)

    # Append fitness for each chromosome at the end of it
    for chromosome in population:
        chromosome.append(fitness(chromosome))

    # Find maximum fitness
    maximum_fitness = 0
    for chromosome in population:
        maximum_fitness = max(maximum_fitness, chromosome[-1])

    # Display chromosomes with highest fitness
    for chromosome in population:
        if chromosome[-1] == maximum_fitness:
            print(chromosome)


main()
