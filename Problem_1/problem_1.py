import random

n = int(input("Enter an integer larger than 15: "))
numbers = [_ for _ in range(n)]

# First generation of chromosomes
POPULATION_SIZE = 10
population = [random.sample(numbers, len(numbers)) for _ in range(POPULATION_SIZE)]


# This fitness function counts and returns how many neighbors satisfy the condition that x+y>7
def fitness(chromosome):
    condition_satisfied_count = 0
    for i in range(len(chromosome)):
        if i < len(chromosome) - 1:
            if chromosome[i] + chromosome[i + 1] > 7:
                condition_satisfied_count += 1
        elif chromosome[i] + chromosome[0] > 7:
            condition_satisfied_count += 1
    return condition_satisfied_count


# Roulette wheel selection
def selection(generation):
    # Make a list with the fitness of each chromosome in the current generation
    fitness_levels = [fitness(chromosome) for chromosome in generation]
    total_fitness = sum(fitness_levels)

    # The proportion of the total fitness for each chromosome
    fitness_proportions = [(fitness_level / total_fitness) for fitness_level in fitness_levels]

    # When the cumulative probability will overtake this number, the corresponding chromosome will be returned
    random_number = random.random()

    # Create an environment in which the chromosomes with the higher proportion will
    # have a higher probability of being chosen
    cumulative_probability = 0
    for index, fitness_proportion in enumerate(fitness_proportions):
        cumulative_probability += fitness_proportion
        if random_number < cumulative_probability:
            return current_generation[index]
    return current_generation[-1]


def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(1, len(chromosome1) - 1)
    offspring = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    return offspring


current_generation = population
for _ in range(10000):
    improved_generation = []
    for __ in range(POPULATION_SIZE):
        # Create chromosome parents, so I can create a better chromosome offspring
        parent1 = selection(current_generation)
        parent2 = selection(current_generation)
        child = crossover(parent1, parent2)
        improved_generation.append(child)
    current_generation = improved_generation

# The chromosome with the highest fitness from the current generation
best_chromosome_index = max(chromosome_index for chromosome_index, chromosome in enumerate(current_generation))
best_chromosome = current_generation[best_chromosome_index]

print(f"{best_chromosome} -> {fitness(best_chromosome)}")
