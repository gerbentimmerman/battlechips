#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore
from board import *

class Windowverloren(QtGui.QWidget):
	def __init__(self):
		super(Windowverloren, self).__init__()
		self.initUI()
		
	def initUI(self):
		#nog een keer spelen
		self.playButton = QtGui.QPushButton("Play again", self)
		self.playButton.clicked.connect(self.playField)
		self.playButton.setStyleSheet("background-color: blue;border-style: outset; border-radius:5px; font: bold 18px;")
		self.playButton.move(160,520)
		self.playButton.resize(150, 50)
		
		#of niet
		self.quitButton = QtGui.QPushButton("Quit", self)
		self.quitButton.clicked.connect(self.quitField)
		self.quitButton.setStyleSheet("background-color: red;border-style: outset; border-radius:5px; font: bold 18px;")
		self.quitButton.move(315,520)
		self.quitButton.resize(150, 50)
		
		#verloren :(
		self.resultlabel = QtGui.QLabel("Helaas, je hebt verloren (hoe dan?)",self)
		self.resultlabel.setStyleSheet("color:blue;font: bold 18px;")
		self.resultlabel.move(160,150)
		
		#huiliehuilie plaatje
		self.huiliehuilie = QtGui.QPixmap("huilie.jpg")
		self.lbl = QtGui.QLabel(self)
		self.lbl.setPixmap(self.huiliehuilie)
		self.lbl.move(200, 200)
		
		#maakt een window
		self.setGeometry(150, 150, 600, 600)
		self.setWindowTitle("Loser")
		self.setStyleSheet("background-color: white")
		self.show()	
		
	def playField(self):
		self.close()
		self.board = Board()
	
	def quitField(self):
		self.close()	
		
def main():
	app = QtGui.QApplication(sys.argv)
	uni = Windowverloren()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
