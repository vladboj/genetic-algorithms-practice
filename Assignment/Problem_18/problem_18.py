import numpy as np


def f(x):
    return sum(x[:4]) - sum(x[4:])


def validate_chromosome(chromosome):
    return sum(chromosome[:4]) >= sum(chromosome[4:])


def generate_population(n):
    population = []
    while len(population) < n:
        chromosome = [np.random.choice([-1, 1]) for _ in range(8)]
        if validate_chromosome(chromosome):
            chromosome.append(f(chromosome))
            population.append(chromosome)
    return population


def main():
    n = int(input("n = "))

    population = generate_population(n)

    # Display maximum fitness
    maximum_fitness = max([chromosome[-1] for chromosome in population])
    print(f"Maximum fitness is {maximum_fitness}")


main()
