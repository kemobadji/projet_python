import re # Permet de manipuler des chaînes de caractères complexes

# Dictionnaire contenant les noms des villes correctes comme valeur et les erreurs comme clés
villes_correctes = {
    # Dakar
    "dakar"          : "Dakar",
    "dakarr"         : "Dakar",
    "dakkar"         : "Dakar",

    # Thies
    "thies"          : "Thies",
    "thies"          : "Thies",

    # Saint-Louis
    "saint louis"    : "Saint-Louis",
    "saint-louis"    : "Saint-Louis",

    # Ziguinchor
    "ziguinchor"     : "Ziguinchor",
    "ziginchor"      : "Ziguinchor",
    "ziguichor"      : "Ziguinchor",

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

def Nettoyage_patient(patient): 

    patient_propre = {
        "id"            : patient["id"].strip(),
        "nom"           : Nettoyage_nom(patient["nom"]),
        "prenom"        : Nettoyage_nom(patient["prenom"]),
        "age"           : Nettoyage_valeur(patient["age"]),
        "telephone"     : Nettoyage_telephone(patient["telephone"]),
        "ville"         : Nettoyage_ville(patient["ville"]),
        "groupe_sanguin": patient["groupe_sanguin"].strip(),
        "poids"         : Nettoyage_valeur(patient["poids"]),
        "taille"        : Nettoyage_valeur(patient["taille"]),
    }

    return patient_propre

# Fonction qui nettoie(en part) tous les patients qui se trouve dans la liste de dictionnaire
# "patients_bruts" situé dans le fichier chargement.py
 
def Nettoyage_tous_patients(patients_bruts): 

    patient_nettoyer = [] # Liste qui va contenir tous les patients nettoyer

    for patient in patients_bruts:

        try:    
            patient_propre = Nettoyage_patient(patient)
            patient_nettoyer.append(patient_propre)

        except Exception as e:
            print("Erreur survenue lors du nettoyage")

    return patient_nettoyer

if __name__ == "__main__":

    print("=" * 35)
    print("   TEST DU MODULE nettoyage.py")
    print("=" * 35)

    from chargement import Chargement 

      
    

   








