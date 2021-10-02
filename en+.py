def main():
    app = QApplication(sys.argv)
    w = MainPage(title="PyQt5")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

"""
def add_yes():
    alert = QMessageBox()
    alert.setText('utilisateur ajouté avec succés')
    print("utilisateur ajouté avec succés")
    alert.exec_()

	



def add():
	connection = sqlite3.connect("exemple.sqlite")
	cursor = connection.cursor() 
	
	#ajout utilisateur (ligne)
	new_user = (cursor.lastrowid,"Pierre", "54")
	cursor.execute('INSERT INTO cours VALUES(?,?,?)', new_user)
	connection.commit()
	add_yes()
	
	connection.close


add()
"""