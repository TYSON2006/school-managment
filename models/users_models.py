from database.connexion import MESDONNÉES






class globaUsers(MESDONNÉES):
    def __init__(self):
        super().__init__()




        #verrification
    def verification(self,nom,passeword):
        self.curseur.execute("""
                            SELECT * FROM users WHERE nom = ? AND  passeword = ? 
                             """,(nom,passeword))



        #ajout



    def ajouter(self, nom, role):
        self.curseur.execute(
            "INSERT INTO users(nom, role) VALUES (?, ?)",
            (nom, role)
        )
        self.connexion.commit()



        # afficher


    def  affcicher (self,id):
        self.curseur.execute(
            "SELECT * FROM users"
        )
        return self.curseur.fetchone()
         
    


    # update

    def modifier (self,id,nom,role):
        self.curseur.execute( """
               
            UPDATE users
            SET nom = ?, role = ?
            WHERE id = ?
            
            
        """,(nom, role, id))
        self.connexion.commit()




        # delete 
    def supprimer(self,id):
        self.curseur.execute(""""
        DELETE FROM users WHERE id = ?
       """,(id) )
        self.connexion.commit()


    def  close(self):
        self.connexion.close()