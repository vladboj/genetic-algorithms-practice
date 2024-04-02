import numpy as np


def fitness(chromosome):
    return np.prod(chromosome)


def main():
    # Input number of chromosomes
    n = int(input("Enter number of chromosomes: "))

    # Generate population and append fitness to each chromosome
    population = []
    for _ in range(n):
        chromosome = [np.random.randint(1, 5) for _ in range(4)] + [np.random.choice([1, 3])] + [np.random.randint(1, 5)
                                                                                                 for _ in range(3)]
        chromosome.append(fitness(chromosome))
        population.append(chromosome)

    # Find minimum fitness
    minimum_fitness = float('inf')
    for chromosome in population:
        minimum_fitness = min(minimum_fitness, chromosome[-1])

    # Display chromosomes with lowest fitness
    for chromosome in population:
        if chromosome[-1] == minimum_fitness:
            print(chromosome)


main()
