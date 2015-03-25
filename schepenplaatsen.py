#!/usr/bin/python3

# schepenplaatsen.py

class SchepenKiezen(self):
	# de lijst: self.lijstSchepenGebruiker moet in de init van de interface gemaakt
	# worden.
	def __init__(self):
		self.schepenGebruiker()
		self.schepenComputer()
		
	def beginschip(self):
		self.begincoord1 = QtGui.QInputDialog.getText(self, 'Kies Begincoordinaat', 'Vul hier het begincoordinaat van het schip en bepaal of hij horizontaal of verticaal neergezet wordt.')
		return self.begincoord1
		
	def eindschip(self, lengte):
		self.lengte = lengte
		self.eindcoord1 = QtGui.QInputDialog.getText(self, 'Kies Eindcoordinaat', 'Vul hier het eindcoordinaat wat' + self.lengte + 'coordinaten van het begincoordinaat afligt in.')
		return self.eindcoord1, self.lengte1
	
	def schepenGebruiker(self):
		# lijst met daarin de lengtes van de schepen waar over je indenteert.
		self.lijstlengtes = [2,3,3,4,5]
		self.lijstSchepenGebruiker = []
		for item in self.lijstlengtes:
			self.begincoord = beginschip()
			self.eindcoord, lengte = eindschip(item)
			counter = 0
			x,y = self.begincoord[0], self.begincoord[1]
			self.tussencoord = (x,y)
			if self.horizonverticaalbox.currentText() == "Horizontaal":
				while self.tussencoord != self.eindcoord1:
					self.tussencoord = (x,y+1)
					self.lijstSchepenGebruiker.append(self.tussencoord)
					counter += 1
				self.lijstSchepenGebruiker.append(self.eindcoord)
			if self.horizonverticaalbox.currentText() == "Verticaal":
				while self.tussencoord != self.eindcoord1:
					self.tussencoord = (x+1,y)
					self.lijstSchepenGebruiker.append(self.tussencoord)
					counter += 1
			if counter != lengte:
				self.lijstSchepenGebruiker = []
				self.schepengebruiker()
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
