import random
from get_parents import get_parents
from crossover import crossover
from fitness import fitness

# initialize max weight of my knapsack
max_weight = 10  # my knapsack can hold at max 20kg

# initialize a list of items which can be placed inside the knapsack with their respective weights
items = [2, 3, 5, 7, 10]

population_size = 10
population = [[random.choice([0, 1]) for _ in range(len(items))] for _ in range(population_size)]

# I will take the initial population and create the next generation.
# In order to create the next generation, I have to take <population_size> number of parent chromosomes
# and crossover their genes. After crossing over the genes, I will have to offsprings which
# I will place in the new generation.
# I will continue this pattern until 10000 steps will have finished, and then I will print the
# chromosome with the maximum fitness(aka the best solution)
new_generation = []
for _ in range(10000):
    new_generation = []
    for _ in range(population_size):
        parent1, parent2 = get_parents(population, items, max_weight)
        offspring = crossover(parent1, parent2)
        new_generation.append(offspring)

fitness_levels = [fitness_level for fitness_level in
                  [fitness(chromosome, items, max_weight) for chromosome in population]]

best_chromosome_index = fitness_levels.index(max(fitness_levels))
best_chromosome = new_generation[best_chromosome_index]
best_chromosome_fitness = fitness_levels[best_chromosome_index]

print(f"The best chromosome is {best_chromosome} and it has the fitness of {best_chromosome_fitness}")
