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
def set_model_parking(t_lambda, max_left_length, max_right_length, max_total_length, mix_total_length):
    """The optimal parking problem"""
    # ------------------------------------------------------------------------ #
    # Linear problem with minimization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='optimal_parking_problem', sense=LpMinimize)
    # FIXME: it is not always a minimization problem ...

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    X_i=[LpVariable(f'x{i}', lowBound=0, cat=LpBinary) for i in range((len(X_i) - 1) + 1)]
    maxLength=LpVariable(f'maxL', lowBound=0)
    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    prob += lpSum([t_lambda[i] * (X_i[i] + (1 - X_i[i])) for i in range(X_i)]), "Total_parking_length"

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    prob+=lpSum((t_lambda[i]*X_i) for i in range(len(t_lambda)))
    prob+=lpSum(t_lambda[i] * (1-X_i) for i in range(len(t_lambda)))

    return prob, X_i


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_parking_problem():
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # TODO: set data

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob = set_model_parking()
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


if __name__ == '__main__':

    solve_parking_problem()
