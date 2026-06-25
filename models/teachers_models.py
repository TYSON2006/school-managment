from database.connexion import MESDONNÉES
from utils.loggers import logger

class Teach_using(MESDONNÉES):
    def __init__(self):                     # ← __int__ → __init__
        super().__init__()
        self.tech_bord()                    # ← () manquaient

    def tech_bord(self):
        try:
            self.curseur.execute("""
                CREATE TABLE IF NOT EXISTS teachers(
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom     TEXT NOT NULL,
                    matiere TEXT NOT NULL
                )
            """)
            self.connexion.commit()
            logger.info("Table teachers créée")
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})
            print("Une erreur est survenue.")

    def ajout(self, nom, matiere):
        try:
            self.curseur.execute("""
                INSERT INTO teachers (nom, matiere)
                VALUES (?, ?)
            """, (nom, matiere))
            self.connexion.commit()
            logger.info("Professeur %s ajouté", nom)
            print("Professeur ajouté ")
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})
            print("Une erreur est survenue.")

    def afficher(self):                     # ← id inutile retiré
        try:
            self.curseur.execute("SELECT * FROM teachers")
            return self.curseur.fetchall()  # ← fetchall pas fetchone
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})

    def modifier(self, id, nom, matiere):
        try:
            self.curseur.execute("""
                UPDATE teachers
                SET nom = ?, matiere = ?
                WHERE id = ?
            """, (nom, matiere, id))        # ← syntaxe UPDATE corrigée
            self.connexion.commit()
            logger.info("Professeur %s modifié", id)
            print("Professeur modifié ")
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})
            print("Une erreur est survenue.")

    def rechercher(self, id):               # ← verification() remplacée par rechercher()
        try:
            self.curseur.execute("""
                SELECT * FROM teachers WHERE id = ?
            """, (id,))
            return self.curseur.fetchone()
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM teachers WHERE id = ?
            """, (id,))                     # ← (id) → (id,)
            self.connexion.commit()
            logger.info("Professeur %s supprimé", id)
            print("Professeur supprimé ")
        except Exception as e:
            logger.error("Erreur base de données : %s", {e})
            print("Une erreur est survenue.")