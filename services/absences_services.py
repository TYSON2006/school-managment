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

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            students_id = int(input("ID de l'étudiant : "))   
            date        = input("Date (ex: 2026-06-19) : ")  
            status      = input("Statut (justifiée / non justifiée) : ")
            db.ajouter(students_id, date, status)
            print("Absence ajoutée ")

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucun résultat trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID          : {row[0]}
        Étudiant ID : {row[1]}
        Date        : {row[2]}
        Statut      : {row[3]}
                    """)
           

        elif choix == '3':
            id       = int(input("ID de l'absence : "))      
            resultat = db.rechercher(id)                      
            if resultat:
                print(f"""
        ID          : {resultat[0]}
        Étudiant ID : {resultat[1]}
        Date        : {resultat[2]}
        Statut      : {resultat[3]}
                """)
            else:
                print("Aucun résultat trouvé!")
           

        elif choix == '4':
            id           = int(input("ID de l'absence : "))
            print("1. Justifiée")
            print("2. Non justifiée")
            choix_status = input("Votre choix : ").strip()
            if choix_status == '1':
                status = "justifiée"
            elif choix_status == '2':
                status = "non justifiée"
            else:
                print("Choix invalide!")
                continue                                      
            db.justifier(id, status)

        elif choix == '5':                                    
            id = int(input("ID de l'absence à supprimer : "))
            db.supprimer(id)

        elif choix == '0':                                   
            break

        else:
            print("Choix invalide!")