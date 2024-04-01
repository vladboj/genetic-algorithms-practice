import random


def f(x, y, z):
    return x ** 2 - 2 * y * z


def validate_candidate_solution(candidate_solution):
    if sum(candidate_solution) < 10:
        return True
    return False


def generate_possible_solution():
    x = random.randint(-2, 7)
    y = random.randint(-2, 7)
    z = random.randint(-2, 7)

    possible_solution = [x, y, z]
    return possible_solution


def main():
    possible_solutions = []
    while len(possible_solutions) < 20:
        possible_solution = generate_possible_solution()
        if validate_candidate_solution(possible_solution):
            possible_solutions.append(possible_solution)
    for possible_solution in possible_solutions:
        print(f"{possible_solution} -> sum = {sum(possible_solution)}")


main()
