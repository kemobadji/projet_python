from chargement import Chargement
from nettoyage import Nettoyage_tous_patients
from validation import Validation_tous_les_patients
from statistiques import afficher_statistiques
from export import exporter_csv, exporter_rapport


def afficher_menu():
    print("="*44)
    print("SYSTÈME DE NETTOYAGE DE DONNÉES MÉDICALES")
    print("="*44)
    print("1. Charger les données brutes")
    print("2. Afficher les anomalies détectées")
    print("3. Nettoyer les données")
    print("4. Afficher les statistiques")
    print("5. Exporter les données propres")
    print("6. Quitter")


def main():
    patients_bruts = []
    patients_propres = []
    patients_rejetes = []
    nb_doublons = 0
    anomalies_suspectes = []

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            chemin = "../data/patients_bruts.txt"
            patients_bruts = Chargement(chemin)
            print(f"{len(patients_bruts)} patients chargés.")

        elif choix == "2":
            if not patients_bruts:
                print("Chargez d'abord les données (option 1).")
            elif not patients_rejetes and not anomalies_suspectes:
                print("Aucune anomalie à afficher. Vérifiez les options 1 et 3.")
            else:
                print(f"\n--- Patients rejetés ({len(patients_rejetes)}) ---")
                for item in patients_rejetes:
                    p = item["patient"]
                    print(f"ID {p['id']} - {p['nom']} {p['prenom']} : {item['erreurs']}")

                print(f"\n--- Anomalies suspectes ({len(anomalies_suspectes)}) ---")
                for item in anomalies_suspectes:
                    p = item["patient"]
                    print(f"ID {p['id']} - {p['nom']} {p['prenom']} : {item['anomalies']}")

        elif choix == "3":
            if not patients_bruts:
                print("Chargez d'abord les données (option 1).")
            else:
                patients_nettoyes = Nettoyage_tous_patients(patients_bruts)
                patients_propres, patients_rejetes, nb_doublons, anomalies_suspectes = Validation_tous_les_patients(patients_nettoyes)
                print(f"Nettoyage terminé : {len(patients_propres)} patients valides, "
                      f"{nb_doublons} doublons supprimés, "
                      f"{len(patients_rejetes)} lignes rejetées.")

        elif choix == "4":
            if not patients_propres:
                print("Aucune donnée nettoyée. Vérifiez les options 1 et 3.")
            else:
                afficher_statistiques(patients_propres, len(patients_bruts), nb_doublons, len(patients_rejetes))

        elif choix == "5":
            if not patients_propres:
                print("Aucune donnée nettoyée. Vérifiez les options 1 et 3.")
            else:
                exporter_csv(patients_propres, "../data/patients_propres.csv")
                exporter_rapport(patients_propres, len(patients_bruts), nb_doublons, len(patients_rejetes), "../rapport/rapport.txt")

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Option invalide, choisissez entre 1 et 6.")


if __name__ == "__main__":
    main()