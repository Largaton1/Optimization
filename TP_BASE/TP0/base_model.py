# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""

from pathlib import Path  # built-in usefull Path class

from pulp import PULP_CBC_CMD, LpMaximize, LpProblem, LpStatus


# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_name():
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='name', sense=LpMaximize)
    # FIXME: it is not always a maximization problem ...

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    # TODO: set variables

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # TODO: write the objective function

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # TODO: write constraints

    return prob


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_something():
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # TODO: set data

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob = set_model_name()
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

    solve_something()
