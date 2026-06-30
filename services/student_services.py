from models.students_models import students_using
from models.users_models import globaUsers
from config.menu import menu_students as texte_menu_students

def menu_students():
    db          = students_using()
    db_users    = globaUsers()

    while True:
        print(texte_menu_students)
        choix = input("Faites un choix : ").strip()

        if choix == '1':
            # Etape 1 — créer dans users
            print("\n--- Création du compte utilisateur ---")
            nom       = input("Nom : ").strip()
            pseudo = input("pseudo :").strip()
            passeword = input("Mot de passe : ").strip()
            db_users.ajouter(nom, pseudo,passeword, 'student')
            user_id = db_users.dernier_id()

            # Etape 2 — compléter dans students
            print("\n--- Informations de l'étudiant ---")
            prenom    = input("Prénom : ").strip()
            age       = int(input("Âge : "))
            matricule = input("Matricule : ").strip()
            classe    = input("Classe : ").strip()
            db.ajouter(user_id, nom, prenom, age, matricule, classe)

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucun étudiant trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID        : {row[0]}
        User ID   : {row[1]}
        Matricule : {row[2]}
        Nom       : {row[3]}
        Prénom    : {row[4]}
        Âge       : {row[5]}
        Classe    : {row[6]}
                    """)

        elif choix == '3':
            id       = int(input("ID à rechercher : "))
            etudiant = db.rechercher(id)
            if etudiant:
                print(f"""
        ID        : {etudiant[0]}
        Matricule : {etudiant[2]}
        Nom       : {etudiant[3]}
        Prénom    : {etudiant[4]}
        Âge       : {etudiant[5]}
        Classe    : {etudiant[6]}
                """)
            else:
                print("Aucun étudiant trouvé!")

        elif choix == '4':
            id        = int(input("ID à modifier : "))
            nom       = input("Nouveau nom : ").strip()
            age       = int(input("Nouvel âge : "))
            matricule = input("Nouveau matricule : ").strip()
            db.modifier(id, nom, age, matricule)

        elif choix == '5':
            id = int(input("ID à supprimer : "))
            db.supprimer(id)

        elif choix == '0':
            break

        else:
            print("Choix invalide!")
