# -*- coding=utf-8 -*-
"""Optimal Parking Problem Model Using PuLP."""

from pathlib import Path  # built-in useful Path class
from pulp import (
    PULP_CBC_CMD,
    LpMinimize,
    LpProblem,
    LpStatus,
    LpVariable,
    lpSum,
    LpBinary,
)

# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_parking(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length):
    """The optimal parking problem"""
    # ------------------------------------------------------------------------ #
    # Linear problem with minimization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='optimal_parking_problem', sense=LpMinimize)

    # ------------------------------------------------------------------------ #
    # The variables
    # Variables: X = 1 if car i is on the left side, 0 if on the right side
    # ------------------------------------------------------------------------ #
    X_i = [LpVariable(f'X_i{i}', cat=LpBinary) for i in range(1, len(t_lambda) + 1)]
    # Longueur totale du côté gauche (Lleft)
    Lleft = lpSum(t_lambda[i] * X_i[i] for i in range(1, len(t_lambda) + 1))
    # Longueur totale du côté droite (Lright)
    Lright = lpSum(t_lambda[i] * (1-X_i[i]) for i in range(len(t_lambda) + 1))
    #Longueur totale des voitures garées
    Ltotal = lpSum(t_lambda[i] for i in range(1, len(t_lambda) + 1))

    # ------------------------------------------------------------------------ #
    # The objective function
    # Minimize the total parking length
    # ------------------------------------------------------------------------ #
    prob += Lleft + Lright, "Total_parking_length"

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #

    # Constraint 1:  the sum of cars’ length parked on the left side should be less than 20 meters;
    prob += Lleft <= 20

    # Constraint 2: cars are allowed to occupy more or equal to 16m on no more than one of the street sides

    over_left = Lleft >= 16
    over_right = Lright >= 16
    prob += over_left + over_right <= 1

    # Constraint 3: cars longer than 4 meters should be parked on left side;
    for i in range(1, len(t_lambda) + 1):
        if t_lambda[i] > 4:
            prob += X_i[i] == 1

    # Constraint 4:  if the length of the left side is larger than 10 meters, the length of the right side should be smaller than 13 meters.

    M = 1000  # Big M
    prob += Lright <= 13 + M * (1 - (Lleft > 10))

    return prob, X_i


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_parking_problem(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length):
    """Solve the parking problem."""
    # ------------------------------------------------------------------------ #
    # Set the model with data
    # ------------------------------------------------------------------------ #
    prob, X = set_model_parking(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob.solve(PULP_CBC_CMD(msg=True, logPath=Path('./CBC_log.log')))

    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob)


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem):
    """Print the log output and problem solutions."""
    print()
    print('-' * 40)
    print('Stats')
    print('-' * 40)
    print(f'Number of variables: {prob.numVariables()}')
    print(f'Number of constraints: {prob.numConstraints()}')
    print()

    print(f'Solution Status: {LpStatus[prob.status]}')
    print(f'Objective value: {prob.objective.value()}')

    print('-' * 40)
    print("Variables' values")
    print('-' * 40)
    for v in prob.variables():
        print(f'{v.name}: {v.varValue}')


if __name__ == '__main__':
    # Sample data: Lengths of cars (example values)
    t_lambda = [4, 4.5, 3, 4.1, 2.4, 4.2, 3.7, 3.5, 3.2, 4.5, 2.3, 3.3, 3.8, 4.6, 3]

    # Constraints on parking lengths
    max_left_length = 20  # Maximum length allowed on the left side
    max_right_length = 20  # Maximum length allowed on the right side
    max_total_length = 50  # Maximum total length for all cars
    min_total_length = 30  # Minimum total length for all cars

    # Solve the problem
    solve_parking_problem(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length)
