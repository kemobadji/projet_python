# Ce module contient la fonction d'exportation des données des patients au format CSV.
import csv

# La fonction d'exportation des données des patients au format CSV
def exporter_csv(patients, chemin):
    if not patients:
        print("Aucun patient à exporter.")
        return
    
    try:
        colonnes = patients[0].keys()
        with open(chemin, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=colonnes)
            writer.writeheader()
            writer.writerows(patients)
        print(f"Export réussi : {chemin}")
    except Exception as e:
        print(f"Erreur lors de l'export CSV : {e}")

# j'exporte ici les fonctions statistiques
from statistiques import (
    moyenne_ages, 
    moyenne_poids, 
    ville_plus_frequente, 
    repartition_groupes_sanguins
)

# La fonction d'exportation du rapport de nettoyage des données des patients au format texte
def exporter_rapport(patients, nb_total_brut, nb_doublons, nb_rejetes, chemin):
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            f.write("="*40 + "\n")
            f.write("RAPPORT DE NETTOYAGE - DONNEES PATIENTS\n")
            f.write("="*40 + "\n\n")
            f.write(f"Nombre total de patients (fichier brut) : {nb_total_brut}\n")
            f.write(f"Nombre de patients valides : {len(patients)}\n")
            f.write(f"Nombre de doublons supprimés : {nb_doublons}\n")
            f.write(f"Nombre de lignes rejetées : {nb_rejetes}\n")
            f.write(f"Moyenne des âges : {moyenne_ages(patients):.2f}\n")
            f.write(f"Moyenne des poids : {moyenne_poids(patients):.2f}\n")
            f.write(f"Ville la plus fréquente : {ville_plus_frequente(patients)}\n")
            f.write("Répartition des groupes sanguins :\n")
            repartition = repartition_groupes_sanguins(patients)
            for groupe, nombre in repartition.items():
                f.write(f"  {groupe} : {nombre}\n")

        print(f"Rapport généré : {chemin}")
    except Exception as e:
        print(f"Erreur lors de l'export du rapport : {e}")