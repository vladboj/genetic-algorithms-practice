import numpy as np


def fitness(chromosome):
    return abs(np.prod(chromosome))


def validate_chromosome(chromosome):
    return sum(chromosome) < 10


def generate_population():
    population = []

    while len(population) < 10:
        chromosome = list(np.random.choice(list(range(-2, 5)), size=6))
        if validate_chromosome(chromosome):
            # To the chromosome append its fitness
            chromosome.append(fitness(chromosome))
            # Append chromosome to the population
            population.append(chromosome)

    return population


def main():
    population = generate_population()

    population.sort(key=lambda chromosome: chromosome[-1], reverse=True)

    for chromosome in population:
        print(f"{chromosome[:-1]} -> {chromosome[-1]}")


main()
