from database.connexion import MESDONNÉES
from utils.loggers import logger

def menu_stats():
    db = MESDONNÉES()

    while True:
        print("""
=========================================
          STATISTIQUES
=========================================
  1. Meilleur étudiant
  2. Moyenne générale
  3. Nombre total d'absences
  0. Retour
=========================================
        """)

        choix = input("Faites un choix : ").strip()

        if choix == '1':
            try:
                db.curseur.execute("""
                    SELECT students_id, AVG(notes) as moyenne
                    FROM grades
                    GROUP BY students_id
                    ORDER BY moyenne DESC
                    LIMIT 1
                """)
                resultat = db.curseur.fetchone()
                if resultat:
                    # récupérer le nom de l'étudiant
                    db.curseur.execute("""
                        SELECT nom, prenom FROM students WHERE id = ?
                    """, (resultat[0],))
                    etudiant = db.curseur.fetchone()
                    if etudiant:
                        print(f"""
=========================================
  Meilleur étudiant : {etudiant[0]} {etudiant[1]}
  Moyenne           : {resultat[1]:.2f}/20
=========================================
                        """)
                    logger.info("Meilleur étudiant consulté")
                else:
                    print("Aucune note enregistrée.")
            except Exception as e:
                logger.error("Erreur : %s", e)
                print("Une erreur est survenue.")

        elif choix == '2':
            try:
                db.curseur.execute("SELECT AVG(notes) FROM grades")
                resultat = db.curseur.fetchone()
                if resultat[0] is not None:
                    print(f"""
=========================================
  Moyenne générale : {resultat[0]:.2f}/20
=========================================
                    """)
                else:
                    print("Aucune note enregistrée.")
                logger.info("Moyenne générale consultée")
            except Exception as e:
                logger.error("Erreur : %s", e)
                print("Une erreur est survenue.")

        elif choix == '3':
            try:
                db.curseur.execute("SELECT COUNT(*) FROM absences")
                resultat = db.curseur.fetchone()
                print(f"""
=========================================
  Nombre total d'absences : {resultat[0]}
=========================================
                """)
                logger.info("Absences comptées")
            except Exception as e:
                logger.error("Erreur : %s", e)
                print("Une erreur est survenue.")

        elif choix == '0':
            break

        else:
            print("Choix invalide!")