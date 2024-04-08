import numpy as np


def fitness(chromosome):
    counter = 0
    for i in range(len(chromosome)):
        if chromosome[i - 1] + chromosome[i] > 7:
            counter += 1
    return counter


def select(current_generation):
    fitness_levels = [fitness(chromosome) for chromosome in current_generation]
    total_fitness = sum(fitness_levels)

    probabilities_of_being_chosen = [fitness_level / total_fitness for fitness_level in fitness_levels]

    random_probability = np.random.random()

    cumulative_probability = 0
    for i in range(len(current_generation)):
        cumulative_probability += probabilities_of_being_chosen[i]
        if random_probability <= cumulative_probability:
            return current_generation[i]
    return current_generation[-1]


def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    return parent1[:crossover_point] + parent2[crossover_point:]


def mutate(unmutated_child, input_list):
    mutated_child = []

    mutation_rate = 0.1

    for gene in unmutated_child:
        random_probability = np.random.random()
        if random_probability <= mutation_rate:
            mutated_child.append(np.random.choice(input_list))
        else:
            mutated_child.append(gene)

    return mutated_child


def main():
    # Get input
    n = int(input("Enter a value larger than 15: "))
    input_list = []
    for i in range(n):
        input_element = int(input(f"input_list[{i}] = "))
        input_list.append(input_element)

    # Generate initial generation
    current_generation = [list(np.random.permutation(input_list)) for _ in range(10)]

    # Run genetic algorithm for 10 thousand iterations
    for _ in range(10000):
        improved_generation = []
        for _ in range(n):
            parent1 = select(current_generation)
            parent2 = select(current_generation)
            unmutated_child = crossover(parent1, parent2)
            child = mutate(unmutated_child, input_list)
            improved_generation.append(child)
        current_generation = improved_generation

    # Find the best chromosome in the last generation
    fitness_levels = [fitness(chromosome) for chromosome in current_generation]
    maximum_fitness = max(fitness_levels)
    best_chromosome_index = fitness_levels.index(maximum_fitness)
    best_chromosome = current_generation[best_chromosome_index]

    # Display best chromosome
    print(f"Best chromosome is {best_chromosome} with a fitness of {maximum_fitness}")


main()
