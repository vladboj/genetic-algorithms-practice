import numpy as np


def fitness(chromosome):
    # Sum the indices of the genes with the value of 1
    sum_of_indices = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            sum_of_indices += i
    return sum_of_indices


def generate_population(n):
    population = []
    for _ in range(n):
        chromosome = [1] * 5 + [0] * 4
        np.random.shuffle(chromosome)
        # To each chromosome append its fitness
        chromosome.append(fitness(chromosome))
        # Add chromosome to population
        population.append(chromosome)
    return population


def main():
    n = int(input("n = "))
    population = generate_population(n)

    # Display chromosomes along with their fitness
    for chromosome in population:
        print(f"{chromosome[:-1]} -> {chromosome[-1]}")


main()
