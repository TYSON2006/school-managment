from models.students_models import students_using
from config.menu import menu_students

def menu_students():
    db = students_using()

    while True:
        print(menu_students)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            nom       = input("Nom : ")
            prenom    = input("Prénom : ")
            age       = int(input("Âge : "))
            matricule = input("Matricule : ")
            classe    = input("Classe : ")
            db.ajouter(nom, prenom, age, matricule, classe)
            print("Étudiant ajouté ")

        elif choix == '2':
            resultat = db.afficher()
            if not resultat:
                print("Aucun étudiant trouvé!")
            else:
                for row in resultat:
                    print(f"""
        ID        : {etudiant[0]}
        Matricule : {etudiant[1]}
        Nom       : {etudiant[2]}
        Prénom    : {etudiant[3]}
        Âge       : {etudiant[4]}
        Classe    : {etudiant[5]}
                    """)

        elif choix == '3':
            id       = int(input("ID à rechercher : "))
            etudiant = db.rechercher(id)      
            if etudiant:
                print(f"""
        ID        : {etudiant[0]}
        Matricule : {etudiant[1]}
        Nom       : {etudiant[2]}
        Prénom    : {etudiant[3]}
        Âge       : {etudiant[4]}
        Classe    : {etudiant[5]}
                """)
            else:
                print("Aucun étudiant trouvé!")  

        elif choix == '4':
            id        = int(input("ID à modifier : "))
            nom       = input("Nouveau nom : ")         
            age       = int(input("Nouvel âge : "))      
            matricule = input("Nouveau matricule : ")
            db.modifier(id, nom, age, matricule)

        elif choix == '5':
            id = int(input("ID à supprimer : "))
            db.supprimer(id)

        elif choix == '0':
            break

        else:
            print("Choix invalide!")