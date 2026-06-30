from database.connexion import MESDONNÉES
from utils.loggers import logger

class subject_using(MESDONNÉES):
    def __init__(self):
        super().__init__()
        self.subject_bord()

    def subject_bord(self):
        try:
            self.curseur.execute("""
                CREATE TABLE IF NOT EXISTS subjects(
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom        TEXT NOT NULL,
                    teacher_id INTEGER NOT NULL,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                )
            """)
            self.connexion.commit()
            logger.info("Table subjects créée")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def ajouter(self, nom, teacher_id):
        try:
            self.curseur.execute("""
                INSERT INTO subjects (nom, teacher_id)
                VALUES (?, ?)
            """, (nom, teacher_id))
            self.connexion.commit()
            logger.info("Matière %s ajoutée", nom)
            print("Matière ajoutée ✅")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def afficher(self):
        try:
            self.curseur.execute("SELECT * FROM subjects")
            return self.curseur.fetchall()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def rechercher(self, id):
        try:
            self.curseur.execute("""
                SELECT * FROM subjects WHERE id = ?
            """, (id,))
            return self.curseur.fetchone()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM subjects WHERE id = ?
            """, (id,))
            self.connexion.commit()
            logger.info("Matière %s supprimée", id)
            print("Matière supprimée ✅")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")
