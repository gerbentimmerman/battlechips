#!/usr/bin/python3

# Battlechips.py


import sys
from PyQt4 import QtGui, QtCore
from collections import Counter

class Battlechips(QtGui.QWidget):
	def __init__(self, argv):
		""" Constructor """
		super(Battlechips, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.setGeometry(100, 20, 800, 900)
		self.setWindowTitle("Battlechips")
		
		self.playButton = QtGui.QPushButton("Play", self)
		self.playButton.setGeometry(330,450,120,30)

	while lijstSchepenComputer or lijstSchepenGebruiker != []:
		
	def randomShotComputer(self):
		coord = (randrange(10), randrange(10))
		return coord
	
	def shotComputer(self):
		# De lijsten met Coordinaten moet eerder in het programma gedefinieerd worden
		# Zodat we ze hier aan een variabele kunnen toewijzen. 
		lijstSchepenGebruiker = [] # Lijst Bij het invoeren van coordinaten meegeven
		lijstAllGebruiker = [] # alle coordinaten 
		randomShot = randomShotComputer()
		if randomShot in lijstSchepenGebruiker:
			lijstSchepen.pop(randomShot)
			#melding Hit en weergeven in interface
		if randomShot not in lijstSchepenGebruiker:
			lijstAllGebruiker.pop(randomShot)
			#melding Miss en weergeven in interface
			
			
	def schietenGebruiker(self):
		lijstSchepenComputer = []
		lijstAllComputer = []
		coordShotGebruiker = gekozenCoordGebruiker()
		if coordShotGebruiker in LijstSchepenComputer:
			lijstSchepenComputer.pop(coordShotGebruiker)
			#melding Hit en weergeven in interface
		if coordShotGebruiker not in LijstSchepenComputer:
			lijstAllComputer.pop(coordShotGebruiker)
			#melding Miss en weergeven in interface
			
	def gekozenCoordGebruiker(self):
		coordShot = #input
		return coordShot
		
			
	

def main():
	app = QtGui.QApplication(sys.argv)
	uni = Battlechips(sys.argv)
	uni.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
