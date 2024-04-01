import random


def f(xyz):
    x, y, z = xyz
    return x ** 2 - 2 * y * z


def validate_candidate_solution(candidate_solution):
    if sum(candidate_solution) < 10:
        return True
    return False


def generate_possible_solution():
    x = random.uniform(-2, 7)
    y = random.uniform(-2, 7)
    z = random.uniform(-2, 7)

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
