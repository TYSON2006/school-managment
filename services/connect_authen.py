from models.users_models import globaUsers
import sys
from config.menu import menu_connexion, menu_akwaba

def connet_users():
    
    print(menu_connexion)
    choix = input("Entrer un nombre : ").strip()

    if choix == '1':
        print(menu_akwaba)
        nom       = input("Entrer votre nom : ").strip()
        passeword = input("Écrivez votre mot de passe : ").strip()

        liaison = globaUsers()
        compte  = liaison.verification(nom, passeword)  # ← liaison.users() retiré
        liaison.close()

        if compte:
            nom_users  = compte[1]
            role_users = compte[2]
            print(f"Akwaba MR {nom_users}, votre rôle est : {role_users}")
            return role_users
        else:
            print("Nom ou mot de passe incorrect ressayer ")
           
    elif choix == '2':
        print("Merci d'être passé.")
        sys.exit()