import random


def crossover(chromosome1, chromosome2):
    # Randomly generate a crossover point where I will combine the genes of the chromosomes
    # to create an offspring
    crossover_point = random.randint(1, len(chromosome1) - 1)

    # Crossover the genes
    offspring = chromosome1[:crossover_point] + chromosome2[crossover_point:]

    return offspring
