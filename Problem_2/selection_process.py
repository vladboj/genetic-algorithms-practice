import random
from fitness import fitness


# roulette wheel selection method which returns a champion chromosome :P
def selection_process(population, items, max_weight):
    fitness_levels = [fitness_level for fitness_level in
                      [fitness(chromosome, items, max_weight) for chromosome in population]]
    fitness_sum = sum(fitness_levels)

    # this list represent the probabilities of each chromosome of winning the roulette wheel
    probabilities = [(fitness_level / fitness_sum) for fitness_level in fitness_levels]

    # when the cumulative probability will overtake this random number, the corresponding chromosome will be chosen
    random_number = random.random()

    cumulative_probability = 0
    for i in range(len(probabilities)):
        cumulative_probability += probabilities[i]
        if cumulative_probability >= random_number:
            return population[i]
    return population[-1]
