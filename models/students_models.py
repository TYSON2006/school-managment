from database.connexion import MESDONNÉES



class students_using(MESDONNÉES):
    def __int__(self):
        super().__init__()



    def students_bord(self):
        self.curseur.execute("""
CREATE TABLE IF NOT EXISTS  students(
                               id PREMARY KEY AUTOINCREMENT,
                               nom TEXT NOT NULL,
                               prenom TEXT  NOT NULL,
                               age INTEGER NOT NULL,
                               classe TEXT NOT  NULL,
                               matricule TEXT NOT NULL
                               )
       """ )
        self.connexion.commit()





#ajouter 

    def ajouter(self,nom,prenom,age,matricule,classe):
        self.curseur.execute("""
INSERT INTO students (nom,prenom,age,matricule,classe) VALUES (?,?,?,?,?)
                               """,(nom,prenom,age,matricule,classe))
        self.connexion.commit()



#update

    def modifier(self,id,age,nom,matricule):
        self.curseur.execute("""
            UPDATE teachers  SET ,
             nom = ?, 
            WHERE id = ?,
            matricule = ?,
            age = ?        
                               """,(nom,age,id,matricule))
        self.connexion.commit()



#verification

    def verifier(self,nom,passeword):
        self.curseur.execute("""
SELECT FROM * WHERE nom =? passeword = ?
                             """,(nom,passeword))
        self.connexion.commit()




#  afficher 

    def afficher(self,id):
        self.curseur.execute("""
SELECT * FROM students
                             """)
        return self.curseur.fetchone()
    






 # supprimer 
    def  supprimer(self,id):
        self.curseur.execute("""
  DELETE FROM teachers WHERE id = ?
                             """,(id))
        self.connexion.commit()
        self.connexion.close()

    


