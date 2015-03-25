#!/usr/bin/python
import sys
from PyQt4 import QtGui
from board import Board

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()
	
	def initUI(self):
		self.playButton = QtGui.QPushButton("Play", self)
		self.playButton.clicked.connect(self.playField)
		self.playButton.move(150, 150)
		self.playButton.resize(100, 20)
		
		self.setGeometry(150, 150, 600, 600)
		self.setWindowTitle("Menu")
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
