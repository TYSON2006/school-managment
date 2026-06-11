from models.students_models import students_using
from models.teachers_models import Teach_using
from models.users_models import globaUsers


class gestion:
    def __init__(self):
        self.students=students_using()
        self.teachers=Teach_using()
        self.users=globaUsers()






menu_utilisateur = """
=========================================
      GESTION D'UTILISATEURS
=========================================

     Bienvenue dans le module de
       gestion des utilisateurs

=========================================
"""

def ajout_users(self,nom,prenom):
    nom = input("nom:")
    prenom = input("prenom:") 

    