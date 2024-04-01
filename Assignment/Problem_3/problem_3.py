import random


def f(x, a):
    return round(sum([x[i] * a[i] for i in range(len(x))]), 2)


def generate_possible_solution():
    possible_solution = [round(random.uniform(-1, 1), 2) for _ in range(10)]
    return possible_solution


def validate_candidate_solution(candidate_solution):
    if sum(candidate_solution[:-1]) == 1 - candidate_solution[-1]:
        return True
    return False


def main():
    # Input list <a> from keyboard
    a = []
    for i in range(10):
        a_element = int(input(f"element {i + 1} = "))
        a.append(a_element)

    solutions = []
    while len(solutions) < 10:
        possible_solution = generate_possible_solution()
        if validate_candidate_solution(possible_solution):
            solutions.append(possible_solution)

    for solution in solutions:
        print(f"f({solution}) = {f(solution, a)}")


main()
