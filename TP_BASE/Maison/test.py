import pulp
from pulp import (
    LpMinimize,
    LpProblem,
    LpVariable,
    lpSum,
    LpStatus,
)
# Paramètres du problème

demandes = [100, 200, 500, 700, 1000, 200, 300]  # demandes pour chaque mois
cout_stockage_par_mois = 4  # coût de stockage par mois
cout_approvisionnement_fixe = 1000  # coût fixe d'approvisionnement
n = len(demandes)  # nombre de mois

# Initialisation du problème
prob = pulp.LpProblem("Optimisation_telecabines", pulp.LpMinimize)

# Variables de décision
commandes = pulp.LpVariable.dicts("Commandes", range (n), lowBound=0, cat='Continuous')

stocks = pulp.LpVariable.dicts("Stocks", range(n+1),lowBound=0, cat='Continuous')
approvisionnement = pulp.LpVariable.dicts("Approvisionnement", range(n), cat='Binary')
# approvisionnement = [pulp.LpVariable(f"Approvisionnement_{i}", lowBound=0, cat='Continuous') for i in range(n)]

# Fonction objectif
prob += pulp.lpSum([cout_stockage_par_mois * stocks [i] for i in range (1, n+1)]) + \
pulp.lpSum ([cout_approvisionnement_fixe* approvisionnement [i] for i in range (n)])

# prob += pulp.lpSum(approvisionnement[i] * cout_approvisionnement_fixe + demandes[i] * cout_stockage_par_mois for i in range(n))

# Contraintes

prob += stocks[0] == 0

for i in range(n):
    prob += stocks[i] + commandes [i] - demandes[i] == stocks[i+1]
    prob += commandes [i] <= 10000 * approvisionnement[i]

    prob += commandes[i] >= 0.0001 *approvisionnement [i]

# Résolution du problème
    prob.solve()
    print()
    print('-' * 40)
    print("Statistiques")
    print()
    print("-" * 40)
    print()
    print(f"Nombre de variables: {len(prob.variables())}")
    print(f"Nombre de contraintes: {len(prob.constraints.values())}")
    print()
    print('Time:')
    print(f'- (real) {prob.solutionTime}')
    print(f'- (CPU) {prob.solutionCpuTime}')
    print()

    print(f'Solve status: {LpStatus[prob.status]}')
    print(f'Objective value: {prob.objective.value()}')

    print(f"Valeur de la stratégie optimale : {pulp.value(prob.objective)}")
    print("Description de la stratégie optimale :")
    print("-" * 83)
    print("| Mois | Approvisionnement | Stock | Commandes | Demandes |")
    print("-" * 83)

    
# Affichage des résultats dans un tableau
    for i in range(n):
        mois = i
        approvisionnement_val = commandes[i].varValue if approvisionnement[i].varValue == 1.0 else 0.0
        stock_val = stocks[i+1].varValue
        commande_val = approvisionnement[i].varValue
        demande_val = demandes[i]
        print(f"| {mois:<4} | {approvisionnement_val:<17} | {stock_val:<5} | {commande_val:<8} | {demande_val:<8} |")

        print("-" * 83)