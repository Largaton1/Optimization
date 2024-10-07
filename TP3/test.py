# -*- coding=utf-8 -*-
from pathlib import Path  # built-in usefull Path class
from pulp import PULP_CBC_CMD, LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Length of each car
lambda_i = {1: 4, 2: 4.5, 3: 3, 4: 4.1, 5: 2.4, 6: 4.2, 7: 3.7, 8: 3.5, 9: 3.2, 10: 4.5,
            11: 2.3, 12: 3.3, 13: 3.8, 14: 4.6, 15: 3}

# Cars longer than 4 meters
long_cars = [i for i, length in lambda_i.items() if length > 4]

def set_model_name():
    """Set up the linear problem."""
    prob = LpProblem(name='parking_problem', sense=LpMinimize)

    # Decision variables for parking each car on the left or right side
    left_vars = {i: LpVariable(f'left_{i}', cat='Binary') for i in range(1, 16)}
    right_vars = {i: LpVariable(f'right_{i}', cat='Binary') for i in range(1, 16)}

    # Objective function: minimize total street length occupied
    prob += lpSum(lambda_i[i] * (left_vars[i] + right_vars[i]) for i in range(1, 16))

    # Constraints:
    # 1. Total length of cars on the left side should be less than 20 meters
    prob += lpSum(lambda_i[i] * left_vars[i] for i in range(1, 16)) <= 20

    # 2. Only one side can have cars occupying 16 meters or more
    prob += lpSum(lambda_i[i] * left_vars[i] for i in range(1, 16)) >= 16 or \
            lpSum(lambda_i[i] * right_vars[i] for i in range(1, 16)) >= 16

    # 3. Cars longer than 4 meters must be parked on the left side
    for i in long_cars:
        prob += left_vars[i] == 1

    # 4. If left side has more than 10 meters, right side must be less than 13 meters
    prob += (lpSum(lambda_i[i] * left_vars[i] for i in range(1, 16)) > 10) >> \
            (lpSum(lambda_i[i] * right_vars[i] for i in range(1, 16)) <= 13)

    return prob

def solve_something():
    """Solve the parking problem."""
    prob = set_model_name()
    prob.solve(
        PULP_CBC_CMD(
            msg=True, logPath=Path('./CBC_log.log'),
        ),
    )
    print_log_output(prob)

def print_log_output(prob: LpProblem):
    """Print the log output and problem solutions."""
    print()
    print('-' * 40)
    print('Stats')
    print('-' * 40)
    print()
    print(f'Number variables: {prob.numVariables()}')
    print(f'Number constraints: {prob.numConstraints()}')
    print()
    print('Time:')
    print(f'- (real) {prob.solutionTime}')
    print(f'- (CPU) {prob.solutionCpuTime}')
    print()
    print(f'Solve status: {LpStatus[prob.status]}')
    print(f'Objective value: {prob.objective.value()}')
    print()
    print('-' * 40)
    print("Variables' values")
    print('-' * 40)
    for var in prob.variables():
        print(f'{var.name} = {var.value()}')

if __name__ == '__main__':
    solve_something()
