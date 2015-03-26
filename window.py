#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPalette, QBrush, QPixmap
from board import Board

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()
	
	def initUI(self):
		"""Maakt startscherm aan (met zieke opmaak, dat wel) waar de gebruiker het spel kan starten """
		#de button om het spel te beginnen
		self.playButton = QtGui.QPushButton("Play", self)
		self.playButton.clicked.connect(self.playField)
		self.playButton.setStyleSheet("background-color: red;border-style: outset; border-radius:5px; font: bold 18px;")
		self.playButton.move(210,100)
		self.playButton.resize(150, 50)
		
		#zakje chips
		self.chips = QtGui.QPixmap("chips.png")
		self.lbl = QtGui.QLabel(self)
		self.lbl.setPixmap(self.chips)
		self.lbl.move(410, 300)
		
		#1 zak chips is nooit genoeg voor de heavy breathing cat
		self.chips2 = QtGui.QPixmap("chips.png")
		self.lbl2 = QtGui.QLabel(self)
		self.lbl2.setPixmap(self.chips)
		self.lbl2.move(30, 30)
		
		#pikachu in een sailor pakje, want battleships
		self.pikachu = QtGui.QPixmap("pikachu.png")
		self.lbl3 = QtGui.QLabel(self)
		self.lbl3.setPixmap(self.pikachu)
		self.lbl3.move(400,0)
		
		#een kat kan natuurlijk niet ontbreken
		self.kat = QtGui.QPixmap("hb2.jpeg")
		self.lblKat = QtGui.QLabel(self)
		self.lblKat.setPixmap(self.kat)
		self.lblKat.move(0,230)
		
		#ons super vette logo #swek
		self.battlechipsPlaatje = QtGui.QPixmap("battleships.png")
		self.lblbattle = QtGui.QLabel(self)
		self.lblbattle.setPixmap(self.battlechipsPlaatje)
		self.lblbattle.move(180,10)
		
		#le window
		self.setGeometry(150, 150, 600, 600)
		self.setWindowTitle("Menu")
		self.setStyleSheet("background-color: #8e8f94")
		self.show()	
	
	def playField(self):
		self.close()
		self.board = Board()

def main():
	app = QtGui.QApplication(sys.argv)
	uni = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
