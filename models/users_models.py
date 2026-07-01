from database.connexion import MESDONNÉES
from utils.loggers import logger

class globaUsers(MESDONNÉES):
    def __init__(self):
        super().__init__()
        self.users_bord()

    def users_bord(self):
        try:
            self.curseur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom       TEXT NOT NULL,
                    pseudo    TEXT NOT NULL UNIQUE,
                    passeword TEXT NOT NULL,
                    role      TEXT NOT NULL
                )
            """)
            self.connexion.commit()
            logger.info("Table users créée")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def verification(self, pseudo, passeword):
        try:
            self.curseur.execute("""
                SELECT * FROM users WHERE pseudo = ? AND passeword = ?
            """, (pseudo, passeword))
            return self.curseur.fetchone()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def ajouter(self, nom,pseudo, passeword, role):
        try:
            self.curseur.execute("""
                INSERT INTO users (nom,pseudo, passeword, role)
                VALUES (?, ?, ?,?)
            """, (nom, pseudo,passeword, role))
            self.connexion.commit()
            logger.info("Utilisateur %s ajouté", nom)
            print("Utilisateur ajouté ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def dernier_id(self):
        return self.curseur.lastrowid

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
            print("Utilisateur modifié ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM users WHERE id = ?
            """, (id,))
            self.connexion.commit()
            logger.info("Utilisateur %s supprimé", id)
            print("Utilisateur supprimé ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")



    def close(self):
        self.connexion.close()
