#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys
from random import randrange
from gewonnen import *
from verloren import *

class Board(QtGui.QWidget):
	def __init__(self):
		"""Constructor"""
		super(Board, self).__init__()
		self.counter = 0
		self.schiplengtes = [2,3,3,4,5]
		self.initUI()
		self.main(self.schiplengtes)
	
	def initUI(self):
		""" Window gemaakt met een speelveld"""
		self.setGeometry(150, 150, 600, 600)
		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)
		
		# Speler veld maken
		for y in range(1, 11):
			 for x in range(1, 11):
				 coord = (x, y)
				 self.coordslist = QtGui.QLabel("(" + str(x) + "," + str(y) + ")")
				 self.grid.addWidget(self.coordslist, x + 12, y)
				 self.grid.addWidget(QtGui.QLabel("Lijn"), 11, 5)
				 
		# Computer veld maken
		for y in range(1, 11):
			for x in range(1, 11):
				coord = (x, y)
				self.computercoordslist = QtGui.QLabel("(" + str(x) + "," + str(y) + ")")
				self.grid.addWidget(self.computercoordslist, x, y)
					
		# Combobox voor keuze Horizontaal/Verticaal richting schip
		self.horizonverticaalbox = QtGui.QComboBox()
		self.horizonverticaalbox.addItem("Horizontaal")
		self.horizonverticaalbox.addItem("Verticaal")
		self.grid.addWidget(self.horizonverticaalbox, 5, 0)
		
		# Knop om schepen plaatsen te bevestigen
		self.plaatsbutton = QtGui.QPushButton("Schipplaatsen", self)
		self.lijstSchepenGebruiker = self.plaatsbutton.clicked.connect(self.plaatsen)
		self.grid.addWidget(self.plaatsbutton, 7, 0)
		
		# Knop om schieten te starten als de schepen zijn geplaatst
		self.schietbutton = QtGui.QPushButton("Start Schieten", self)
		self.buttonschiet = self.schietbutton.clicked.connect(self.startSchieten)
		self.grid.addWidget(self.schietbutton, 9, 0)
		
		self.show()
		
		QtGui.QMessageBox.information(self, "Spel Uitleg" , "Hallo, welkom bij Battlechips.\nZorg ervoor dat je eerst de richting van het schip bepaald in de combobox. Klik dan op plaats schepen knop en vul het begin coordinaat van het schip in om het schip te plaatsen. \nDe schepen worden in de volgende volgorde \ningevuld: 2,3,3,4,5. \nWees geen cheater en zorg ervoor dat de eindcoordinaten van de schepen binnen de grid blijven. Dus zorg als je coordinaten bij lengte 2 hebt minstens coordinaten van de kant zit.\nEr zijn 5 schepen als je die geplaatst heb kun je op het schietknopje klikken")

	def main(self, lengtes):
		""" Lijst van schepen maken en de lengtes van de schepen toewijzen"""
		self.lijstSchepenGebruiker = []
		self.schepenlengtes = lengtes
		
	def startSchieten(self):
		"""Verloop van het spel wanneer je op de schietknop geklikt hebt"""
		self.lijstSchepenComputer = self.schepenComputer()
		
		# Totdat een van de twee lijsten leeg is blijf je doorgaan met schieten
		while len(self.lijstSchepenComputer) or len(self.lijstSchepenGebruiker) != 0:
			self.shotComputer()
			self.schietenGebruiker()
			# Als een van de twee lijsten leeg is ga je over tot de eindschermen
			if len(self.lijstSchepenComputer) == 0:
				self.close()
				self.gewonnen = Windowgewonnen()
			if len(self.lijstSchepenGebruiker) == 0:
				self.close()
				self.verloren = Windowverloren()

	def plaatsen(self):
		"""Lengte van schip inlezen en meegeven aan de functie Schepenmaken"""
		self.lengteschip = self.schepenlengtes[0]
		self.schepenlengtes.remove(self.schepenlengtes[0])
		self.lijstSchepenGebruiker = self.schepenGebruiker(self.lengteschip, self.lijstSchepenGebruiker)
		self.counter += 1
		return self.lijstSchepenGebruiker
		
	def beginschip(self, lengte):
		""" De gebruiker zijn begincoordinaat laten kiezen en returnen"""
		self.lengteschip = lengte
		
		# Input met spatie geven
		self.begincoord1, ok = QtGui.QInputDialog.getText(self,'Kies Begincoordinaat', 'Vul hier het begincoordinaat van het schip in welke ' + str(self.lengteschip) +' coordinaten lang is.')
		self.begin = str(self.begincoord1).split()
		x,y = int(self.begin[0]),int(self.begin[1])
		self.begincoord = (x,y)
		return self.begincoord
		
	def schepenGebruiker(self, lengte, lijstSchepenGebruiker):
		"""Functie die de schepen van de gebruiker plaatst en toevoegd aan de lijst"""
		self.lengte = lengte
		
		# Lijst toewijzen
		self.lijstSchepenGebruiker = lijstSchepenGebruiker
		
		# Begincoord ophalen uit functie beginschip
		self.begincoord = self.beginschip(self.lengte)
		x,y = self.begincoord[0], self.begincoord[1]
		self.tussencoord = [x,y]
		self.countercoord = 0
		
		# Als Combobox horizontaal staat voer deze if uit
		if self.horizonverticaalbox.currentText() == "Horizontaal":
			# Als de counter nog niet gelijk is aan de lengte van het schip voer blijf je coordinaten toevoegen
			while self.countercoord != self.lengte:
				y = self.tussencoord[1] + self.countercoord
				self.tussencoord1 = (self.tussencoord[0],y)
				# Toevoegen aan de lijst
				self.grid.addWidget(QtGui.QLabel("____"), self.tussencoord1[0] + 12, self.tussencoord1[1])
				self.lijstSchepenGebruiker.append(self.tussencoord1)
				self.countercoord += 1
		
		# Als Combobox verticaal staat voer deze if uit
		if self.horizonverticaalbox.currentText() == "Verticaal":
			# Als de counter nog niet gelijk is aan de lengte van het schip voer blijf je coordinaten toevoegen
			while self.countercoord != self.lengte:
				x = self.tussencoord[0] + self.countercoord
				self.tussencoord1 = (x,self.tussencoord[1])
				self.grid.addWidget(QtGui.QLabel("____"), self.tussencoord1[0] + 12, self.tussencoord1[1])
				# Toevoegen aan de lijst
				self.lijstSchepenGebruiker.append(self.tussencoord1)
				self.countercoord += 1
		
		print(self.lijstSchepenGebruiker)
		return self.lijstSchepenGebruiker
		
	def schepenComputer(self):
		"""Functie waarin de computer de coordinaten plaatst"""
		self.lijstlengtes = [2,3,3,4,5]
		lijstSchepenComputer = []
		for item in self.lijstlengtes:
			# random coord
			counter = 0
			hv = randrange(2)
			# Horizontaal if
			if hv == 0:
				self.begincoordcomputerschip = (randrange(1,11),randrange(1,11 - item))
				x,y = self.begincoordcomputerschip[0], self.begincoordcomputerschip[1]
				# ycoord + 1 totdat hij gelijk is aan lengte schip 
				while counter != item:
					ycoord = y + counter
					self.begincoordcomputerschip = (x,ycoord)
					if self.begincoordcomputerschip in lijstSchepenComputer:
						self.lijstSchepenComputer = []
						self.lijstSchepenComputer = self.schepenComputer
					# coord toevoegen aan lijst
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
			# Verticaal if
			if hv == 1:
				self.begincoordcomputerschip = (randrange(1,11 - item ),randrange(1,11))
				x,y = self.begincoordcomputerschip[0], self.begincoordcomputerschip[1]
				# xcoord + 1 totdat hij gelijk is aan lengte schip 
				while counter != item:
					xcoord = x + counter
					self.begincoordcomputerschip = (xcoord,y)
					if self.begincoordcomputerschip in lijstSchepenComputer:
						self.lijstSchepenComputer = []
						self.lijstSchepenComputer = self.schepenComputer
					# coord toevoegen aan lijst
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
		print(lijstSchepenComputer)
		return lijstSchepenComputer
			
	def randomShotComputer(self):
		""" De Computer selecteert willekeurige getallen die in een coordinaat worden gezet """
		self.coord = (randrange(1,11), randrange(1,11))
		return self.coord
				
	def shotComputer(self):
		""" Computer schiet op het speelveld van de Gebruiker"""
		self.randomShot = self.randomShotComputer()
		coordrij, coordkolom = self.randomShot[0], self.randomShot[1]
		if self.randomShot in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Hap!!" , "Ai, de computer heeft een hap van je chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("XXX"), coordrij+12, coordkolom)
			
			# Haal coord uit de lijst als hij geraakt is
			self.lijstSchepenGebruiker.remove(self.randomShot)
		elif self.randomShot not in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Pfiieuw!!" , "Oef, de computer miste zijn schot!")
			self.grid.addWidget(QtGui.QLabel("MMM"), coordrij+12, coordkolom)
			# kleur gemist
						
	def schietenGebruiker(self):
		""" Gebruiker schiet op het speelveld van de Computer """
		# Functie aanroepen om coord te returnen
		self.coordShotGebruiker = self.gekozenCoordGebruiker()
		
		coordrij, coordkolom = self.coordShotGebruiker[0], self.coordShotGebruiker[1]
		#Coordinaat vergelijken met lijst van schepen Computer
		if self.coordShotGebruiker in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Hap!!" , "Yess, je hebt een hap van het chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("XXX"), coordrij, coordkolom)
			self.grid.addWidget(QtGui.QLabel("____"), self.coordShotGebruiker[0], self.coordShotGebruiker[1])
			# Haal coord uit de lijst als hij geraakt is
			self.lijstSchepenComputer.remove(self.coordShotGebruiker)
		
		# Miss weergeven in scherm
		elif self.coordShotGebruiker not in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Chips!!" , "Helaas, je hebt geen schip geraakt!")
			self.grid.addWidget(QtGui.QLabel("MMM"), coordrij, coordkolom)
			# Kleur gemist
		print(self.lijstSchepenComputer)
		
	def gekozenCoordGebruiker(self):
		""" Gebruiker geeft coordinaat om te schieten """
		# Input met spatie
		self.schietcoord, ok = QtGui.QInputDialog.getText(self,'Kies Schietcoord', 'Vul hier je schietcoordinaat in met een spatie bijv.: 1 1')
		self.schietcoord = str(self.schietcoord).split()
		x,y = int(self.schietcoord[0]),int(self.schietcoord[1])
		self.begincoord = (x,y)
		return self.begincoord

if __name__ == "__main__":
	"""Runnen van Programma"""
	app = QtGui.QApplication(sys.argv)
	board = Board()
	board.show()
	sys.exit(app.exec_())
