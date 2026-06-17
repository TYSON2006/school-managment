from services.connect_authen import connet_users
from services.student_services import menu_students
from services.teacher_service import menu_teachers
from services.subjects_services import menu_subject
from services.grades_services import menu_grades

def main():
    role = connet_users()

    while True:
        print("""
=========================================
       SYSTÈME DE GESTION D'ÉCOLE
=========================================
  1. Gestion des étudiants
  2. Gestion des professeurs
  3. Gestion des matières
  4. Gestion des notes
  0. Quitter
=========================================
              """)
        choix = input("faite un choix :").strip()
        if choix == '1':
            menu_students()
        elif choix == '2':
            menu_teachers()
        elif choix == '3':
            menu_subject()
        elif choix == '4':
            menu_grades()
        elif choix == '0':
            print("à bientôt")
            break
        else:
            print("choix invalide!")
if __name__ == "__main__":
    main()
        

