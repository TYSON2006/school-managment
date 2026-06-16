from models.grades_models import grades_using

import sys

from config.menu import menu_connexion,menu_grades


def menu_grades():
    db = grades_using()


    while True :
        print(
            """


==================================
        GESTION DES NOTES
==================================
  1. Ajouter une note
  2. Afficher toutes les notes
  3. Rechercher une note
  4. Modifier une note
  5. Supprimer une note
  6. Calculer la moyenne d'un étudiant
  0. Retour
==================================


"""
        )

        choix = input("faite un choix:").strip()

        if choix == '1':
            students_id = input("id de l'etududiant:")
            subjects_id = input("id de la matiere")
            note = float(input("0-20"))
            print("merci d'être passé")
            db.ajout(students_id,subjects_id,note)
        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("aucun resultat trouvé!")
            else:
                for row in resultat:
                    print(f"""
                          id :{row[1]} , 
                          etudiant id :{row[2]}
                          matiere id : {row[3]}
                          note : {row[4]}
                    """) 
                    print("merci d'être passé")
                    db.afficher(students_id,subjects_id,note)
        elif choix == '3':
            id = int(input("id de la note:"))

            resultat = db.rechercher(id)
            if  resultat:
                print(f"""
                        id :{resultat[1]},
                        students id :{resultat[2]},
                        subjects id :{resultat[3]},
                        note : {resultat[4]} 
                      """)
                print("merci d'être passé")
            else:
                print("aucun resultat trouvé!")
        elif choix == '4':
            id = input("id a modifier :")
            note = float(input("nouvelle note (0-20):"))
            db.modifier(id,note)
        elif choix == '5':
            id = input("id a supprimer:")
        elif choix == '6':
            students_id = int(input("id de l'etudiant :"))
            moyenne = db.calculer(students_id)
            print(f"moyenne de l'etudiant id{students_id}: {moyenne : .2f/20}")
        elif choix == '0':
            break
        else:
            print("choix valide!!")       
                  

   