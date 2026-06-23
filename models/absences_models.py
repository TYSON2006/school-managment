from database.connexion import  MESDONNÉES
from utils.loggers import logger



class absences_using(MESDONNÉES):
    def __init__(self):
        super.__init__()
    
def absences_bord(self):
    try:
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS absences(
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                date       TEXT NOT NULL,
                status     TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)
        self.connexion.commit()
        logger.info("Table absences créée")
    except Exception as e:
        logger.error(f"Erreur base de données : {e}")
        print("Une erreur est survenue.")
      
    

        
   

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

        
