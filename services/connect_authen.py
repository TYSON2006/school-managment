from models.users_models import globaUsers
import sys
from config.menu import menu_connexion, menu_akwaba

def connet_users():
    while True:
        print(menu_connexion)
        choix = input("Entrer un nombre : ").strip()

        if choix == '1':
            print(menu_akwaba)
            pseudo      = input("Entrer votre pseudo: ").strip()
            passeword = input("Écrivez votre mot de passe : ").strip()

            liaison = globaUsers()
            compte  = liaison.verification(pseudo, passeword)
            liaison.close()

            if compte:
                nom_users  = compte[1]
                pseudo_users = compte[2]
                role_users = compte[4]     
                print(f"Akwaba MR {nom_users}, votre rôle est : {role_users}")
                return role_users
            else:
                print("pseudo ou mot de passe incorrect, réessayez.")

        elif choix == '2':
            print("Merci d'être passé.")
            return None

        else:
            print("Choix invalide.")
