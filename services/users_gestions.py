from models.users_models import globaUsers


def menu_users():
    db = globaUsers()


    while True :
        print("""
=========================================
        GESTION DES UTILISATEURS
=========================================
  1. Afficher tous les utilisateurs
  2. Modifier le rôle d'un utilisateur et pseudo
  3. Supprimer un utilisateur
  0. Retour
=========================================
              """)
        choix = input("faite un choix :").strip()

        if choix == '1':
            resultats = db.afficher()
            if not resultats:
                print("aucun resultat trouvé!")
            else:
                for row in resultats:
                    print("""
                    id : {row[0]}
                    nom : {row[1]}
                    pseudo : {row[2]}
                    role : {row[3]}
                          """)
        elif choix == '2':
            id = int (input("id de l'user :"))
            nom = input("nom :")
            pseudo = input("nouveau pseudo :")
            role = input("nouveau role (admin/student/teachers) : ").strip()
            db.modifier(id,nom,pseudo , role)
        
        elif  choix == '3':
            id = int(input("id à supprimer"))
            db.supprimer(id)

        elif choix == '0':
            break
        else:
            print("choix invalide")

    