import random


def f(xyz):
    x, y, z = xyz
    return round(x ** 2 - 2 * y * z, 2)


def validate_candidate_solution(candidate_solution):
    if sum(candidate_solution) < 10:
        return True
    return False


def generate_possible_solution():
    x = round(random.uniform(-2, 7), 2)
    y = round(random.uniform(-2, 7), 2)
    z = round(random.uniform(-2, 7), 2)

    possible_solution = [x, y, z]
    return possible_solution


def main():
    solutions = []
    while len(solutions) < 20:
        possible_solution = generate_possible_solution()
        if validate_candidate_solution(possible_solution):
            solutions.append(possible_solution)
    for solution in solutions:
        print(f"{solution} -> sum = {f(solution)}")


main()
