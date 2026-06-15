from database.connexion import MESDONNÉES

class grades_using(MESDONNÉES):
    def __init__(self):
        super().__init__()



    def grades_bord(self):
        self.curseur.execute("""
CREATE TABLE IF NOT EXISTS grades(
                             id INTEGER PREMARY KEY AUTOINCREMENT,
                             students_id INTEGER NOT NULL,
                             subjects_id INTEGER NOT NULL,
                             notes REAL NOT NULL CHECK(note >=0 and note <=20),
                             FOREIGN KEY(students_id)REFERENCES students(id)
                             FOREIGN KEY(subjects)REFERENCES subjects(id)
                             )
                             """)
        self.connexion.commit()
    


    # ajouter

    def ajout(self,students_id,subjects_id,notes):
        if (0 <= notes <=20 ):
            print(" non valide  note compris entre 0 et 20!")
            return False
        self.curseur.execute("""
INSERT INTO grades (students_id,subjects_id,notes) VALUES (?,?,?)
                             """,(students_id,subjects_id,notes))
        self.connexion.commit()


        return True
    
    #afficher 
    def affciher(self):
        self.curseur.execute("""
SELECT * FROM grades
                             """)
        return self.curseur.fetchall()
    


    #rechercher
    def rechercher(self,id):
        self.curseur.execute("""
SELECT *FROM WHERE id = ?
                             """,(id,))
        self.connexion.commit()
    
    


  