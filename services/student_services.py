from models.students_models import students_using


import sys 




from config.menu import menu_connexion,menu_students













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
       

       if choix == '1':
           
           ajouter = input("veuiller ajouter un nom:")













