from models.grades_models import grades_using
from config.menu import menu_grades as texte_menu_grades

def menu_grades():
    db = grades_using()

    while True:
        print(texte_menu_grades)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            students_id = int(input("ID de l'étudiant : "))
            subjects_id = int(input("ID de la matière : "))
            note        = float(input("Note (0-20) : "))
            db.ajout(students_id, subjects_id, note)

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucun résultat trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID          : {row[0]}
        Étudiant ID : {row[1]}
        Matière ID  : {row[2]}
        Note        : {row[3]}
                    """)                   # ← index corrigés, row pas resultat

        elif choix == '3':
            id       = int(input("ID de la note : "))
            resultat = db.rechercher(id)
            if resultat:
                print(f"""
        ID          : {resultat[0]}
        Étudiant ID : {resultat[1]}
        Matière ID  : {resultat[2]}
        Note        : {resultat[3]}
                """)                       
            else:
                print("Aucun résultat trouvé!")

        elif choix == '4':
            id   = int(input("ID à modifier : "))    
            note = float(input("Nouvelle note (0-20) : "))
            db.modifier(id, note)

        elif choix == '5':
            id = int(input("ID à supprimer : "))     
            db.supprimer(id)

        elif choix == '6':
            student_id = int(input("ID de l'étudiant : "))
            moyenne    = db.calculer(student_id)     
            print(f"Moyenne de l'étudiant ID {student_id} : {moyenne:.2f}/20") 

        elif choix == '0':
            break

        else:
            print("Choix invalide!")