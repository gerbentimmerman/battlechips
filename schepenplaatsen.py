#!/usr/bin/python3

# schepenplaatsen.py
from PyQt4 import QtGui
from random import randrange
import sys

class SchepenKiezen(QtGui.QWidget):
	# de lijst: self.lijstSchepenGebruiker moet in de init van de interface gemaakt
	# worden.
    def __init__(self, combobox):
        super(SchepenKiezen, self).__init__()
        self.horizonverticaalbox = combobox
        self.lijstSchepenGebruiker = self.schepenGebruiker()
        self.lijstSchepenComputer = self.schepenComputer()
     
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
			
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	x = SchepenKiezen(sys.argv)
	x.show()
	sys.exit(app.exec_())
