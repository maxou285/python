# SQLITE : CRÉATION DE LA TABLE

import sqlite3

# connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums3.db")
curseur = connexion.cursor()

curseur.execute("CREATE TABLE artiste (artiste_id INTEGER NOT NULL PRIMARY KEY, nom VARCHAR);")
curseur.execute("CREATE TABLE album (album_id INTEGER NOT NULL PRIMARY KEY, artiste_id  INTEGER REFERENCES artiste, titre VARCHAR, annee_sortie INTEGER);")
curseur.execute('INSERT INTO artiste (nom) VALUES ("Michael Jackson");')
mj_id = curseur.lastrowid
curseur.execute('INSERT INTO artiste (nom) VALUES ("Celine Dion");')
cd_id = curseur.lastrowid
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(mj_id) + ',"Thriller", 1982);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ('+ str(cd_id) + ', "Falling into you" , 1996);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ',"Let\'s talk about you", 1997);')

connexion.commit()
connexion.close()

