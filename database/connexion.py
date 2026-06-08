
import sqlite3

class MESDONNÉES():
    def __init__(self):
        self.connexion = sqlite3.connect("terminal.db")
        self.curseur = self.connexion.cursor()

        self.connexion.commit()



    # creation de la table  users
    def users(self):
        self.curseur.execute("""
   CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        role TEXT NOT NULL
    )
       """ )
        


    # création de la table  students
    def students(self):
        self.curseur.execute("""
 CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricule INTEGER NOT NULL,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        age INTEGER NOT NULL,
        classe TEXT
    )
                             """)



# creation de la table teachers 
    
    def teachers(self):
        self.curseur.execute("""
  CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        matiere TEXT NOT NULL
    )
                             """)
        




    # creationde la table subject

    def subject(self):
        self.curseur.execute("""
 CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
                             """)
        

        # creationde la table grades 

    def grades(self):
        self.curseur.execute("""
 CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        note REAL NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
                             """)
        
        # creation de la table absences

    def absences(self):
        self.curseur.execute("""
 CREATE TABLE IF NOT EXISTS absences(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        status TEXT
    )
                             """)
            
