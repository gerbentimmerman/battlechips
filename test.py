#!/usr/bin/python3

# Battlechips.py

import sys
from PyQt4 import QtGui, QtCore
from random import randrange

class Battlechips(QtGui.QWidget):
	def __init__(self, combobox):
		super(Battlechips, self).__init__()
		self.horizonverticaalbox = combobox
		self.lijstSchepenGebruiker = self.schepenGebruiker()
		self.lijstSchepenComputer = self.schepenComputer()
		self.main()
	
	def main(self):
		while self.lijstSchepenComputer or self.lijstSchepenGebruiker != []:
			self.shotComputer()
			self.schietenGebruiker()
	
	def beginschip(self, lengte):
		self.begin = tuple(QtGui.QInputDialog.getDouble(self,'Kies Begincoordinaat', 'Vul hier het begincoordinaat van het schip en bepaal \n of hij horizontaal of verticaal neergezet wordt.'))
		self.lengte = lengte
		return self.begin, self.lengte
		
	def schepenGebruiker(self):
		# lijst met daarin de lengtes van de schepen waar over je indenteert.
		self.lijstlengtes = [2,3,3,4,5]
		lijstSchepenGebruiker = []
		for item in self.lijstlengtes:
			self.begincoord, self.lengte = self.beginschip(item)
			x,y = self.begincoord[0], self.begincoord[1]
			self.tussencoord = [x,y]
			if self.horizonverticaalbox.currentText() == "Horizontaal":
				for nummer in range(self.lengte):
					self.tussencoord = (int(self.tussencoord[0]), int(self.tussencoord[1] + nummer))
					lijstSchepenGebruiker.append(self.tussencoord)
					print(lijstSchepenGebruiker)
			if self.horizonverticaalbox.currentText() == "Verticaal":
				for nummer in range(self.lengte):
					self.tussencoord = (int(self.tussencoord[0] + nummer), int(self.tussencoord[1]))
					lijstSchepenGebruiker.append(self.tussencoord)
		return lijstSchepenGebruiker
		"""# Aanpassen fout
			if self.begincoord or self.tussencoord or self.eindcoord in self.lijstSchepenGebruiker:
				self.lijstSchepenGebruiker = []
				self.schepenGebruiker()"""
		
	def schepenComputer(self):
		self.lijstlengtes = [2,3,3,4,5]
		lijstSchepenComputer = []
		for item in self.lijstlengtes:
			self.begincoordcomputerschip = (randrange(1,11),randrange(1,11))
			x,y = self.begincoordcomputerschip[0], self.begincoordcomputerschip[1]
			counter = 0
			hv = randrange(2)
			if hv == 0:
				while counter != item:
					self.begincoordcomputerschip = [x,y + counter]
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
			if hv == 1:
				while counter != item:
					self.begincoordcomputerschip = [x + counter,y]
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
		return lijstSchepenComputer
			
	def randomShotComputer(self):
		coord = (randrange(10), randrange(10))
		return coord
				
	def shotComputer(self):
		self.randomShot = self.randomShotComputer()
		coordrij, coordkolom = self.randomShot[0], self.randomShot[1]
		if self.randomShot in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Hap!!" , "Ai, de computer heeft een hap van je chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("o"), coordrij+12, coordkolom)
			# kleur rood
			self.lijstSchepenGebruiker.pop(self.randomShot)
		if self.randomShot not in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Chips!!" , "Oef, de computer miste zijn schot!")
			self.grid.addWidget(QtGui.QLabel("x"), coordrij, coordkolom)
			# kleur gemist
						
	def schietenGebruiker(self):
		self.coordShotGebruiker = self.gekozenCoordGebruiker()
		coordrij, coordkolom = self.coordShotGebruiker[0], self.coordShotGebruiker[1]
		if self.coordShotGebruiker in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Hap!!" , "Yess, je hebt een hap van het chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("o"), coordrij, coordkolom)
			# kleur Groen
			self.lijstSchepenComputer.pop(self.coordShotGebruiker)
		if self.coordShotGebruiker not in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Chips!!" , "Helaas, je hebt geen schip geraakt!")
			self.grid.addWidget(QtGui.QLabel("x"), coordrij, coordkolom)
			# Kleur gemist

	def gekozenCoordGebruiker(self):
		self.coordShot = QtGui.QInputDialog.getText(self, 'Schiet Coordinaat', 'Vul hier een coordinaat tussen haakjes in waarop je wilt schieten bijv. (1,1)')
		if self.coordShot != (range(1,11), range(1,11)):
			QtGui.QMessageBox.information(self, " Input Error" , "Je moet een coordinaat tussen haakjes invullen bijv. (6,9)")
			gekozenCoordGebruiker()
		return self.coordShot
			

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	x = Battlechips(sys.argv)
	x.show()
	sys.exit(app.exec_())
