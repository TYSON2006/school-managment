from models.absences_models import absences_using
from config.menu import menu_absences as texte_menu_absences

def menu_absences():
    db = absences_using()

    while True:
        print(texte_menu_absences)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            student_id = int(input("ID de l'étudiant : "))
            date       = input("Date (ex: 2026-06-19) : ")
            status     = input("Statut (justifiée / non justifiée) : ")
            db.ajout(student_id, date, status)

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
            print("Statut mis à jour ✅")

        elif choix == '5':
            id = int(input("ID de l'absence à supprimer : "))
            db.supprimer(id)

        elif choix == '0':
            break

        else:
            print("Choix invalide!")