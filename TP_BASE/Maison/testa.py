import pulp

# Paramètres du problème
demandes = [100, 200, 500, 700, 1000, 200]  # demandes pour chaque mois
cout_stockage_par_mois = 4  # coût de stockage par mois
cout_approvisionnement_fixe = 1000  # coût fixe d'approvisionnement
n = len(demandes)  # nombre de mois

# Initialisation du problème
prob = pulp.LpProblem("Optimisation_telecabines", pulp.LpMinimize)

# Variables de décision
commandes = pulp.LpVariable.dicts("Commande", range(n), lowBound=0, cat='Continuous')
stocks = pulp.LpVariable.dicts("Stock", range(n+1), lowBound=0, cat='Continuous')
approvisionnement = pulp.LpVariable.dicts("Approvisionnement", range(n), cat='Binary')

# Fonction objectif
prob += pulp.lpSum(cout_stockage_par_mois * stocks[i] for i in range(1, n+1)) + \
        pulp.lpSum(cout_approvisionnement_fixe * approvisionnement[i] for i in range(n))

# Contraintes
prob += stocks[0] == 0

for i in range(n):
    prob += stocks[i] + commandes[i] - demandes[i] <= stocks[i+1]
    prob += commandes[i] <= 10000 * approvisionnement[i]
    prob += commandes[i] >= 0.0001 * approvisionnement[i]

# Proposition du directeur des achats : approvisionnement en début du premier mois
prob += approvisionnement[0] == sum(demandes)

# Proposition du directeur financier : approvisionnement au début de chaque mois
for i in range(1, n):
    prob += approvisionnement[i] >= demandes[i]

# Résolution du problème
prob.solve()

# Affichage de la valeur optimale du coût total
print("Statistiques")
print("-" * 40)
print(f"Nombre de variables: {len(prob.variables())}")
print(f"Nombre de contraintes: {len(prob.constraints.values())}")

# Affichage des resultats
print(f"Valeur de la stratégie optimale : {pulp.value(prob.objective)}")
print("Description de la stratégie optimale :")
print("-" * 83)
print("| Mois | Approvisionnement | Stock | Commande | Demandes |")
print("-" * 83)

# Affichage des résultats dans un tableau
for i in range(n):
    mois = i
    approvisionnement_val = commandes[i].varValue if approvisionnement[i].varValue == 1.0 else 0.0
    stock_val = stocks[i+1].varValue
    commande_val = commandes[i].varValue
    demande_val = demandes[i]
    print(f"| {mois:<4} | {approvisionnement_val:<17} | {stock_val:<5} | {commande_val:<8} | {demande_val:<8} |")

print("-" * 83)
