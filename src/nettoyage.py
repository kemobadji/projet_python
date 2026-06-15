import re # Importation du module re pour les expressions régulières

# Dictionnaire contenant les noms des villes correctes comme valeur et les erreurs comme clés
villes_correctes = {
    # Dakar
    "dakar"          : "Dakar",
    "dakarr"         : "Dakar",
    "dakkar"         : "Dakar",

    # Thies
    "thies"          : "Thies",
    "thiès"          : "Thies",

    # Saint-Louis
    "saint louis"    : "Saint-Louis",
    "saint-louis"    : "Saint-Louis",

    # Ziguinchor
    "ziguinchor"     : "Ziguinchor",
    "ziginchor"      : "Ziguinchor",
    "ziguichor"      : "Ziguinchor",
    "ziguincor"      : "Ziguinchor",

    # Kaolack
    "kaolack"        : "Kaolack",
    "kaolak"         : "Kaolack",

    # Tambacounda
    "tambacounda"    : "Tambacounda",
    "tamba"          : "Tambacounda",

    # Diourbel
    "diourbel"       : "Diourbel",
    "diorbel"        : "Diourbel",

    # Louga
    "louga"          : "Louga",
    "lougar"         : "Louga",
    
}

def Nettoyage_nom(nom): # Fonction qui nettoie les noms qu se trouve dans le fichier

    nom = nom.strip()       
    nom = nom.title()
    return nom

def Nettoyage_prenom(prenom): # Fonction qui nettoie les prenoms qu se trouve dans le fichier

    prenom = prenom.strip()
    prenom = prenom.title()
    return prenom 

def Nettoyage_telephone(telephone): # Fonction qui nettoie les numéros téléphones qu se trouve dans le fichier

    telephone = telephone.replace(" ", "")  
    telephone = telephone.replace("-", "")   
    telephone = re.sub(r"^00221", "", telephone)
    telephone = re.sub(r"^\+221", "", telephone)
    return telephone

def Nettoyage_ville(ville): # Fonction qui nettoie les villes qu se trouve dans le fichier

    ville = ville.strip()
    ville_minuscule = ville.lower()
    if ville_minuscule in villes_correctes:
        return villes_correctes[ville_minuscule]
    
    return ville.title() # Sinon 

def Nettoyage_valeur(valeur): # Fonction qui nettoie les ages, poids et taille

    valeur = valeur.strip()
    return valeur

# Fonction qui nettoie (en partie) les patients qui se trouve dans le dictionnaire 
# "patient" situé au niveau du fichier chargement.py

def Nettoyage_patient(patient): # Fonction qui nettoie (en partie) les patients qui se trouve dans le dictionnaire "patient" situé au niveau du fichier chargement.py

    patient_propre = { # Dictionnaire qui contient les informations du patient nettoyé
        "id"            : patient["id"].strip(),
        "nom"           : Nettoyage_nom(patient["nom"]),
        "prenom"        : Nettoyage_prenom(patient["prenom"]),
        "age"           : Nettoyage_valeur(patient["age"]),
        "telephone"     : Nettoyage_telephone(patient["telephone"]),
        "ville"         : Nettoyage_ville(patient["ville"]),
        "groupe_sanguin": patient["groupe_sanguin"].strip(),
        "poids"         : Nettoyage_valeur(patient["poids"]),
        "taille"        : Nettoyage_valeur(patient["taille"]),
    }

    return patient_propre

def Nettoyage_tous_patients(patients_bruts): # Fonction qui nettoie (en partie) tous les patients qui se trouve dans la liste
    patients_nettoyes = []  # Liste pour stocker les patients nettoyés

    for patient in patients_bruts:
        try:
            patient_propre = Nettoyage_patient(patient)
            patients_nettoyes.append(patient_propre)
        except Exception as e:
            print(f"[ERREUR] Impossible de nettoyer le patient id={patient.get('id', '?')} : {e}")

    print(f"\n Nettoyage terminé : {len(patients_nettoyes)} patients traités") 

    return patients_nettoyes

if __name__ == "__main__": # Point d'entrée pour tester le module nettoyage.py

    from chargement import Chargement

    chemin = "../data/patients_bruts.txt"

    print("=" * 35)
    print("   TEST DU MODULE nettoyage.py")
    print("=" * 35)

    patients_bruts = Chargement(chemin )
    patients_nettoyes = Nettoyage_tous_patients(patients_bruts)

    print("\n Comparaison AVANT → APRÈS pour 30 patients :\n")
    for i in range(min(10, len(patients_bruts))):
        b = patients_bruts[i]
        n = patients_nettoyes[i]
        print(f"  Patient {b['id']} :")
        print(f"    nom        : '{b['nom']}'  →  '{n['nom']}'")
        print(f"    prenom     : '{b['prenom']}'  →  '{n['prenom']}'")
        print(f"    age        : '{b['age']}'  →  '{n['age']}'")
        print(f"    telephone  : '{b['telephone']}'  →  '{n['telephone']}'")
        print(f"    ville      : '{b['ville']}'  →  '{n['ville']}'")
        print(f"    groupe_sanguin : '{b['groupe_sanguin']}'  →  '{n['groupe_sanguin']}'")
        print(f"    poids        : '{b['poids']}'  →  '{n['poids']}'")
        print(f"    taille        : '{b['taille']}'  →  '{n['taille']}'")
        print()