#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore
from board import Board

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()
		
	def initUI(self):
		#nog een keer spelen
		self.playButton = QtGui.QPushButton("Play again", self)
		self.playButton.clicked.connect(self.playField)
		self.playButton.setStyleSheet("background-color: blue;border-style: outset; border-radius:5px; font: bold 18px;")
		self.playButton.move(160,520)
		self.playButton.resize(150, 50)
		
		#of stoppen
		self.quitButton = QtGui.QPushButton("Quit", self)
		self.quitButton.clicked.connect(self.quitField)
		self.quitButton.setStyleSheet("background-color: red;border-style: outset; border-radius:5px; font: bold 18px;")
		self.quitButton.move(315,520)
		self.quitButton.resize(150, 50)
		
		#Gefeliciteerd
		self.resultlabel = QtGui.QLabel("GEFELICITEERD, JE HEBT GEWONNEN",self)
		self.resultlabel.setStyleSheet("color:purple;font: bold 18px;")
		self.resultlabel.move(160,150)
		
		#vuurwerk plaatje
		self.vuurwerk = QtGui.QPixmap("fireworks.png")
		self.lbl = QtGui.QLabel(self)
		self.lbl.setPixmap(self.vuurwerk)
		self.lbl.move(200, 170)
		
		#maakt een window
		self.setGeometry(150, 150, 600, 600)
		self.setWindowTitle("Gewonnen")
		self.setStyleSheet("background-color: white")
		self.show()	
		
	def playField(self):
		self.close()
		self.board = Board()
	
	def quitField(self):
		self.close()	
		
def main():
	app = QtGui.QApplication(sys.argv)
	uni = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
