from database.connexion import  MESDONNÉES


class absences_using(MESDONNÉES):
    def __init__(self):
        super.__init__()
    

    def absences_using(self):
        self.curseur.execute("""
CREATE TABLE IF NOT EXISTS absences(
                             id INTEGER PREMARY KEY AUTOINCREMENT,
                             students_id NOT NULL,
                             date TEXT NOT NULL,
                             status TEXT NOT NULL,
                             FOREIGN KEY (students_id)REFERENCES students(id)
                             ) 
                             """)
        self.connexion.commit()
    


    #ajouter

    def ajout(self,student_id,date,status):
        self.curseur.execute("""
INSERT INTO absences (student_id,date,status) VALUES (?,?,?)
                             """,(student_id,date,status))
        self.connexion.commit()
    


    #afficher
    def afficher(self):
        self.curseur.execute("""
SELECT * FROM absences 
                             """)
        return self.curseur.fetchall()
    



    #rechercher

    def rechercher(self,id):
        self.curseur.execute("""
SELCT * FROM absences WHERE  id = ?
                             """,(id,))
        self.connexion.commit()
    


    #justifier

    def justifier(self,id,status):
        self.curseur.execute("""
        UPDATE absences
        SET status = ?
        WHERE id = ?
                             """,(status,id))
        self.connexion.commit()

    def supprimer(self,id):
        self.curseur.execute("""
DELETE  * FROM absences WHERE id = ?
                             """,(id,))
        self.connexion.commit()

        self
