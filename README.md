                            PROJET DE PROGRAMMATION PYTHON 1

Ceci est projet appelé "Prétraitement et Nettoyage de Données Médicales".Dans ce projet, on incarne une équipe de prétraitement de données travaillant dans un environnement réel de data engineering. Une clinique médicale dispose d'un fichier de données patients collecté depuis
plusieurs sources sur plusieurs années. Ce fichier est dans un état déplorable et notre mission est de développer une application Python capable de lire ce fichier, de détecter toutes les anomalies, de nettoyer les données et de produire un dataset final exploitable par les équipes data science.

On commence par le fichier chargement.py qui a pour rôle de charger le fichier patients_bruts.txt et de le lire.
A l'intérieur on a créer des fonctions:
- Chargement(chemin_fichier) : qui permet de charger le fichier patients_bruts.txt et de le lire.
Affichage_patients(patients) : qui permet d'afficher les patients chargés.


Après le fichier nettoyage.py qui a pour rôle de nettoyer les données. A l'intérieur on a créer des fonctions:
- Nettoyage_tous_patients(patients) : qui permet de nettoyer tous les patients
Nettoyage_patient(patient) : qui permet de nettoyer un patient
Nettoyage_nom(nom) : qui permet de nettoyer le nom d'un patient
Nettoyage_prenom(prenom) : qui permet de nettoyer le prénom d'un patient
Nettoyage_age(age) : qui permet de nettoyer l'âge d'un patient
Nettoyage_telephone(telephone) : qui permet de nettoyer le numéro de téléphone d'un patient
Nettoyage_ville(ville) : qui permet de nettoyer la ville d'un patient 
Nettoyage_groupe_sanguin(groupe_sanguin) : qui permet de nettoyer le groupe sanguin d'un patient
Nettoyage_poids(poids) : qui permet de nettoyer le poids d'un patient
Nettoyage_taille(taille) : qui permet de nettoyer la taille d'un patient   


Nous avons aussi le fichier validation.py qui a pour rôle de valider les données. A l'intérieur on a créer des fonctions:
- Validation_tous_les_patients(patients) : qui permet de valider tous les patients
Validation_patient(patient) : qui permet de valider un patient
Validation_nom(nom) : qui permet de valider le nom d'un patient
Validation_prenom(prenom) : qui permet de valider le prénom d'un patient
Validation_age(age) : qui permet de valider l'âge d'un patient
Validation_telephone(telephone) : qui permet de valider le numéro de téléphone d'un patient 
Validation_ville(ville) : qui permet de valider la ville d'un patient
Validation_groupe_sanguin(groupe_sanguin) : qui permet de valider le groupe sanguin d'un patient
Validation_poids(poids) : qui permet de valider le poids d'un patient
Validation_taille(taille) : qui permet de valider la taille d'un patient
