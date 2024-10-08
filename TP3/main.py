# -*- coding=utf-8 -*-
"""Optimal Parking Problem Model Using PuLP."""
#authors: Cyril KONE & Loic Nassara
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
    #Variable Z: the maximum of the two sides (left and right)
    Z = LpVariable('Z', lowBound=0)

    # ------------------------------------------------------------------------ #
    # The objective function
    # Minimize the total parking length
    # ------------------------------------------------------------------------ #
    prob += Z, "Minimise le maximum de chaque coté"
    prob += Z >= Lleft, "Z plus grand à gauche"
    prob += Z >= Lright, "Z plus grand à droite"

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # Constraint 1:  the sum of cars’ length parked on the left side should be less than 20 meters;
    prob += Lleft <= 20
    # Constraint 2: cars are allowed to occupy more or equal to 16m on no more than one of the street sides;
    prob += Lleft >= 16, "Plus de 16m sur le coté gauche"
    prob += Lright <= 16, "Moins de 16m sur le coté droit ou égale"
    prob += Lleft + Lright >= 16
    
    # Constraint 3: cars longer than 4 meters should be parked on left side;
    for i in range(len(t_lambda)):
        if t_lambda[i] > 4:
            prob += X_i[i] == 1

    #Constraint 4: if the length of the left side is larger than 10 meters, the length of the rightside should be smaller than 13 meters.
    M = 1000  # Big contrainte M
    Y = LpVariable("Y", cat=LpBinary)
    prob += Lleft <= 10 + M * Y, "10m comme limite à gauche"
    prob += Lright <= 13 + M * (1 - Y), "13m comme limite à droite"
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
    print('-' * 40)
    print("Variables' values")
    print('-' * 40)
    for v in prob.variables():
        print(f'{v.name}: {v.varValue}')

    # Calculate the lengths of cars on each side
    Lleft_value = sum(t_lambda[i] * X_i[i].varValue for i in range(len(t_lambda)))
    Lright_value = sum(t_lambda[i] * (1 - X_i[i].varValue) for i in range(len(t_lambda)))

    print('-' * 40)
    print(f'La longueur de la voiture sur le coté gauche: {Lleft_value}')
    print(f'La longueur de la voiture sur le coté droit: {Lright_value}')


if __name__ == '__main__':
    # Solve the problem
    solve_parking_problem()
