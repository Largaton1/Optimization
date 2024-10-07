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
def set_model_parking(t_lambda):
    """The optimal parking problem"""
    # ------------------------------------------------------------------------ #
    # Linear problem with minimization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='optimal_parking_problem', sense=LpMinimize)

    # ------------------------------------------------------------------------ #
    # The variables
    # Variables: X = 1 if car i is on the left side, 0 if on the right side
    # ------------------------------------------------------------------------ #
    X_i = [LpVariable(f'X_i{i}', cat=LpBinary) for i in range(len(t_lambda))]
    # Longueur totale du côté gauche (Lleft)
    Lleft = lpSum(t_lambda[i] * X_i[i] for i in range(len(t_lambda)))
    # Longueur totale du côté droite (Lright)
    Lright = lpSum(t_lambda[i] * (1-X_i[i]) for i in range(len(t_lambda)))
    # Variable Z: the maximum of the two sides (left and right)
    Z = LpVariable('Z', lowBound=0)

    # ------------------------------------------------------------------------ #
    # The objective function
    # Minimize the total parking length
    # ------------------------------------------------------------------------ #
    prob += Z, "MinimizeMaxSide"
    prob += Z >= Lleft, "Z_GreaterThan_Left"
    prob += Z >= Lright, "Z_GreaterThan_Right"

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # Constraint 1:  the sum of cars’ length parked on the left side should be less than 20 meters;


    # Constraint 2: One of the sides must have at least 16 meters, but not both.

    

    # Constraint 3: cars longer than 4 meters should be parked on left side;

    return prob, X_i

# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_parking_problem():
    """Solve the parking problem."""
    # ------------------------------------------------------------------------ #
    # Set the model with data
    # ------------------------------------------------------------------------ #
    # Sample data: Lengths of cars (example values)
    t_lambda = [4, 4.5, 3, 4.1, 2.4, 4.2, 3.7, 3.5, 3.2, 4.5, 2.3, 3.3, 3.8, 4.6, 3]

    prob, X_i = set_model_parking(t_lambda)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob.solve(PULP_CBC_CMD(msg=True, logPath=Path('./CBC_log.log')))

    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob, X_i, t_lambda)


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem, X_i, t_lambda):
    """Print the log output and problem solutions."""
    print()
    print('-' * 40)
    print('Stats')
    print('-' * 40)
    print(f'Number of variables: {prob.numVariables()}')
    print(f'Number of constraints: {prob.numConstraints()}')
    print()

    print(f'Solution Status: {LpStatus[prob.status]}')
    print(f'Objective value (Z): {prob.objective.value()}')

    print('-' * 40)
    print("Variables' values")
    print('-' * 40)
    for v in prob.variables():
        print(f'{v.name}: {v.varValue}')

    # Calculate the lengths of cars on each side
    Lleft_value = sum(t_lambda[i] * X_i[i].varValue for i in range(len(t_lambda)))
    Lright_value = sum(t_lambda[i] * (1 - X_i[i].varValue) for i in range(len(t_lambda)))

    print('-' * 40)
    print(f'Length of cars on the left side: {Lleft_value}')
    print(f'Length of cars on the right side: {Lright_value}')


if __name__ == '__main__':
    # Solve the problem
    solve_parking_problem()
