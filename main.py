from models.users_models import globaUsers

user = globaUsers()

MENU_USER = """
=========================================
         GESTION D'ÉCOLE
=========================================

1 - Ajouter un utilisateur
2 - Afficher les utilisateurs
3 - Modifier un utilisateur
4 - Supprimer un utilisateur
0 - Quitter
"""

while True:
    print(MENU_USER)

    choix = input("Votre choix : ")

    # AJOUTER
    if choix == "1":
        nom = input("Nom : ")
        role = input("Role : ")
        matricule = input("matricule")

        user.ajouter(nom, role)
        print("Utilisateur ajouté avec succès.")

    # AFFICHER
    elif choix == "2":
        utilisateurs = user.afficher()

        if not utilisateurs:
            print("Aucun utilisateur trouvé.")
        else:
            print("\n===== LISTE DES UTILISATEURS =====")

            for u in utilisateurs:
                print(f"""
ID   : {u[0]}
Nom  : {u[1]}
Role : {u[2]}
-------------------------
""")

    # MODIFIER
    elif choix == "3":
        id = int(input("ID de l'utilisateur : "))
        nom = input("Nouveau nom : ")
        role = input("Nouveau rôle : ")

        user.modifier(id, nom, role)
        print("Modification effectuée.")

    # SUPPRIMER
    elif choix == "4":
        id = int(input("ID à supprimer : "))

        user.supprimer(id)
        print("Utilisateur supprimé.")

    # QUITTER
    elif choix == "0":
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")