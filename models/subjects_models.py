from database.connexion import MESDONNÉES



class subject_using(MESDONNÉES):
    def __init__(self):
        super().__init__()



    def subject_bord(self):

        self.curseur.execute("""
CREATE TABLE IF NOT EXISTS subject(
                             id INTEGER PREMARY KEY AUTOINCREMENT,
                             nom TEXT NOT NULL,
                             teachers_id INTEGER NOT NULL,
                             FOREIGN KEY (teachers_id)REFERENCES teachers(id)

                             )
                             """)
        self.connexion.commit()




#ajout 
    def ajout(self,nom,matiere):
        self.curseur.execute("""
            INSERT INTO subject(nom,matiere) VALUES (?,?) 
        """,(nom,matiere))
        self.connexion.commit()



# lister

    def lister(self,matiere):
        self.curseur.execute("""
SELCT * FROM WHERE  matiere = ?
                             """,(matiere))
        self.connexion.commit()






#affciher 

    def afficher(self,matiere):
        self.curseur.execute("""
SELECT * FROM WHERE matiere = ?
                             """)
        return self.curseur.fetchall()
    



#recherchere
    def rechercher(self,matiere):
        self.curseur.execute("""
SELECT * FROM WHERE matiere = ?
                             """)
        self.connexion.commit()



#supprimer


    def supprimer(self,matiere):
        self.curseur.execute("""
DELETE FROM subject WHERE matiere = ?
                             """,(matiere))
        self.connexion.commit()
        self.connexion.close()

    
