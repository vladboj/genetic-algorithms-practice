import random


# crossover the two parents to create two new children
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)

    offspring = parent1[:crossover_point] + parent2[crossover_point:]

    return offspring
