from models.teachers_models import Teach_using

import sys 


from config.menu import menu_connexion,menu_teacher

def menu_teachers():
    db = Teach_using()


    while True:
        print("""

==================================
        ESPACE TEACHER
==================================
  1. Ajouter une matière ,un nom
  2. Afficher tousles professeur
  3. Afficher un professeur
  4. Modifier un proffesseur
  5. Supprimer un professeur
  0. Retour
==================================
              """)
        choix = input("faire un choix:")
        if choix == '1':
            nom =input("ecrivez votre nom:")
            matiere = input("entrer votre matiere")
            db.ajout(nom,matiere)

        elif choix == '2':
            reusltat = db.afficher
            if not reusltat:
                print("aucun professeur trouvé")
            else :
                for row in reusltat:
                    print(f"""
              id : {row[0]}
             nom :{row[1]}
             matiere:{row[2]}
                          """)
                    print("merci d'être passé")
        elif choix == '3':
            id = input("id à rechercher:")
            db.afficher(id)
        elif choix == '4':
            nom = input("entrer le nouveau nom:")
            matiere = input("nouvelle matiere:")
            db.modifier(nom,matiere)
        elif choix == '5':
            id = int(input("id a supprimer:"))
            db.supprimer(id)
        elif choix == '5':
            break
        else:
            print("retour.")
        
        
       


