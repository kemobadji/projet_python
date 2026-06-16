# Projet Python - Nettoyage Données Médicales

## Membres
- Abdou Aziz SAMB
- Kemo BADJI

## Description du projet
Ce projet consiste à développer une application Python pour le prétraitement et le nettoyage de données médicales. L'objectif est de lire un fichier de données patients, de détecter les anomalies, de nettoyer les données et de produire un dataset final exploitable par les équipes data science ou data engineers.
--=====================================================================================================--
--                         Etapes realisées dans ce projet par Abdou Aziz SAMB                         --
--=====================================================================================================--
1) je viens de creer ma branche 'brancheB'
cette branche est destinée à contenir les modifications liées à l'ajout de nouvelles fonctionnalités pour l'analyse des données des patients, notamment les fonctions de calcul de statistiques et d'exportation des données. Je vais travailler sur cette branche pour implémenter ces fonctionnalités sans affecter la branche principale 'main'.
2) je viens de terminer le fichier 'statistiques.py' dans le dossier 'src'
ce fichier contient une fonction pour calculer la moyenne des âges des patients à partir d'une liste de dictionnaires représentant les patients. La fonction vérifie si la liste est vide et retourne 0 dans ce cas, sinon elle calcule la somme des âges et divise par le nombre de patients pour obtenir la moyenne.
Pareil pour les autres fonctions de ce fichier : moyenne_poids, ville_plus_frequente, repartition_groupes_sanguins. Et affichage_statistiques qui affiche les résultats de ces fonctions de manière lisible.
je viens de faire un commit avec le message "Ajout du fichier statistiques.py"
3) je viens de terminer le fichier 'export.py' dans le dossier 'src'
ce fichier contient une fonction pour exporter les données des patients au format CSV. La fonction vérifie si la liste de patients est vide et affiche un message d'erreur si c'est le cas. Sinon, elle ouvre un fichier en mode écriture, crée un objet writer pour écrire les données au format CSV, écrit l'en-tête du fichier, puis parcourt la liste des patients pour écrire chaque patient dans le fichier.
je viens de faire un commit avec le message "Ajout du fichier export.py"
4) je viens de terminer les modifications dans le fichier 'main.py' dans le dossier 'src'
j'ai ajouté des vérifications pour s'assurer que les données nettoyées sont disponibles avant d'afficher les statistiques ou d'exporter les données. Si les données nettoyées ne sont pas disponibles, un message d'erreur est affiché pour informer l'utilisateur de vérifier les options précédentes.
je viens de faire un commit avec le message "Mise à jour du fichier main.py pour améliorer la gestion des données nettoyées et des anomalies"

--=====================================================================================================--
--                         Etapes realisées dans ce projet par Kemo BADJI                              --
--=====================================================================================================--

Ceci est projet appelé "Prétraitement et Nettoyage de Données Médicales".Dans ce projet, on incarne une équipe de prétraitement de données travaillant dans un environnement réel de data engineering. Une clinique médicale dispose d'un fichier de données patients collecté depuis
plusieurs sources sur plusieurs années. Ce fichier est dans un état déplorable et notre mission est de développer une application Python capable de lire ce fichier, de détecter toutes les anomalies, de nettoyer les données et de produire un dataset final exploitable par les équipes data science.


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