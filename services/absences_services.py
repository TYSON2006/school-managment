from models.absences_models import absences_using

import sys


from config.menu import menu_connexion,menu_absences



def menu_absences():
    db = absences_using()


    while True:
        print("""
==================================
       GESTION DES ABSENCES
==================================
  1. Ajouter une absence
  2. Afficher toutes les absences
  3. Rechercher une absence
  4. Justifier une absence
  5. Supprimer une absence
  0. Retour
==================================
              """)
        choix = input("faites un choix :").strip()
        if choix == '1':
            students_id = input(" id a rentrer :")
            date = float(input("entrer la date :"))
            status = input("entrer le status :")
            db.ajout(students_id,date,status)
        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("aucun resultat trouvé !!")
            else:
                for row in resultat:
                    print(f"""
                students_id : {row[0]}
                date : {row[1]}
                status : {row[2]}
                          """)
                    print("merci d'être passé!!")
                   
        elif choix == '3':
            resultat = db.rechercher()
            if not resultat:
                print("aucun resultat trouvé !!")
            else:
                for row in resultat:
                    print(f"""
                students_id :{resultat[0]}
                date : {resultat[1]}
                status : {resultat[2]}
                          """)
                   
                    print("merci d'être passé!!")
        elif choix == '4':
            id = int(input("id de l'absences :"))
            print("1.justifiée")
            print("2.non justifiée")
            choix_status = input("votre choix :").strip()
            if choix_status == '1':
                status = "justifiée"
            elif choix_status == '2':
                     status = "non justifiée"
        
        
        else:
            print("choi invalide!")
            db.justifier()
        elif
       

        
