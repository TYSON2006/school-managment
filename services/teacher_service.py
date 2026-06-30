from models.teachers_models import Teach_using
from models.users_models import globaUsers
from config.menu import menu_teachers as texte_menu_teachers

def menu_teachers():
    db       = Teach_using()
    db_users = globaUsers()

    while True:
        print(texte_menu_teachers)
        choix = input("Faites un choix : ").strip()

        if choix == '1':
            # Etape 1 — créer dans users
            print("\n--- Création du compte utilisateur ---")
            nom       = input("Nom : ").strip()
            pseudo = input("pseudo :").strip()
            passeword = input("Mot de passe : ").strip()
            db_users.ajouter(nom, pseudo,passeword, 'teachers')
            user_id = db_users.dernier_id()

            # Etape 2 — compléter dans teachers
            print("\n--- Informations du professeur ---")
            matiere = input("Matière enseignée : ").strip()
            db.ajout(user_id, nom, matiere)

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucun professeur trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID      : {row[0]}
        Nom     : {row[2]}
        Matière : {row[3]}
                    """)

        elif choix == '3':
            id       = int(input("ID à rechercher : "))
            resultat = db.rechercher(id)
            if resultat:
                print(f"""
        ID      : {resultat[0]}
        Nom     : {resultat[2]}
        Matière : {resultat[3]}
                """)
            else:
                print("Professeur non trouvé!")

        elif choix == '4':
            id      = int(input("ID à modifier : "))
            nom     = input("Nouveau nom : ").strip()
            matiere = input("Nouvelle matière : ").strip()
            db.modifier(id, nom, matiere)

        elif choix == '5':
            id = int(input("ID à supprimer : "))
            db.supprimer(id)

        elif choix == '0':
            break

        else:
            print("Choix invalide!")
