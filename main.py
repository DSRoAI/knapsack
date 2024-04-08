from utils import read_testcase, write_testcase_csv, write_testcase_txt, get_filepath
from ortools.algorithms.python import knapsack_solver
import random
import time

def run_solver(values: list, weights: list, capacity: int, time_limit = 180):
    
    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    solver.init(values, [weights], [capacity])
    solver.set_time_limit(time_limit)
    start_time = time.time()
    computed_value = solver.solve()
    end_time = time.time()
    packed_items = []
    packed_weights = []
    total_weight = 0
    is_optimal = (end_time - start_time) <= time_limit - 1
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[i])
            total_weight += weights[i]
    '''
    print("Computed value:", computed_value)
    print("Total weight:", total_weight)
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)
    '''
    return computed_value, total_weight, packed_items, packed_weights, is_optimal

def main():
    testcase_path_lst = get_filepath()
    excecute_testcase_lst = [] 
    for group in testcase_path_lst:
        random_testcase_lst = random.sample(group, 5)
        excecute_testcase_lst += random_testcase_lst

    for id, testcase_path in enumerate(excecute_testcase_lst):
        number_of_items, capacity, values, weights = read_testcase(testcase_path)
        computed_value, total_weight, packed_items, packed_weights, is_optimal = run_solver(values, weights, capacity)
        write_testcase_csv(testcase_path, computed_value, total_weight, is_optimal, id)
        write_testcase_txt(testcase_path, computed_value, total_weight, packed_items, packed_weights, id)
        print(f'Filepath: {testcase_path}')
        print(f'Computed Value: {computed_value}')
        print(f'Total Weight: {total_weight}')
        print(f'Is Optimal: {is_optimal}')
        print('--------------------------------------')

if __name__ == '__main__':
    main()