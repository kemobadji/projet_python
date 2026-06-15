# --- Groupes sanguins autorisés ---
groupes_valides = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]


def Validation_nom(nom): # Fonction de validation du nom
    if nom.strip() == "":
        return False, "nom manquant", None
    return True, "", None


def Validation_prenom(prenom): # Fonction de validation du prénom
    if prenom.strip() == "":
        return False, "prenom manquant", None
    return True, "", None


def Validation_age(age): # Fonction de validation de l'âge
    if age.strip() == "":
        return False, "age manquant", None

    try:
        age_int = int(age) # Convertit l'âge en entier
    except ValueError:
        return False, f"age non numérique : '{age}'", None

    if age_int == 0: 
        return True, "", "age égal à zéro : suspect"
    if age_int < 0:
        return False, f"age négatif : {age_int}", None
    if age_int > 120:
        return False, f"age irréaliste : {age_int}", None

    return True, "", None


def Validation_telephone(telephone): # Fonction de validation du numéro de téléphone
    if telephone.strip() == "":
        return False, "telephone manquant", None

    if not telephone.isdigit():
        return False, f"telephone contient des caractères invalides : '{telephone}'", None

    if len(telephone) != 9:
        return False, f"telephone doit avoir 9 chiffres : '{telephone}' ({len(telephone)} chiffres)", None

    if not telephone.startswith("7"):
        return False, f"telephone doit commencer par 7 : '{telephone}'", None

    if len(set(telephone)) == 1:
        # Pas un rejet : on garde le patient mais on signale l'anomalie
        return True, "", f"telephone suspect (tous chiffres identiques) : '{telephone}'"

    return True, "", None


def Validation_groupe_sanguin(groupe): # Fonction de validation du groupe sanguin
    if groupe.strip() == "":
        return False, "groupe sanguin manquant", None

    if groupe not in groupes_valides:
        return False, f"groupe sanguin invalide : '{groupe}'", None

    return True, "", None


def Validation_poids(poids): # Fonction de validation du poids
    if poids.strip() == "" or poids.strip().upper() == "N/A":
        return False, "poids manquant", None

    try:
        poids_float = float(poids)
    except ValueError:
        return False, f"poids non numérique : '{poids}'", None

    if poids_float < 1:
        return False, f"poids trop faible : {poids_float}", None
    if poids_float > 300:
        return False, f"poids trop élevé : {poids_float}", None

    return True, "", None


def Validation_taille(taille): # Fonction de validation de la taille
    if taille.strip() == "" or taille.strip().upper() == "N/A":
        return False, "taille manquante", None

    try:
        taille_int = int(taille)
    except ValueError:
        return False, f"taille non numérique : '{taille}'", None

    if taille_int < 50:
        return False, f"taille trop faible : {taille_int}", None
    if taille_int > 250:
        return False, f"taille trop élevée : {taille_int}", None

    return True, "", None


def Validation_patient(patient):

    erreurs = []
    anomalies = []

    for fonction, champ in [
        (Validation_nom, "nom"),
        (Validation_prenom, "prenom"),
        (Validation_age, "age"),
        (Validation_telephone, "telephone"),
        (Validation_groupe_sanguin, "groupe_sanguin"),
        (Validation_poids, "poids"),
        (Validation_taille, "taille"),
    ]:
        valide, erreur, anomalie = fonction(patient[champ])
        if not valide:
            erreurs.append(erreur)
        if anomalie:
            anomalies.append(anomalie)

    if len(erreurs) != 0:
        return False, erreurs, anomalies, None

    # Si tout est valide, on construit un patient avec les bons types
    patient_converti = patient.copy()
    patient_converti["age"] = int(patient["age"])
    patient_converti["poids"] = float(patient["poids"])
    patient_converti["taille"] = int(patient["taille"])

    return True, [], anomalies, patient_converti # Renvoie True si le patient est valide, sinon False avec les erreurs et anomalies


def Validation_tous_les_patients(patients_nettoyes): # Fonction de validation de tous les patients après nettoyage
    patients_valides = [] # Liste pour stocker les patients valides
    patients_rejetes = [] # Liste pour stocker les patients rejetes
    anomalies_suspectes = [] # Liste pour stocker les anomalies suspectes
    nb_doublons = 0 # Compteur pour les doublons

    cles_vues = set()

    for patient in patients_nettoyes:
        cle = f"{patient['nom']}|{patient['prenom']}|{patient['telephone']}"

        if cle in cles_vues:
            nb_doublons += 1
            continue

        cles_vues.add(cle)

        valide, erreurs, anomalies, patient_converti = Validation_patient(patient)

        if valide:
            patients_valides.append(patient_converti)
            if anomalies:
                anomalies_suspectes.append({
                    "patient": patient,
                    "anomalies": anomalies
                })
        else:
            patients_rejetes.append({
                "patient": patient,
                "erreurs": erreurs
            })

    print(f"\n Validation terminée :")
    print(f"   - Patients valides  : {len(patients_valides)}")
    print(f"   - Patients rejetés  : {len(patients_rejetes)}")
    print(f"   - Doublons supprimés: {nb_doublons}")
    print(f"   - Anomalies suspectes: {len(anomalies_suspectes)}")

    return patients_valides, patients_rejetes, nb_doublons, anomalies_suspectes


if __name__ == "__main__":

    from chargement import Chargement
    from nettoyage import Nettoyage_tous_patients

    chemin = "../data/patients_bruts.txt"

    print("=" * 50)
    print("   TEST DU MODULE validation.py")
    print("=" * 50)

    patients_bruts    = Chargement(chemin)
    patients_nettoyes = Nettoyage_tous_patients(patients_bruts)
    patients_valides, patients_rejetes, nb_doublons, anomalies_suspectes = Validation_tous_les_patients(patients_nettoyes)

    print("\n Patients REJETÉS et leurs raisons :\n")
    for item in patients_rejetes:
        p = item["patient"]
        print(f"  ❌ Patient {p['id']} — {p['nom']} {p['prenom']}")
        for erreur in item["erreurs"]:
            print(f"      → {erreur}")

    print(f"\n Patients VALIDES ({len(patients_valides)}) :\n")
    for p in patients_valides:
        print(f"  ✅ Patient {p['id']} — {p['nom']} {p['prenom']} — {p['ville']} — {p['groupe_sanguin']}")
