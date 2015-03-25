#!/usr/bin/python3

# schepenplaatsen.py
from PyQt4 import QtGui

class SchepenKiezen(QtGui.QWidget):
	# de lijst: self.lijstSchepenGebruiker moet in de init van de interface gemaakt
	# worden.
    def __init__(self, lijstschepencomputer, lijstschepengebruiker, combobox):
        super(SchepenKiezen, self).__init__()
        self.lijstSchepenGebruiker = lijstschepengebruiker
        self.lijstSchepenComputer = lijstschepencomputer
        self.horizonverticaalbox = combobox
        self.schepenGebruiker()
        self.schepenComputer()

    def beginschip(self):
        self.begin = QtGui.QInputDialog.getText(self,'Kies Begincoordinaat', 'Vul hier het begincoordinaat van het schip en bepaal \n of hij horizontaal of verticaal neergezet wordt.')
        return self.begin
		
    def eindschip(self, lengte):
		self.lengte = lengte
		self.eind = QtGui.QInputDialog.getText(self,'Kies Eindcoordinaat', 'Vul hier het eindcoordinaat wat' + str(self.lengte) + 'coordinaten van het begincoordinaat afligt in.')
		return self.eind, self.lengte
	
    def schepenGebruiker(self):
		# lijst met daarin de lengtes van de schepen waar over je indenteert.
		self.lijstlengtes = [2,3,3,4,5]
		for item in self.lijstlengtes:
			self.begincoord = self.beginschip()
			self.lijstSchepenGebruiker.append(self.begincoord)
			self.eindcoord, lengte = self.eindschip(item)
			counter = 0
			x,y = self.begincoord[0], self.begincoord[1]
			self.tussencoord = (x,y)
			if self.horizonverticaalbox.currentText() == "Horizontaal":
				while self.tussencoord != self.eindcoord:
					x,y = self.tussencoord[0], self.tussencoord[1] + int(1)
					self.tussencoord = (x,y)
					self.lijstSchepenGebruiker.append(self.tussencoord)
					counter += 1
					print(self.lijstSchepenGebruiker)
				self.lijstSchepenGebruiker.append(self.eindcoord)
			if self.horizonverticaalbox.currentText() == "Verticaal":
				while self.tussencoord != self.eindcoord:
					x,y = self.tussencoord[0] + 1, self.tussencoord[1]
					self.tussencoord = (x,y)
					self.lijstSchepenGebruiker.append(self.tussencoord)
					counter += 1
				self.lijstSchepenGebruiker.append(self.eindcoord)
			if counter != lengte:
				self.lijstSchepenGebruiker = []
				self.schepenGebruiker()
			"""# Aanpassen fout
			if self.begincoord or self.tussencoord or self.eindcoord in self.lijstSchepenGebruiker:
				self.lijstSchepenGebruiker = []
				self.schepenGebruiker()"""
		
		
    def schepenComputer(self):
		self.lijstlengtes = [2,3,3,4,5]
		for item in self.lijstlengtes:
			self.begincoordcomputerschip = (randrange(1,11),randrange(1,11))
			self.lijstSchepenComputer.append(self.begincoordcomputerschip)
			(x,y) = self.begincoordcomputerschip[0], self.begincoordcomputerschip[1]
			hv = randrange(2)
			if hv == 0:
				self.eindcoordcomputerschip = (x,y + item)
				while self.begincoordcomputerschip != self.eindcoordcomputerschip:
					self.begincoordcomputerschip = (x,y+1)
					self.lijstSchepenComputer.append(self.begincoordcomputerschip)
				
			if hv == 1:
				self.eindcoordcomputerschip = (x + item,y)
				while self.begincoordcomputerschip != self.eindcoordcomputerschip:
					self.begincoordcomputerschip = (x+1,y)
					self.lijstSchepenComputer.append(self.begincoordcomputerschip)
			self.lijstSchepenComputer.append(self.eindcoordcomputerschip)
			
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	x = SchepenKiezen(sys.argv)
	x.show()
	sys.exit(app.exec_())
