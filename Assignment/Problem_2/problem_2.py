import random


def fitness(chromosome):
    distinct_consecutive_pairs_count = 0
    for i in range(len(chromosome) - 1):
        if chromosome[i] != chromosome[i + 1]:
            distinct_consecutive_pairs_count += 1
    return distinct_consecutive_pairs_count


def generate_chromosome(number_of_genes):
    chromosome = [random.randint(0, 1) for _ in range(number_of_genes)]
    return chromosome


def main():
    POPULATION_SIZE = 18
    NUMBER_OF_GENES = 5
    population = [generate_chromosome(NUMBER_OF_GENES) for _ in range(POPULATION_SIZE)]
    for chromosome in population:
        chromosome.append(fitness(chromosome))

    fitness_levels = [chromosome[-1] for chromosome in population]
    maximum_fitness = max(fitness_levels)
    fittest_chromosomes = [population[i] for i in range(POPULATION_SIZE) if fitness_levels[i] == maximum_fitness]

    print(f"Maximum fitness = {maximum_fitness}")
    print(fittest_chromosomes)


main()
