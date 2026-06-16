# Moyenne des âges
def moyenne_ages(patients):
    total = 0
    if not patients:
        return 0
    for p in patients:
        total += p["age"]
    return total / len(patients)


# Moyenne des poids
def moyenne_poids(patients):
    total = 0
    if not patients:
        return 0
    for p in patients:
        total += p["poids"]
    return total / len(patients)


# Ville la plus fréquente
def ville_plus_frequente(patients):
    compteur = {}
    for p in patients:
        ville = p["ville"]
        if ville in compteur:
            compteur[ville] += 1
        else:
            compteur[ville] = 1
    return max(compteur, key=compteur.get)


# Répartition des groupes sanguins
def repartition_groupes_sanguins(patients):
    compteur = {}
    for p in patients:
        groupe = p["groupe_sanguin"]
        if groupe in compteur:
            compteur[groupe] += 1
        else:
            compteur[groupe] = 1
    return compteur

# Affichage des statistiques
def afficher_statistiques(patients, nb_total_brut, nb_doublons, nb_rejetes):
    print("="*40)
    print("STATISTIQUES")
    print("="*40)
    print(f"Nombre total de patients (fichier brut) : {nb_total_brut}")
    print(f"Nombre de patients valides : {len(patients)}")
    print(f"Nombre de doublons supprimés : {nb_doublons}")
    print(f"Nombre de lignes rejetées : {nb_rejetes}")
    print(f"Moyenne des âges : {moyenne_ages(patients):.2f}")
    print(f"Moyenne des poids : {moyenne_poids(patients):.2f}")
    print(f"Ville la plus fréquente : {ville_plus_frequente(patients)}")
    print("Répartition des groupes sanguins :")
    repartition = repartition_groupes_sanguins(patients)
    for groupe, nombre in repartition.items():
        print(f"  {groupe} : {nombre}")