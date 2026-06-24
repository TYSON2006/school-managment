from database.connexion import MESDONNÉES
from utils.loggers import logger

class grades_using(MESDONNÉES):
    def __init__(self):
        super().__init__()
        self.grades_bord()

    def grades_bord(self):
        try:
            self.curseur.execute("""
                CREATE TABLE IF NOT EXISTS grades(
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    students_id INTEGER NOT NULL,
                    subjects_id INTEGER NOT NULL,
                    notes       REAL NOT NULL,
                    FOREIGN KEY (students_id) REFERENCES students(id),
                    FOREIGN KEY (subjects_id) REFERENCES subjects(id)
                )
            """)
            self.connexion.commit()
        except Exception as e:
            logger.error(f"Erreur : %s",{e})

    def ajout(self, students_id, subjects_id, notes):
        if not (0 <= notes <= 20):
            print("Note non valide, doit être entre 0 et 20!")
            logger.warning("Note invalide rejetée")
            return False
        try:
            self.curseur.execute("""
                INSERT INTO grades (students_id, subjects_id, notes)
                VALUES (?, ?, ?)
            """, (students_id, subjects_id, notes))
            self.connexion.commit()
            print("Note ajoutée ")
            logger.info(f"Note {notes} ajoutée")
            return True
        except Exception as e:
            logger.error(f"Erreur : %s",{e})
            print("Une erreur est survenue.")

    def afficher(self):
        try:
            self.curseur.execute("SELECT * FROM grades")
            return self.curseur.fetchall()     # ← fetchall pas fetchone
        except Exception as e:
            logger.error(f"Erreur : %s",{e})

    def rechercher(self, id):
        try:
            self.curseur.execute("""
                SELECT * FROM grades WHERE id = ?
            """, (id,))                        # ← FROM grades manquait
            return self.curseur.fetchone()
        except Exception as e:
            logger.error(f"Erreur : s%",{e})

    def modifier(self, id, notes):
        try:
            self.curseur.execute("""
                UPDATE grades
                SET notes = ?
                WHERE id = ?
            """, (notes, id))                  # ← syntaxe UPDATE corrigée
            self.connexion.commit()
            logger.info(f"Note modifiée")
        except Exception as e:
            logger.error(f"Erreur : %s",{e})

    def supprimer(self, id):
        try:
            self.curseur.execute("""
                DELETE FROM grades WHERE id = ?
            """, (id,))
            self.connexion.commit()
            logger.info("Note supprimée")
        except Exception as e:
            logger.error(f"Erreur : %s",{e})

    def calculer(self, students_id):
        try:
            self.curseur.execute("""
                SELECT notes FROM grades WHERE students_id = ?
            """, (students_id,))
            notes = self.curseur.fetchall()
            if not notes:
                print("Aucune note trouvée.")
                return 0
            totale = 0
            for note in notes:
                totale += note[0]
            moyenne = totale / len(notes)
            return moyenne
        except Exception as e:
            logger.error(f"Erreur : %s",{e})
            return 0