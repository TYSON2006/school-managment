from database.connexion import MESDONNÉES



class Teach_using(MESDONNÉES):
    def __int__(self):
        super().__init__()
        self.tech_bord



    def tech_bord(self):
        self.curseur.execute("""
CREATE TABLE IF NOT EXISTS teachers(
                             id  PRIMARY KEY AUTOINCREMENT,
                             nom NOT NULL,
                             matiere NOT NULL
                             )
                             """)
        self.connexion.commit()



# ajout 
   
    def ajout(self,nom,matiere):
        self.curseur.execute("""
INSERT INTO teachers(nom,matiere) VALUES (?,?)
                             """,(nom,matiere))
        self.connexion.commit()
   


# verification

    def verification(self,nom,passeword):
        self.curseur.execute("""
SELECT FROM * teachers  WHERE nom = ?  passeword = ?
                             """,(nom,passeword))
        self.connexion.commit

# afficher 

    def afficher(self,id):
        self.curseur.execute("""
SELECT * FROM teachers 
                             """)
        return self.curseur.fetchone()
    


# update 

    def  modifier(self,id,nom,matiere):
        self.curseur.execute("""
     
            UPDATE teachers  SET ,
            nom = ?, 
            WHERE id = ?,
            matiere = ?                                          
            
                             """,(nom,id,matiere))
        self.connexion.commit()



# supprimer 
    def  supprimer(self,id):
        self.curseur.execute("""
  DELETE FROM teachers WHERE id = ?
                             """,(id))
        self.connexion.commit()
        self.connexion.close()
