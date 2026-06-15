chemin = "../data/patients_bruts.txt" # Chemin vers le fichier patients_bruts.txt

def Chargement(chemin): # Fonction qui charge le fichier patients_bruts.txt et le lit

    # Les colonnes du fichier patients_bruts.txt
    colonnes = ["id", "nom", "prenom", "age", "telephone", "ville", "groupe_sanguin", "poids", "taille"]
    nbr_colonnes = len(colonnes) 
    patients_bruts = [] # liste qui contiendra tous les patients
    lignes_ignorees = 0 # compteur des lignes non lues

    try:
        
        with open(chemin, "r", encoding="utf-8") as f: # Ouverture du fichier en lecture
            fichier = f.readlines()

    except FileNotFoundError:
        print(f"Fichier introuvable : {chemin}") # Le fichier n'existe pas à cet emplacement et retourne une liste vide.
        return []

    except Exception as e:
        print(f"Impossible d'ouvrir le fichier : {e}") # Autre problème lors de  l'ouverture et retourne une liste vide.
        return []

    if len(fichier) == 0: # Si le fichier est vide ça va retourner une liste vide. 
        print("Le fichier est vide.")
        return []

    donnees = fichier[1:]  # Première ligne du fichier patients_bruts.txt est ignorée

    # Parcourir chaque ligne de données
    for index, ligne in enumerate(donnees, start=2):  # start=2 car ligne 1 = en-tête
        ligne = ligne.strip() # Suppression des (\n) en fin de chaîne créés par la readlines
        if ligne == "": # Ignorer les lignes complètement vides
            continue

        try:
            
            champs = ligne.split(";") # Découper la ligne en champs séparés par ";"

            if len(champs) != nbr_colonnes:  # Vérification du nombre de colonne
                print(f"Erreur sur le nombre de colonnes")
                lignes_ignorees += 1
                continue

            # Création du dictionnaire patient 
            patient = {
                "id"            : champs[0],
                "nom"           : champs[1],
                "prenom"        : champs[2],
                "age"           : champs[3],
                "telephone"     : champs[4],
                "ville"         : champs[5],
                "groupe_sanguin": champs[6],
                "poids"         : champs[7],
                "taille"        : champs[8],
            }

            patients_bruts.append(patient) # Chaque dictionnaire de patient sera ajouter dans la liste patients_bruts.

        except Exception as e:
            # Si une ligne cause une erreur inattendue, on l'ignore sans crasher
            print(f"Erreur inattendue sur une ligne: {e}")
            lignes_ignorees += 1

    return patients_bruts

def Affichage_patient(patient): # Fonction pour afficher les informations d'un patient de manière lisible
    
    print("-" * 35)
    for cle, valeur in patient.items():
        print(f"  {cle:<15} : '{valeur}'")
    print("-" * 35)

if __name__ == "__main__": # Test du module chargement.py

    print("=" * 35)
    print("   TEST DU MODULE chargement.py")
    print("=" * 35)

    patients = Chargement(chemin)

    if patients:
        print(f"\n Aperçu des 30 premiers patients chargés :\n")
        for p in patients[:10]:
            Affichage_patient(p)
    