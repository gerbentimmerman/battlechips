#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys

class Board(QtGui.QWidget):
    def __init__(self):
        super(Board, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 600, 600)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)

		#Spelers veld
        for y in range(1, 11):
            for x in range(1, 11):
                coord = (x, y)
                self.coordslist = QtGui.QLabel("(" + str(x) + "," + str(y) + ")")
                self.grid.addWidget(self.coordslist, x+10, y+10)
                
		#Tegenstander
        for y in range(1, 11):
            for x in range(1, 11):
                coord = (x, y)
                self.computercoordslist = QtGui.QLabel("(" + str(x) + "," + str(y) + ")")
                self.grid.addWidget(self.computercoordslist, x, y)
		
        #Combobox Horizontaal/Verticaal schip
        self.horizonverticaalbox = QtGui.QComboBox()
        self.horizonverticaalbox.addItem("Horizontaal")
        self.horizonverticaalbox.addItem("Verticaal")
        self.grid.addWidget(self.horizonverticaalbox, 5,0)

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    board = Board()
    board.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
