#!/usr/bin/python3

# Battlechips.py

import sys
from PyQt4 import QtGui, QtCore
from random import randrange

class Battlechips():
    def __init__(self, lijstSchepenComputer, lijstSchepenGebruiker):
		super(Battlechips, self).__init__()
		self.lijstSchepenComputer = lijstSchepenComputer
		self.lijstSchepenGebruiker = lijstSchepenGebruiker
		self.main()
	
		def main(self):
			while self.lijstSchepenComputer or self.lijstSchepenGebruiker != []:
				self.shotComputer()
				self.schietenGebruiker()
				
		def randomShotComputer(self):
			coord = (randrange(10), randrange(10))
			return coord
			
		def shotComputer(self):
			# De lijsten met Coordinaten moeten in de init gedefinieerd worden
			# Zodat we ze hier aan een variabele kunnen toewijzen.
			# self.lijstSchepenGebruiker = [] # Lijst Bij het invoeren van coordinaten meegeven
			self.randomShot = randomShotComputer()
			coordrij, coordkolom = self.randomShot[0], self.randomShot[1]
			if self.randomShot in self.lijstSchepenGebruiker:
				self.QMessageBox.Information(self, "Raak!!" , "Ai, de computer heeft een van je schepen geraakt!")
				self.grid.addWidget(QtGui.QLabel("o"), coordrij+12, coordkolom)
				# kleur rood
				self.lijstSchepenGebruiker.pop(self.randomShot)
			if self.randomShot not in self.lijstSchepenGebruiker:
				self.QMessageBox.Information(self, "Mis!!" , "Oef, de computer misde zijn schot!")
				self.grid.addWidget(QtGui.QLabel("x"), coordrij, coordkolom)
				# kleur gemist
					
		def schietenGebruiker(self):
			self.lijstSchepenComputer = []
			self.coordShotGebruiker = gekozenCoordGebruiker()
			coordrij, coordkolom = self.coordShotGebruiker[0], self.coordShotGebruiker[1]
			if self.coordShotGebruiker in self.lijstSchepenComputer:
				self.QMessageBox.Information(self, "Raak!!" , "Yess, je hebt een schip geraakt!")
				self.grid.addWidget(QtGui.QLabel("o"), coordrij, coordkolom)
				# kleur Groen
				self.lijstSchepenComputer.pop(self.coordShotGebruiker)
				#melding Hit en weergeven in interface
			if self.coordShotGebruiker not in self.lijstSchepenComputer:
				QMessageBox.Information(self, "Mis!!" , "Helaas, je hebt geen schip geraakt!")
				self.grid.addWidget(QtGui.QLabel("x"), coordrij, coordkolom)
				# Kleur gemist

		def gekozenCoordGebruiker(self):
			self.coordShot = QtGui.QInputDialog.getText(self, 'Schiet Coordinaat', 'Vul hier een coordinaat tussen haakjes in waarop je wilt schieten bijv. (1,1)')
			if self.coordShot != (range(1,11), range(1,11)):
				self.QMessageBox.Information(self, " Input Error" , "Je moet een coordinaat tussen haakjes invullen bijv. (6,9)")
				gekozenCoordGebruiker()
			return self.coordShot
			

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	x = Battlechips(sys.argv)
	x.show()
	sys.exit(app.exec_())
