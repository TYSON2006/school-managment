from database.connexion import MESDONNÉES
from utils.loggers import logger

class absences_using(MESDONNÉES):
    def __init__(self):
        super().__init__()          # ← super() avec parenthèses
        self.absences_bord()        # ← appelé automatiquement

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
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def ajout(self, student_id, date, status):
        try:
            self.curseur.execute("""
                INSERT INTO absences (student_id, date, status)
                VALUES (?, ?, ?)
            """, (student_id, date, status))
            self.connexion.commit()
            logger.info("Absence ajoutée")
            print("Absence ajoutée ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def afficher(self):
        try:
            self.curseur.execute("SELECT * FROM absences")
            return self.curseur.fetchall()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def rechercher(self, id):
        try:
            self.curseur.execute("""
                SELECT * FROM absences WHERE id = ?
            """, (id,))             # ← SELCT → SELECT + FROM absences ajouté
            return self.curseur.fetchone()  # ← return manquait
        except Exception as e:
            logger.error("Erreur base de données : %s",e)

    def justifier(self, id, status):
        try:
            self.curseur.execute("""
                UPDATE absences
                SET status = ?
                WHERE id = ?
            """, (status, id))
            self.connexion.commit()
            logger.info("Absence mise à jour")
            print("Statut mis à jour ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM absences WHERE id = ?
            """, (id,))             # ← DELETE * → DELETE FROM
            self.connexion.commit()
            logger.info("Absence supprimée")
            print("Absence supprimée ")
        except Exception as e:
            logger.error("Erreur base de données : %s",e)