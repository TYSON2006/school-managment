from models.users_models import globaUsers

import sys

from config.menu import menu_connexion,menu_akwaba


def connet_users():
    print(menu_connexion)
    choix = input("entrer un nombre :").strip()
    if choix =='1':
        print(menu_akwaba)
        nom = input("entrer votre nom :").strip()
        passeword = input("ecrivez votre mot de pass:").strip()
        liaison = globaUsers()
        liaison.users()
        compte = liaison.verification(nom,passeword)
        liaison.close()
        if compte : 
            nom_users = compte[1]
            role_users = compte[2]
            print(f"akwaba MR {nom_users} votre role est {role_users}")
            return role_users
        else:
            print("merci d'être passé.")
            sys.exit()



    elif choix == '2':
        print(" merci d'être passé ")
        return

