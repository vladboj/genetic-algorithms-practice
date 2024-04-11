import numpy as np


def fitness(chromosome):
    sum_of_indices = 0
    for i in range(len(chromosome)):
        if chromosome[i] % 2 == 0:
            sum_of_indices += i
    return sum_of_indices


def validate_chromosome(chromosome):
    return 1 not in chromosome[:3]


def generate_population(n):
    population = []

    while len(population) < n:
        chromosome = list(np.random.permutation(5))
        if validate_chromosome(chromosome):
            # To the chromosome append its fitness
            chromosome.append(fitness(chromosome))
            # Append chromosome to population
            population.append(chromosome)

    return population


def main():
    n = int(input("n = "))

    population = generate_population(n)

    # Display maximum fitness
    maximum_fitness = max([chromosome[-1] for chromosome in population])
    print(f"Maximum fitness is {maximum_fitness}")


main()
