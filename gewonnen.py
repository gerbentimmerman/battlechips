#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()
		
	def initUI(self):
		
		self.resultlabel = QtGui.QLabel("GEFELICITEERD, JE HEBT GEWONNEN",self)
		self.resultlabel.setStyleSheet("color:purple;font: bold 18px;")
		self.resultlabel.move(160,280)
		
		self.vuurwerk = QtGui.QPixmap("fireworks.png")
		self.lbl = QtGui.QLabel(self)
		self.lbl.setPixmap(self.vuurwerk)
		self.lbl.move(200, 300)
		
		#maakt een window
		self.setGeometry(150, 150, 600, 600)
		self.setWindowTitle("Gewonnen")
		self.setStyleSheet("background-color: white")
		self.show()		
		
def main():
	app = QtGui.QApplication(sys.argv)
	uni = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
