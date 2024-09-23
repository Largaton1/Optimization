# -*- coding=utf-8 -*-

# Do not take these comments into consideration
# pylint: disable=too-many-arguments

"""TP2: Admissible cells: array version."""

from pulp import (
    PULP_CBC_CMD,
    LpInteger,
    LpMaximize,
    LpProblem,
    LpStatus,
    LpVariable,
    lpSum,
)
from tp2_setting_input_data import get_adm_cells_data_bis
from tp2_read_data_files import get_adm_cells_data 


# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_admissible_array(ll_adm, l_row_limits, l_col_limits,l_diag_limits):
    """ build the model with arrays """
    # ------------------------------------------------------------------------ #
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='Admissible_cells', sense=LpMaximize)

    # ------------------------------------------------------------------------ #
    # Constants
    # ------------------------------------------------------------------------ #
    n_row, n_col, n_diag = len(l_row_limits), len(l_col_limits), len(l_diag_limits)

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    ll_cells = [
        [
            LpVariable(f'cell_{i}_{j}', lowBound=0, cat=LpInteger)
            for j in range(n_col)
        ] for i in range(n_row)
    ]

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    prob += lpSum(
        ll_adm[i][j] * ll_cells[i][j]
        for i in range(n_row) for j in range(n_col)
    ), 'Total_value'

    # --------------------------he sum of the numbers allocated on the admissible cells on row i should be less or equal tha---------------------------------------------- #
    # The constraints
    # ------------------------------------------------------------------------ #
    for i in range(n_row):
        prob += (
            lpSum(ll_adm[i][j] * ll_cells[i][j] for j in range(n_col))
            <= l_row_limits[i], f'Row_limit_constraints_{i}'
        
        )

    for j in range(n_col) :
        prob+= (
            lpSum(ll_adm[i][j] * ll_cells[i][j] for i in range(n_row))
            <= l_col_limits[j], f'Col_limit_constraints_{j}'
        
        )
        
    for d in range (n_diag) :
        diag_cells = [(i,j) for i in range(n_row) for j in range(n_col) if i+j ==d]        
        prob+= (
            lpSum(ll_adm[i][j] * ll_cells[i][j] for i,j in diag_cells)
            <= l_diag_limits[d], f'Diag_limit_constraints_{j}'
        
        )

    return prob, ll_cells


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_admissible_cells_array(l_adm_cells, l_row_limits, l_col_limits,l_diag_limits):
    """Solve the Admissible Cells problem with an array."""
    # ------------------------------------------------------------------------ #
    # Set input data
    # ------------------------------------------------------------------------ #
    # The array of size m * n:
    m = len(l_row_limits)
    n = len(l_col_limits)
    #  d = len(l_diag_limits)
    #   ll_adm[i][j] = 1 if cells (i, j) is admissible, else 0
    ll_adm = [[0 for _ in range(n)] for _ in range(m)]
    for (i, j) in l_adm_cells:
        ll_adm[i][j] = 1
    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    print('# ------------------- #')
    print('#  MODEL USED: ARRAY  #')
    print('# ------------------- #')

    prob, ll_cells = set_model_admissible_array(
        ll_adm, l_row_limits, l_col_limits,l_diag_limits
    )
    # Coin Branch and Cut solver is used to solve the instanced model
    prob.solve(
        PULP_CBC_CMD(
            msg=False, logPath='./CBC_adm_array.log',
        ),
    )
    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob, ll_cells, ll_adm)


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem, ll_cells, ll_adm):
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
    # Each of the variables is printed with it's resolved optimum value
    print('Admissible cells\tvalues')
    for i, row_i in enumerate(ll_cells):  # we get the ith row
        for j, var_ij in enumerate(row_i):
            if ll_adm[i][j] == 1:
                print(f'{(i, j)}\t\t\t{var_ij.varValue}')


# ============================================================================ #
#                                     MAIN                                     #
# ============================================================================ #
if __name__ == '__main__':
    # for adm_cells, row_limits, col_limits in get_adm_cells_data():
        adm_cells, row_limits, col_limits,diag_limits = get_adm_cells_data_bis()
        solve_admissible_cells_array(adm_cells, row_limits, col_limits,diag_limits)