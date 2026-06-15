from models.subjects_models import subject_using

import sys

from config.menu import menu_connexion,menu_subjects



def menu_subject():
    db = subject_using


    while True :
        print("""
==================================
        GESTION DES MATIÈRES
==================================
  1. Ajouter une matière
  2. Afficher toutes les matières
  3. Rechercher une matière
  4. Supprimer une matière
  0. Retour
==================================
              """)
        choix = input("faite un choix :").strip()
        if choix == '1':
            matiere = input("entrer la matiere:")
            db.ajout(matiere)
        elif choix == '2':
            resultat = db .afficher()
            if not resultat:
               print("aucune matiere trouvé!")
            else:
                for row in resultat:
                    print(f"""
                          id {resultat[0]}
                          matiere : {resultat[1]}
                          """)
                    print("merci d'être passé!")
        elif choix == '3':
            matiere = input("id de la matiere rechercher:")
            matiere = db.rechercher(id)

        elif choix == '4':
            matiere = input("id de la matiere a supprimer? :")
            print("merci d'être passé!")
            matiere = db.supprimer(id)

        elif choix == '0':
            break
        else:
            print("retour")
            




            
               
           
