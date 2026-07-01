## SYSTÈME DE GESTION D'ÉCOLE ##

Application CLI (terminal) de gestion complète d'un système scolaire, développée en Python pur avec SQLite.


## DESCRIPTION ##

Ce projet simule le fonctionnement réel d'une école depuis le terminal. Il permet à un administrateur de gérer les étudiants, professeurs, matières, notes et absences, avec un système d'authentification par rôle et une journalisation complète des actions.


## FONCTIONNALITÉS ##

Authentification — connexion par pseudo + mot de passe avec gestion des rôles
Gestion des utilisateurs — ajout, modification, suppression
Gestion des étudiants — CRUD complet (matricule, nom, prénom, âge, classe)
Gestion des professeurs — CRUD complet (nom, matière enseignée)
Gestion des matières — ajout, affectation d'un professeur
Gestion des notes — ajout avec validation (0-20), moyenne par étudiant
Gestion des absences — enregistrement, justification, historique
Statistiques — meilleur étudiant, moyenne générale, comptage des absences
Logs — journalisation automatique de toutes les actions dans logs/app.log


## ARCHITÈCTURE ##

school-managment/
│── main.py                        ← Point d'entrée + gestion des rôles
│── init_data.py                   ← Création du compte admin initial
│── database/
│   └── connexion.py               ← Classe MESDONNÉES (connexion SQLite)
│── models/                        ← Requêtes SQL (CRUD)
│   ├── users_models.py
│   ├── students_models.py
│   ├── teachers_models.py
│   ├── subjects_models.py
│   ├── grades_models.py
│   └── absences_models.py
│── services/                      ← Menus CLI
│   ├── connect_authen.py
│   ├── student_services.py
│   ├── teacher_service.py
│   ├── subjects_services.py
│   ├── grades_services.py
│   ├── absences_services.py
│   ├── stats_services.py
│   └── users_gestions.py
│── utils/
│   └── loggers.py                 ← Configuration du système de logs
│── config/
│   ├── menu.py                    ← Textes des menus
│   └── settings.py                ← Constantes de configuration
│── logs/
│   └── app.log                    ← Fichier de logs (généré automatiquement)


## BASES DE DONNÉES ##

Le projet utilise SQLite avec 6 tables reliées par des clés étrangères :

TableColonnes principalesusersid, nom, pseudo, passeword, rolestudentsid, user_id, matricule, nom, prenom, age, classeteachersid, user_id, nom, matieresubjectsid, nom, teacher_idgradesid, students_id, subjects_id, notesabsencesid, student_id, date, status


## RÔLES DISPONIBLE ##

RôleAccèsadminAccès complet à tous les modulesteachersMatières, notes, absencesstudentConsultation de ses informations, notes et absences


⚙️ Installation et lancement

Prérequis


Python 3.x
Aucune dépendance externe (SQLite est inclus dans Python)


Étapes

1. Cloner le projet

bashgit clone https://github.com/TYSON2006/school-managment.git
cd school-managment

2. Créer le compte administrateur

bashpython3 init_data.py

3. Lancer l'application

bashpython3 main.py

4. Se connecter

Pseudo    : Admin
Mot de passe : 1234


## SYSTÈME DE LOGS ##

Toutes les actions sont enregistrées automatiquement dans logs/app.log :

2026-06-25 10:15:00 [INFO]    Étudiant Allou ajouté
2026-06-25 10:20:00 [WARNING] Note invalide rejetée
2026-06-25 10:30:00 [ERROR]   Erreur base de données : ...


## TECHNOLOGIE RESPECTÉÉS ##


Python 3 — langage principal
SQLite3 — base de données relationnelle
logging — journalisation des actions
POO — programmation orientée objet avec héritage
Git — versionnement du code


 ## CONTRAINTE RESPECTÉE ##


Aucun framework externe
Aucun frontend (HTML/CSS)
Application en ligne de commande uniquement
SQLite obligatoire
Système de logs obligatoire
Code structuré en modules
Git utilisé



## AUTEUR##

Kouadio Nango Ruffin Tyson
 NAN Académie — Abidjan, Côte d'Ivoire
Juin 2026