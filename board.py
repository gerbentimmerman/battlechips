#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys
from random import randrange
from gewonnen import *
from verloren import *

class Board(QtGui.QWidget):
	def __init__(self):
		super(Board, self).__init__()
		self.counter = 0
		self.schiplengtes = [2,3,3,4,5]
		self.initUI()
		self.main(self.schiplengtes)
	
	def initUI(self):
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
				
		#Combobox Horizontaal/Verticaal schip
		self.horizonverticaalbox = QtGui.QComboBox()
		self.horizonverticaalbox.addItem("Horizontaal")
		self.horizonverticaalbox.addItem("Verticaal")
		self.grid.addWidget(self.horizonverticaalbox, 5, 0)
		
		self.plaatsbutton = QtGui.QPushButton("Schipplaatsen", self)
		self.lijstSchepenGebruiker = self.plaatsbutton.clicked.connect(self.plaatsen)
		self.grid.addWidget(self.plaatsbutton, 7, 0)
		
		
		
		self.show()
		
	def main(self, lengtes):
		self.lijstSchepenGebruiker = []
		self.schepenlengtes = lengtes
		if self.schepenlengtes == []:
			self.lijstSchepenComputer = self.schepenComputer()
			while self.lijstSchepenComputer or self.lijstSchepenGebruiker != []:
				self.shotComputer()
				self.schietenGebruiker()
			if self.lijstSchepenComputer == []:
				self.gewonnen = Windowgewonnen()
			if self.lijstSchepenGebruiker == []:
				self.verloren = Windowverloren()
			
	
	def counterschepen(self, counterschepen):
		self.counter = counterschepen + 1
		return self.counter
	
	def plaatsen(self):
		self.lengteschip = self.schepenlengtes[0]
		self.schepenlengtes.remove(self.schepenlengtes[0])
		self.lijstSchepenGebruiker = self.schepenGebruiker(self.lengteschip, self.lijstSchepenGebruiker)
		self.counter += 1
		
	def beginschip(self, lengte):
		self.lengteschip = lengte
		self.begincoord1, ok = QtGui.QInputDialog.getText(self,'Kies Begincoordinaat', 'Vul hier het begincoordinaat van het schip in welke ' + str(self.lengteschip) +' coordinaten lang is.')
		self.begin = str(self.begincoord1).split()
		x,y = int(self.begin[0]),int(self.begin[1])
		self.begincoord = (x,y)
		return self.begincoord
		
	def schepenGebruiker(self, lengte, lijstSchepenGebruiker):
		# lijst met daarin de lengtes van de schepen waar over je indenteert.
		self.lengte = lengte
		self.lijstSchepenGebruiker = lijstSchepenGebruiker
		self.begincoord = self.beginschip(self.lengte)
		x,y = self.begincoord[0], self.begincoord[1]
		self.tussencoord = [x,y]
		self.countercoord = 0
		if self.horizonverticaalbox.currentText() == "Horizontaal":
			while self.countercoord != self.lengte:
				y = self.tussencoord[1] + self.countercoord
				self.tussencoord1 = (self.tussencoord[0],y)
				if self.tussencoord1 in lijstSchepenGebruiker:
					QtGui.QMessageBox.information(self, "Error" , "Je schepen overlopen elkaar voer opnieuw de coordinaten in")
					self.lijstSchepenGebruiker = self.schepenGebruiker(self.lengteschip, self.lijstSchepenGebruiker)
				self.lijstSchepenGebruiker.append(self.tussencoord1)
				self.countercoord += 1
		if self.horizonverticaalbox.currentText() == "Verticaal":
			while self.countercoord != self.lengte:
				x = self.tussencoord[0] + self.countercoord
				self.tussencoord1 = (x,self.tussencoord[1])
				if self.tussencoord1 in lijstSchepenGebruiker:
					QtGui.QMessageBox.information(self, "Error" , "Je schepen overlopen elkaar voer opnieuw de coordinaten in")
					self.lijstSchepenGebruiker = self.schepenGebruiker(self.lengteschip, self.lijstSchepenGebruiker)
				self.lijstSchepenGebruiker.append(self.tussencoord1)
				self.countercoord += 1
		print(self.lijstSchepenGebruiker)
		return self.lijstSchepenGebruiker
		
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
					ycoord = y + counter
					self.begincoordcomputerschip = (x,ycoord)
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
			if hv == 1:
				while counter != item:
					xcoord = x + counter
					self.begincoordcomputerschip = (x,y)
					lijstSchepenComputer.append(self.begincoordcomputerschip)
					counter += 1
		print(lijstSchepenComputer)
		return lijstSchepenComputer
			
	def randomShotComputer(self):
		self.coord = (randrange(10), randrange(10))
		return self.coord
				
	def shotComputer(self):
		self.randomShot = self.randomShotComputer()
		coordrij, coordkolom = self.randomShot[0], self.randomShot[1]
		if self.randomShot in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Hap!!" , "Ai, de computer heeft een hap van je chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("iii"), coordrij+12, coordkolom)
			# kleur rood
			self.lijstSchepenGebruiker.remove(self.randomShot)
		if self.randomShot not in self.lijstSchepenGebruiker:
			QtGui.QMessageBox.information(self, "Pfiieuw!!" , "Oef, de computer miste zijn schot!")
			self.grid.addWidget(QtGui.QLabel("o"), coordrij+12, coordkolom)
			# kleur gemist
						
	def schietenGebruiker(self):
		self.coordShotGebruiker = self.gekozenCoordGebruiker()
		coordrij, coordkolom = self.coordShotGebruiker[0], self.coordShotGebruiker[1]
		if self.coordShotGebruiker in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Hap!!" , "Yess, je hebt een hap van het chipje genomen!")
			self.grid.addWidget(QtGui.QLabel("x"), coordrij, coordkolom)
			# kleur Groen
			self.lijstSchepenComputer.remove(self.coordShotGebruiker)
		elif self.coordShotGebruiker not in self.lijstSchepenComputer:
			QtGui.QMessageBox.information(self, "Chips!!" , "Helaas, je hebt geen schip geraakt!")
			self.grid.addWidget(QtGui.QLabel("iii"), coordrij, coordkolom)
			# Kleur gemist
		print(self.lijstSchepenComputer)
		
	def gekozenCoordGebruiker(self):
		self.schietcoord, ok = QtGui.QInputDialog.getText(self,'Kies Schietcoord', 'Vul hier je schietcoordinaat in met een spatie bijv.: 1 1')
		self.schietcoord = str(self.schietcoord).split()
		x,y = int(self.schietcoord[0]),int(self.schietcoord[1])
		self.begincoord = (x,y)
		return self.begincoord

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    board = Board()
    board.show()
    sys.exit(app.exec_())
