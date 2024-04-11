import numpy as np


def fitness(chromosome):
    return np.prod(chromosome)


def generate_population(k):
    population = []

    possible_values = list(range(1, 7))

    for _ in range(10):
        chromosome = list(np.random.choice(possible_values, size=k))
        if chromosome[-1] % 2 == 1:
            chromosome[-1] += 1
        # To each chromosome append its fitness
        chromosome.append(fitness(chromosome))
        # Append chromosome to population
        population.append(chromosome)

    return population


def main():
    k = int(input("k = "))

    population = generate_population(k)
    population.sort(key=lambda chromosome: chromosome[-1])

    for chromosome in population:
        print(f"{chromosome[:-1]} -> {chromosome[-1]}")


main()
