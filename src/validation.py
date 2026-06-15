# --- Groupes sanguins autorisés ---
GROUPES_VALIDES = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

def Validation_nom(nom): # Fonction qui valide les noms
    
    if nom.strip() == "":
        return False, "nom manquant"
    return True, ""

def Validation_prenom(prenom): # Fonction qui valide les prenoms
    
    if prenom.strip() == "":
        return False, "prenom manquant"
    return True, ""


def Validation_age(age): # Fonction qui valide les ages
   
    if age.strip() == "":
        return False, "age manquant"

    try:
        age_int = int(age)
    except ValueError:
        return False, f"age non numérique : '{age}'"

    if age_int < 0:
        return False, f"age négatif : {age_int}"
    if age_int == 0:
        return False, f"age égal à zéro : suspect"
    if age_int > 120:
        return False, f"age irréaliste : {age_int}"

    return True, ""


def Validation_telephone(telephone): # Fonction qui valide les telephone
    
    if telephone.strip() == "":
        return False, "telephone manquant"

    if not telephone.isdigit():
        return False, f"telephone contient des caractères invalides : '{telephone}'"

    if len(telephone) != 9:
        return False, f"telephone doit avoir 9 chiffres : '{telephone}' ({len(telephone)} chiffres)"

    if not telephone.startswith("7"):
        return False, f"telephone doit commencer par 7 : '{telephone}'"

    if len(set(telephone)) == 1:
        return False, f"telephone suspect (tous chiffres identiques) : '{telephone}'"

    return True, ""


def Validation_groupe_sanguin(groupe): # Fonction qui valide les groupes sanguins
   
    if groupe.strip() == "":
        return False, "groupe sanguin manquant"

    if groupe not in GROUPES_VALIDES:
        return False, f"groupe sanguin invalide : '{groupe}'"

    return True, ""


def Validation_poids(poids): # Fonction qui valide les poids
    
    if poids.strip() == "" or poids.strip().upper() == "N/A":
        return False, "poids manquant"

    try:
        poids_float = float(poids)
    except ValueError:
        return False, f"poids non numérique : '{poids}'"

    if poids_float < 1:
        return False, f"poids trop faible : {poids_float}"
    if poids_float > 300:
        return False, f"poids trop élevé : {poids_float}"

    return True, ""


def Validation_taille(taille): # Fonction qui valide les tailles
   
    if taille.strip() == "" or taille.strip().upper() == "N/A":
        return False, "taille manquante"

    try:
        taille_int = int(taille)
    except ValueError:
        return False, f"taille non numérique : '{taille}'"

    if taille_int < 50:
        return False, f"taille trop faible : {taille_int}"
    if taille_int > 250:
        return False, f"taille trop élevée : {taille_int}"

    return True, ""


# =============================================================================
# FONCTION PRINCIPALE — Validation un seul patient
# =============================================================================

def Validation_patient(patient): # Fonction qui valide les patients un par un
   
    erreurs = []

    valide, msg = Validation_nom(patient["nom"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_prenom(patient["prenom"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_age(patient["age"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_telephone(patient["telephone"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_groupe_sanguin(patient["groupe_sanguin"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_poids(patient["poids"])
    if not valide:
        erreurs.append(msg)

    valide, msg = Validation_taille(patient["taille"])
    if not valide:
        erreurs.append(msg)

    if len(erreurs) == 0:
        return True, []
    else:
        return False, erreurs


# =============================================================================
# FONCTION PRINCIPALE — Validation toute la liste + supprimer les doublons
# =============================================================================

def Validation_tous_les_patients(patients_nettoyes): # Fonction qui valide tous les patients
    
    patients_valides = []
    patients_rejetes = []
    doublons_trouves = 0

    cles_vues = set()

    for patient in patients_nettoyes:
        cle = f"{patient['nom']}|{patient['prenom']}|{patient['telephone']}"

        if cle in cles_vues:
            doublons_trouves += 1
            patients_rejetes.append({
                "patient": patient,
                "erreurs": ["doublon détecté"]
            })
            continue

        cles_vues.add(cle)

        valide, erreurs = Validation_patient(patient)

        if valide:
            patients_valides.append(patient)
        else:
            patients_rejetes.append({
                "patient": patient,
                "erreurs": erreurs
            })

    print(f"\n Validation terminée :")
    print(f"   - Patients valides  : {len(patients_valides)}")
    print(f"   - Patients rejetés  : {len(patients_rejetes)}")
    print(f"   - Doublons supprimés: {doublons_trouves}")

    return patients_valides, patients_rejetes


# =============================================================================
# TEST — s'exécute seulement si on lance ce fichier directement
# =============================================================================
if __name__ == "__main__":

    import sys
    sys.path.append("..")
    from chargement import Chargement
    from nettoyage import Nettoyage_tous_patients

    chemin_fichier = "../data/patients_bruts.txt"

    print("=" * 50)
    print("   TEST DU MODULE validation.py")
    print("=" * 50)

    patients_bruts    = Chargement(chemin_fichier)
    patients_nettoyes = Nettoyage_tous_patients(patients_bruts)
    patients_valides, patients_rejetes = Validation_tous_les_patients(patients_nettoyes)

    print("\n Patients REJETÉS et leurs raisons :\n")
    for item in patients_rejetes:
        p = item["patient"]
        print(f"  ❌ Patient {p['id']} — {p['nom']} {p['prenom']}")
        for erreur in item["erreurs"]:
            print(f"      → {erreur}")

    print(f"\n Patients VALIDES ({len(patients_valides)}) :\n")
    for p in patients_valides:
        print(f"  ✅ Patient {p['id']} — {p['nom']} {p['prenom']} — {p['ville']} — {p['groupe_sanguin']}")




