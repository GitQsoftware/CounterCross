#conding utf-8
import sys
import sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

def hello():
    print("hello")

"""
Le graphique 
"""
#La fenetre

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
          
        #La fenetre et ses details
        title = "CounterCross"
        self.setWindowIcon(QtGui.QIcon('marathon.png'))
        self.setWindowTitle(title) 
        self.setGeometry(0, 0, 500, 300) 
        
        #Les labels
        Label = QLabel("Hello Word", self)
        Label.move(250, 150)
        Label.show()
        
        #Le menu bar
        self.title = title
        self.left = 250
        self.top = 250
        self.width = 400
        self.height = 300
        self.widget()

    def widget(self):
        # window setup
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        ## use above line or below
        # self.resize(self.width, self.height) # resizable
        self.setFixedSize(self.width, self.height)  # fixed size
        self.move(self.left, self.top)
        
        #Les menu quit 
        self.menubar1= self.menuBar()
        self.quitMenu = self.menubar1.addMenu("&Fichier")  # Add Help in menu bar
        self.about = self.quitMenu.addAction("&Quitter")  # Add option in Help
        self.about.setShortcut("CTRL + Q")
        self.about.triggered.connect(qApp.quit)
        #Les actions éventuelles
        
        #Help, info et credits
        self.menubar2= self.menuBar() # add menu bar
        self.helpMenu = self.menubar2.addMenu("&Help")  # Add Help in menu bar
        self.about = self.helpMenu.addAction("&About")  # Add option in Help
        self.about.setShortcut("F11") # display F11 as shortcut
        #self.about.triggered.connect(qApp.quit)
        self.credits = self.helpMenu.addAction("&Credits") # Add another option in Help
        self.show() 

app = QApplication(sys.argv) 
window = Window() 
sys.exit(app.exec()) 
