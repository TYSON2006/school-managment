from database.connexion import MESDONNÉES
from utils.loggers import logger

class globaUsers(MESDONNÉES):
    def __init__(self):
        super().__init__()

    def verification(self, nom, passeword):
        try:
            self.curseur.execute("""
                SELECT * FROM users WHERE nom = ? AND passeword = ?
            """, (nom, passeword))
            return self.curseur.fetchone()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def ajouter(self, nom, passeword, role):
        try:
            self.curseur.execute("""
                INSERT INTO users (nom, passeword, role)
                VALUES (?, ?, ?)
            """, (nom, passeword, role))
            self.connexion.commit()
            logger.info("Utilisateur %s ajouté", nom)
            print("Utilisateur ajouté ✅")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def afficher(self):
        try:
            self.curseur.execute("SELECT * FROM users")
            return self.curseur.fetchall()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def modifier(self, id, nom, role):
        try:
            self.curseur.execute("""
                UPDATE users
                SET nom = ?, role = ?
                WHERE id = ?
            """, (nom, role, id))
            self.connexion.commit()
            logger.info("Utilisateur %s modifié", id)
            print("Utilisateur modifié ✅")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM users WHERE id = ?
            """, (id,))                     # ← triple quote + virgule corrigées
            self.connexion.commit()
            logger.info("Utilisateur %s supprimé", id)
            print("Utilisateur supprimé ✅")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def close(self):
        self.connexion.close()