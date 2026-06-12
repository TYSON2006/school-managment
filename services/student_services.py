from models.students_models import students_using 


import          sys

from config.menu  import menu_connexion,menu_students 


def menu_students():
    db = students_using()

    while True:
        print("""
       
==================================
        GESTION DES ÉTUDIANTS
==================================
  1. Ajouter un étudiant
  2. Afficher tous les étudiants
  3. Rechercher un étudiant
  4. Modifier un étudiant
  5. Supprimer un étudiant
  0. Retour
==================================
              """)
        choix = input("faite un choix:").strip()
        if choix == '1':
            nom = input("nom:")
            prenom = input("prenom:")
            age = input("age:")
            matricule = input("matricule : ")
            classe = input("classe :")
            db.ajouter(nom,prenom,age,matricule,classe)
        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("aucun etudiant trouvé!")
            else:
                for row in resultat:
                    print(f"""
        id :{row[0]}
        matricule :{row[1]}
        nom :{row[2]}
        prenom :{row[3]}
        age : {row[4]}
        classe : {row[5]}
                          """)
                    print("merci d'être passé")
                  
        elif choix =='3':
            id = int(input("id à rechercher:"))
            etudiant = db.rechercher()
            if etudiant:
                print(f"""
         id :{row[0]}
         nom :{row[1]}
         prenom :{row[2]}
                      """)
                print(" aucun etudiant trouvé!")
      
        elif choix == '4':
            id = int(input("id à modifier:"))
            nom = int(input("nouveau nom :"))
            prenom = int(input("nuovel age:"))
            matricule = input("nuoveau matricule:")
            db.modifier(id,nom,prenom,matricule)

        elif choix == '5':
            id = int(input("id à supprimer:"))
            db .supprimer(id)

        elif choix == '0':
            break
        else:
            print("retour.")
