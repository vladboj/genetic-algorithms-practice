import numpy as np


def fitness(chromosome):
    number_of_ones_at_odd_positions = 0
    for i in range(len(chromosome)):
        if i % 2 == 0 and chromosome[i] == 1:  # I check if "i" is even because of the problem statement
            number_of_ones_at_odd_positions += 1
    return number_of_ones_at_odd_positions


def main():
    # Generate population
    population = [[np.random.choice([0, 1]) for _ in range(7)] for _ in range(10)]

    # To each chromosome of the population, append its fitness
    for i in range(len(population)):
        population[i].append(fitness(population[i]))

    # Compute average fitness
    average_fitness = np.average([chromosome[-1] for chromosome in population])

    # Display average fitness
    print(f"Average fitness is {average_fitness}")


main()
