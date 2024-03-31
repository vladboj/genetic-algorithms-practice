from fitness import fitness
import random


# Roulette wheel selection
def selection(population):
    # List of the fitness of each chromosome in the population
    fitness_levels = [fitness(chromosome) for chromosome in population]

    # Sum of the fitness of all chromosomes
    total_fitness = sum(fitness_levels)

    # If all chromosomes are unfeasible, I will return one of them at random
    if total_fitness == 0:
        return population[random.randint(0, len(population) - 1)]

    # Proportion of each chromosome's fitness from the total fitness
    fitness_proportions = [(fitness_level / total_fitness) for fitness_level in fitness_levels]

    # When the cumulative proportion overtakes this number, the respective chromosome will be returned
    random_number = random.random()

    # This method of choosing a chromosome attributes the highest chance of being chosen
    # to the chromosome that is the fittest because it covers the largest area of the cumulative
    # proportion and so the random number was most probable to be contained within that interval
    cumulative_proportion = 0
    for i in range(len(fitness_proportions)):
        cumulative_proportion += fitness_proportions[i]
        if cumulative_proportion > random_number:
            return population[i]
    return population[-1]
