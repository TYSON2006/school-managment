from models.users_models import globaUsers

students = globaUsers()

MENU_STUDENTS = """

 
╔══════════════════════════════════════════════╗
║           GESTION DES ÉTUDIANTS             ║
╠══════════════════════════════════════════════╣
║  1  ➜ Ajouter un étudiant                   ║
║  2  ➜ Afficher tous les étudiants           ║
║  3  ➜ Rechercher un étudiant                ║
║  4  ➜ Modifier un étudiant                  ║
║  5  ➜ Supprimer un étudiant                 ║
╠══════════════════════════════════════════════╣
║  6  ➜ Nombre total d'étudiants              ║
║  7  ➜ Afficher les étudiants par classe     ║
╠══════════════════════════════════════════════╣
║  0  ➜ Quitter                               ║
╚══════════════════════════════════════════════╝



"""


while True:
    print("MENU_STUDENTS")
    choix = input("votre choix:")
    