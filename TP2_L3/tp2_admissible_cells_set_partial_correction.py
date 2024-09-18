# -*- coding=utf-8 -*-


"""TP2: Admissible cells: set version."""

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
def set_model_admissible_set(st_adm, l_row_limits, l_col_limits,l_diag_limits):
    """build the model with sets  """
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='Admissible_cells', sense=LpMaximize)

    # ------------------------------------------------------------------------ #
    # Constants
    # ------------------------------------------------------------------------ #
    n_row, n_col, n_diag = len(l_row_limits), len(l_col_limits),len(l_diag_limits)

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    d_cells = {
        (i, j): LpVariable(f'cell_{i}_{j}', lowBound=0, cat=LpInteger)
        for (i, j) in st_adm
    }

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    prob += lpSum(d_cells), 'Total_value'

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #

    for j in range(n_col) :
          prob += (
                lpSum(d_cells[(k, l)] for (k,l) in st_adm if l == j)  <= l_col_limits[j], f'Col_limit_constraints_{j}',
          )
          
    for i in range(n_row):
          prob += (
                lpSum(d_cells[(k, l)] for (k,l) in st_adm if k == i)  <= l_row_limits[i], f'Row_limit_constraints_{i}',
          )

    for d in range (n_diag) :
        # diag_cells = {(i,j) for i in range(n_row) for j in range(n_col) if i+j == d}
        #     prob+= (

        #         lpSum(ll_adm[i][j] * ll_cells[i][j] for i,j in diag_cells)

        #         <= l_diag_limits[d], f'Diag_limit_constraints_{d}'

        # )
        prob += (
            lpSum(d_cells[(k, l)] for (k,l) in st_adm if l+k == d)  <= l_diag_limits[d], f'Diag_limit_constraints_{d}',
        )


    return prob, d_cells

#

# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_admissible_cells_set(l_adm_cells, l_row_limits, l_col_limits, l_diag_limits):
    """Solve the Admissible Cells problem with a set."""
    # ------------------------------------------------------------------------ #
    # Set input data
    # ------------------------------------------------------------------------ #
    # The set containing only admissible cells coordinates (i, j)
    st_adm = set(l_adm_cells)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    print('# ----------------- #')
    print('#  MODEL USED: SET  #')
    print('# ----------------- #')

    prob, d_cells = set_model_admissible_set(
        st_adm, l_row_limits, l_col_limits, l_diag_limits
    )
    # Coin Branch and Cut solver is used to solve the instanced model
    prob.solve(
        PULP_CBC_CMD(
            msg=False, logPath='./CBC_adm_set.log',
        ),
    )
    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob, d_cells, len(l_row_limits), len(l_col_limits))


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem, d_cells, n_row: int, n_col: int):
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
    for (i, j) in d_cells:
        print(f'{(i, j)}\t\t\t{d_cells[i, j].varValue}')


# ============================================================================ #
#                                     MAIN                                     #
# ============================================================================ #
if __name__ == '__main__':
    #for adm_cells, row_limits, col_limits in get_adm_cells_data():
    adm_cells, row_limits, col_limits,l_diag_limits = get_adm_cells_data_bis()   
    solve_admissible_cells_set(adm_cells, row_limits, col_limits,l_diag_limits)
