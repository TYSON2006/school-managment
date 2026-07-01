from database.connexion import MESDONNÉES
from utils.loggers import logger

class students_using(MESDONNÉES):
    def __init__(self):
        super().__init__()
        self.students_bord()

    def students_bord(self):
        try:
            self.curseur.execute("""
                CREATE TABLE IF NOT EXISTS students(
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id   INTEGER NOT NULL,
                    matricule TEXT NOT NULL,
                    nom       TEXT NOT NULL,
                    prenom    TEXT NOT NULL,
                    age       INTEGER NOT NULL,
                    classe    TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            self.connexion.commit()
            logger.info("Table students créée")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def ajouter(self, user_id, nom, prenom, age, matricule, classe):
        try:
            self.curseur.execute("""
                INSERT INTO students (user_id, matricule, nom, prenom, age, classe)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, matricule, nom, prenom, age, classe))
            self.connexion.commit()
            logger.info("Étudiant %s ajouté", nom)
            print("Étudiant ajouté ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def modifier(self, id, pseudo,nom, age, matricule):
        try:
            self.curseur.execute("""
                UPDATE students
                SET nom = ?, age = ?, matricule = ?, pseudo= ?
                WHERE id = ?
            """, (nom, age, matricule, id))
            self.connexion.commit()
            logger.info("Étudiant %s modifié", id)
            print("Étudiant modifié ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")

    def afficher(self):
        try:
            self.curseur.execute("SELECT * FROM students")
            return self.curseur.fetchall()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def rechercher(self, id):
        try:
            self.curseur.execute("""
                SELECT * FROM students WHERE id = ?
            """, (id,))
            return self.curseur.fetchone()
        except Exception as e:
            logger.error("Erreur base de données : %s", e)

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM students WHERE id = ?
            """, (id,))
            self.connexion.commit()
            logger.info("Étudiant %s supprimé", id)
            print("Étudiant supprimé ")
        except Exception as e:
            logger.error("Erreur base de données : %s", e)
            print("Une erreur est survenue.")
