from selection_process import selection_process


# select two parents using the selection_process method
def get_parents(population, items, max_weight):
    selected_parents = [selection_process(population, items, max_weight),
                        selection_process(population, items, max_weight)]

    return selected_parents
