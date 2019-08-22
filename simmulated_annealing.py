import math
from random import randrange, random, uniform

##
# Se equação de 2º grau, duas threads, cada uma procurando uma solução?


def choose_random_solution():
    a = -50
    b = 50
    result = randrange(a, b)
    return result


def calculate_cost(expression, solution):
    cost = eval(expression, dict(x=solution))
    return cost


def compare_solutions(expression, neighbor, current):
    neighbor_cost = calculate_cost(expression, neighbor)
    current_cost = calculate_cost(expression, current)
    return neighbor_cost - current_cost


def will_update_solution(delta, temperature):
    is_better_solution = delta <= 0
    calc_1 = uniform(0, abs(delta))
    try:
        calc_2 = math.exp(-delta/temperature)
        random_update = calc_1 > calc_2
    except (OverflowError, ZeroDivisionError):
        random_update = False
    return is_better_solution or random_update


def simmulated_annealing(
    expression, initial_solution, initial_temperature,
    cooling_factor, number_of_solutions_to_test
):
    current_solution = initial_solution
    temperature = initial_temperature
    for i in range(1, number_of_solutions_to_test):
        neighbor_solution = choose_random_solution()
        delta = compare_solutions(expression, neighbor_solution, current_solution)
        if will_update_solution(delta, temperature):
            current_solution = neighbor_solution
        temperature = temperature * cooling_factor

        # Se achou a solução ideal, para o algoritmo
        if calculate_cost(expression, current_solution) == 0:
            break

    return current_solution


def main():
    # TODO: Informar esses dados via args para a função
    solution = simmulated_annealing(
        expression="2 * x - 10",
        initial_solution=10,
        initial_temperature=1000,
        cooling_factor=0.001,
        number_of_solutions_to_test=1000
    )

    print("Solução: ", solution)


if __name__ == "__main__":
    main()
