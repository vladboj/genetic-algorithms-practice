import random
from selection import selection
from crossover import crossover
from fitness import fitness

matrix_order = int(input("Enter number of rows and columns of the matrix: "))
number_of_objects = int(input("Enter the number of objects: "))

# A possible solution will be represented as list of pairs, where a pair
# represent the coordinates of an object in the matrix
# The initial population will be a list of possible solutions
POPULATION_SIZE = 10
initial_population = []
for _ in range(POPULATION_SIZE):
    possible_solution = []
    for __ in range(number_of_objects):
        random_index_1 = random.randint(0, matrix_order - 1)
        random_index_2 = random.randint(0, matrix_order - 1)
        possible_solution.append((random_index_1, random_index_2))
    initial_population.append(possible_solution)

current_generation = initial_population
for _ in range(1000):
    improved_generation = []
    for __ in range(POPULATION_SIZE):
        parent1 = selection(current_generation)
        parent2 = selection(current_generation)
        child = crossover(parent1, parent2)
        improved_generation.append(child)
    current_generation = improved_generation

fitness_levels = [fitness(chromosome) for chromosome in current_generation]

best_chromosome_index = fitness_levels.index(max(fitness_levels))
best_chromosome = current_generation[best_chromosome_index]

print(f"{best_chromosome} -> {fitness_levels[best_chromosome_index]}")
