# in my case, the fitness is the sum of each item's weight
def fitness(chromosome, items, max_weight):
    fitness_level = sum(item for item, gene in zip(items, chromosome) if gene == 1)
    return fitness_level if fitness_level <= max_weight else 0
