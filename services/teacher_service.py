from models.teachers_models import Teach_using
from config.menu import menu_teachers as texte_menu_teachers

def menu_teachers():
    db = Teach_using()

    while True:
        print(texte_menu_teachers)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            nom     = input("Nom du professeur : ").strip()
            matiere = input("Matière enseignée : ").strip()
            db.ajout(nom, matiere)

        elif choix == '2':
            resultat = db.afficher()           # ← parenthèses manquaient
            if not resultat:
                print("Aucun professeur trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID      : {row[0]}
        Nom     : {row[1]}
        Matière : {row[2]}
                    """)

        elif choix == '3':
            id       = int(input("ID à rechercher : "))   # ← int
            resultat = db.rechercher(id)                   # ← rechercher pas afficher
            if resultat:
                print(f"""
        ID      : {resultat[0]}
        Nom     : {resultat[1]}
        Matière : {resultat[2]}
                """)
            else:
                print("Professeur non trouvé!")

        elif choix == '4':
            id      = int(input("ID à modifier : "))       # ← id manquait
            nom     = input("Nouveau nom : ").strip()
            matiere = input("Nouvelle matière : ").strip()
            db.modifier(id, nom, matiere)                  # ← id ajouté

        elif choix == '5':
            id = int(input("ID à supprimer : "))
            db.supprimer(id)

        elif choix == '0':                                 # ← '5' dupliqué → '0'
            break

        else:
            print("Choix invalide!")