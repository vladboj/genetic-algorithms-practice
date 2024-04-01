import random
from selection import selection
from crossover import crossover
from fitness import fitness

# The solution to this problem will be represented as an array of 3 elements,
# these 3 elements being the amount invested in each security

# I want each generation of possible solutions(chromosomes) to have 10 possible solutions
POPULATION_SIZE = 10
# Generate 10 lists of 3 elements, each element being between 0 and 80000
initial_population = [[random.randint(0, 80000) for _ in range(3)] for __ in range(10)]

current_generation = initial_population
for _ in range(10000):
    improved_generation = []
    for __ in range(POPULATION_SIZE):
        parent1 = selection(current_generation)
        parent2 = selection(current_generation)
        child = crossover(parent1, parent2)
        improved_generation.append(child)
    current_generation = improved_generation

# Find the best chromosome of the last generation
fitness_levels = [fitness(chromosome) for chromosome in current_generation]
best_chromosome_index = fitness_levels.index(max(fitness_levels))
best_chromosome = current_generation[best_chromosome_index]

print(f"{best_chromosome} -> {fitness_levels[best_chromosome_index]}")
