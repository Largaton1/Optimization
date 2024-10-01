# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""

from pathlib import Path  # built-in usefull Path class

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
    # FIXME: it is not always a minimization problem ...

    # ------------------------------------------------------------------------ #
    # The variables
    # Variables: x_i = 1 if car i is on the left side, 0 if on the right side
    # ------------------------------------------------------------------------ #
    X_i = [LpVariable(f'X_i{i}', lowBound=0, cat=LpBinary) for i in range(len(t_lambda))]

    max_left_length=LpVariable(f'maxLeft', lowBound=0)
    max_right_length=LpVariable(f'maxRight', lowBound=0)
    max_total_length=LpVariable(f'maxTotal', lowBound=0)
    min_total_length=LpVariable(f'minTotal', lowBound=0)
    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    prob += lpSum([t_lambda[i] for i in range(len(t_lambda))]), "Total_parking_length"

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #

    # Constraint 1: Length on the left side <= max_left_length
    prob += lpSum([t_lambda[i] * X_i[i] for i in range(len(t_lambda))]) <= max_left_length, "Left_side_limit"

    # Constraint 2: Length on the right side <= max_right_length
    prob += lpSum([t_lambda[i] * (1 - X_i[i]) for i in range(len(t_lambda))]) <= max_right_length, "Right_side_limit"

    # Constraint 3: Total length parked <= max_total_length
    prob += lpSum([t_lambda[i] for i in range(len(t_lambda))]) <= max_total_length, "Max_total_length"

    # Constraint 4: Total length parked >= min_total_length
    prob += lpSum([t_lambda[i] for i in range(len(t_lambda))]) >= min_total_length, "Min_total_length"


    return prob, X_i


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_parking_problem(t_lambda, max_left_length, max_right_length, max_total_length, mix_total_length):
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    prob, X_i = set_model_parking(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob = set_model_parking(t_lambda, max_left_length, max_right_length, max_total_length, mix_total_length)
    # Coin Branch and Cut solver is used to solve the instanced model
    # TODO: change the log path file
    prob.solve(
        PULP_CBC_CMD(
            msg=False, logPath=Path('./CBC_log.log'),
        ),
    )
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
    print()
    # TODO: you can print variables value here
    for v in prob.variables():
        print(f'{v.name}: {v.varValue}')

if __name__ == '__main__':
    t_lambda = [10, 15, 20, 25]  # Example car lengths
    max_left_length = 50
    max_right_length = 50
    max_total_length = 150
    min_total_length = 100

    solve_parking_problem(t_lambda, max_left_length, max_right_length, max_total_length, min_total_length)
