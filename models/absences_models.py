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