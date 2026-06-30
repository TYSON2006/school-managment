from models.subjects_models import subject_using
from config.menu import menu_subjects as texte_menu_subjects

def menu_subject():
    db = subject_using()                 
    while True:
        print(texte_menu_subjects)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            nom        = input("Nom de la matière : ").strip()
            teacher_id = int(input("ID du professeur : "))
            db.ajouter(nom, teacher_id)    

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucune matière trouvée!")
            else:
                for row in resultat:       # ← resultat → row dans la boucle
                    print(f"""
        ID            : {row[0]}
        Matière       : {row[1]}
        Professeur ID : {row[2]}
                    """)

        elif choix == '3':
            id       = int(input("ID de la matière à rechercher : "))  # ← int
            resultat = db.rechercher(id)
            if resultat:
                print(f"""
        ID            : {resultat[0]}
        Matière       : {resultat[1]}
        Professeur ID : {resultat[2]}
                """)
            else:
                print("Matière non trouvée!")

        elif choix == '4':
            id = int(input("ID de la matière à supprimer : "))  # ← int
            db.supprimer(id)               # ← appel correct

        elif choix == '0':
            break

        else:
            print("Choix invalide!")