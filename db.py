import sqlite3
from tkinter.messagebox import showerror, showinfo

try:
	
	connection = sqlite3.connect("exemple.sqlite")
	cursor = connection.cursor() 
	
	#ajout utilisateur (ligne)
	new_user = (cursor.lastrowid,"Joseph", "43")
	cursor.execute('INSERT INTO cours VALUES(?,?,?)', new_user)
	connection.commit()
	showinfo('Good !',"utilisateur(s) ajouté(e)(s) avec succès")
	

	
except Exception as e:
	showerror("[ERREUR]",e)
	print("[Erreur]",e)
	connection.rollback()

finally:
	connection.close


"""
	#Connection
	connection = sqlite3.connect("db.sqlite")
	cursor = connection.cursor() 
	
	#lecture des données
	req = cursor.execute('SELECT * FROM users')
	
	for row in req.fetchall():
		print(row[1])
"""
"""
#ajout utilisateur (ligne)
new_user = (cursor.lastrowid,"Marc", "sa")
cursor.execute('INSERT INTO users VALUES(?,?,?)', new_user)
connection.commit()
showinfo("utilisateur(s) ajouté(e)s avec succès")
"""

"""
#Selection user
user_login = ("Quentin",)
cursor.execute('SELECT * FROM users WHERE user_login = ?', user_login)		
name = cursor.fetchone()[1]
showinfo("Bienvenue : {name}")
print(f"Bienvenue : {name}")
"""

#fermeture
