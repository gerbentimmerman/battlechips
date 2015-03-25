#!/usr/bin/python

import sys
from PyQt4 import QtGui

class Interface(QtGui.QWidget):
	def __init__(self):
		super(Interface, self).__init__()
		self.initUI()
		
	def myList(self):
		self.myList = []
		for i in range(10):
			self.myList.append('[] [] [] [] [] [] [] [] [] []')
		return self.myList
		
	def enemyList(self):
		self.swekList = []
		for i in range(10):
			self.swekList.append('[] [] [] [] [] [] [] [] [] []')
		return self.swekList
		
	def initUI(self):
		
		#Creates a window and sets layout
		self.setGeometry(100, 100, 400, 500)
		self.setWindowTitle("Battlechips")
		self.show()
		self.grid = QtGui.QGridLayout(self)
		self.grid.setVerticalSpacing(0)
		self.setLayout(self.grid)
		
		#Creates an Player field through Qlabels and lists
		self.playerSign =  QtGui.QLabel("Player Field")
		self.grid.addWidget(self.playerSign)
		for item in self.myList():
			self.playerField = QtGui.QLabel(item)
			self.grid.addWidget(self.playerField)
		
		#Creates an Enemy field through Qlabels and lists
		self.enemySign =  QtGui.QLabel("Enemy Field")
		self.grid.addWidget(self.enemySign)
		for item in self.enemyList():
			self.enemyField = QtGui.QLabel(item)
			self.grid.addWidget(self.enemyField)
		
		
		

def main():
	app = QtGui.QApplication(sys.argv)
	uni = Interface()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()
