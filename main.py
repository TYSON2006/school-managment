from services.connect_authen import connet_users
from services.student_services import menu_students
from services.teacher_service import menu_teachers
from services.subjects_services import menu_subject
from services.grades_services import menu_grades

def main():
    role = connet_users()
    print(role)

    if role == 'admin':
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
            choix = input("faites un choix:").strip()
            if choix == '1':
                menu_students()
            elif choix == "2":
                menu_teachers()
            elif choix == '3':
                menu_subject()
            elif choix == '4':
               menu_grades()
            elif choix == '0':
                print("merci d'être passé!")
                break
            else:
                print("choix invalide!!")

    elif role == 'student':
        while True:
            print("""
=========================================
          ESPACE ÉTUDIANT
=========================================
  1. Voir mes informations
  2. Voir mes notes
  3. Voir mes absences
  0. Quitter
=========================================
            """)
            choix = input("Faites un choix : ").strip()

            if choix == '1':
                menu_students()
            elif choix == '2':
                menu_grades()
            elif choix == '3':
                pass  
            elif choix == '0':
                print("merci d'être passé")
                break
            else:
                print("Choix invalide!!")
    elif role == 'teachers':
        while True:
            print("""
=========================================
          ESPACE PROFESSEUR
=========================================
  1. Voir les matières
  2. Voir les notes
  0. Quitter
=========================================
                  """)  
            choix = input("faites un choix:").strip()
            if choix == '1':
                menu_subject()
            elif choix == '2':
                menu_grades()
            elif choix == '0':
                print("merci d'être passé")
                break 
            else:
                print("choix invalide !!")
        else:
            print("role non reconnu,accès interdit.")
if __name__ == "__main__":
    main()     

 
 
            
                  
                    
                    
          
            

    