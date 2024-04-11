import numpy as np


def fitness(chromosome):
    count = 0
    for i in range(len(chromosome) - 1):
        if chromosome[i] == i + 1 and chromosome[i + 1] == i:
            count += 1
    return count


def generate_population(n):
    population = [list(np.random.permutation(7)) for _ in range(n)]
    for i in range(len(population)):
        population[i].append(fitness(population[i]))
    return population


def find_maximum_fitness(population):
    return max([chromosome[-1] for chromosome in population])


def main():
    n = int(input("n = "))

    population = generate_population(n)

    maximum_fitness = find_maximum_fitness(population)
    print(f"Maximum fitness is {maximum_fitness}")


main()
