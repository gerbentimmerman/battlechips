#!/usr/bin/python

import sys
from PyQt4 import QtGui

class Interface(QtGui.QWidget):
	def __init__(self):
		super(Interface, self).__init__()
		self.initUI()
		
	def initUI(self):		
		
		
		self.setGeometry(100, 100, 800, 900)
		self.setWindowTitle("Battlechips")
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	uni = Interface()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()
