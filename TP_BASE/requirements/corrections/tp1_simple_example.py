# -*- coding=utf-8 -*-


"""TP1 - A simple example."""


from pathlib import Path  # built-in usefull Path class

from pulp import (
    PULP_CBC_CMD,
    LpMinimize,
    LpProblem,
    LpStatus,
    LpVariable,
    lpSum,
)


# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_diet(t_cost, t_calories, t_chocolate, t_sugar, t_fat, t_demands):
    """Set the diet problem's model."""
    # ------------------------------------------------------------------------ #
    # Linear problem with minimization
    # ------------------------------------------------------------------------ #
    # `prob` is a linear minimization problem
    prob = LpProblem(name='The_diet_problem', sense=LpMinimize)

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    # The list of `x_i` variables
    #   `x_i` = the quantities of food `i`
    qty_foods = [LpVariable(f'x_{i}', lowBound=0) for i in range(len(t_cost))]

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # We add to the problem variable `prob` the objective function which is
    #   a sum representing the total cost
    #   `lpSum()` is a PuLP function, explaining the module caller `pl.`
    prob += lpSum(
        t_cost[i] * food for i, food in enumerate(qty_foods)
    ), 'Totat_cost'

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # We add to the problem the constraints which are inequations here :
    #   we want to respect at least (>=) the nutrition demands
    prob += (
        lpSum(t_calories[i] * food for i, food in enumerate(qty_foods))
        >= t_demands[0], 'Calories_constraints',
    )

    prob += (
        lpSum(t_chocolate[i] * food for i, food in enumerate(qty_foods))
        >= t_demands[1], 'Chocolate_constraints',
    )

    prob += (
        lpSum(t_sugar[i] * food for i, food in enumerate(qty_foods))
        >= t_demands[2], 'Sugar_constraints',
    )

    prob += (
        lpSum(t_fat[i] * food for i, food in enumerate(qty_foods))
        >= t_demands[3], 'Fat_constraints',
    )

    # Return the problem variable and the list of linear variables
    return prob, qty_foods


# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #
def solve_simple_example():
    """Solve the simple example."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # The cost of each food
    t_cost = (50, 20, 30, 80)
    # The nutrition coefficients for each food
    t_calories = (400, 200, 150, 500)
    t_chocolate = (3, 2, 0, 0)
    t_sugar = (2, 2, 4, 4)
    t_fat = (2, 4, 1, 5)
    # The nutrition demands
    t_demands = (500, 6, 10, 8)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    # Get the problem and the list containing the linear variables
    prob, qty_foods = set_model_diet(
        t_cost, t_calories, t_chocolate, t_sugar, t_fat, t_demands,
    )

    # After solving, a `.log` file is written.
    #   Some solver stats are written in it
    prob.solve(
        PULP_CBC_CMD(
            msg=False, logPath=Path('./CBC_simple_ex.log'),
        ),
    )
    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print_log_output(prob, qty_foods)


# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #
def print_log_output(prob: LpProblem, qty_foods):
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
    print('NUM FOOD\tFOOD QUANTITIES')
    for num_food, lpvar in enumerate(qty_foods):
        # `varValue` is a LpVariable instance attribute.
        #   You can access to it with a `.`
        #   It corresponds to the variable value after solving
        food_qty = lpvar.varValue
        print(f'{num_food}\t\t{food_qty}')


if __name__ == '__main__':

    solve_simple_example()
