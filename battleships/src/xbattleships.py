#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Copyright 2010 Laurie Clark-Michalek (Blue Peppers) <bluepeppers@archlinux.us>
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep
import battleshipslib
import images
import sys

log = battleshipslib.log
IP = battleshipslib.ip
PORT = battleshipslib.port

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(':/LOGO.png'))
size = 50
EMPTY = QPixmap(':/EMPTY.png').scaled(size,size)
HIT = QPixmap(':/HIT.png').scaled(size,size)
MISS = QPixmap(':/MISS.png').scaled(size,size)
SHIP = QPixmap(':/SHIP.png').scaled(size,size)

VERTFRONT = QPixmap(':/VERTFRONT.png').scaled(size,size)
VERTBACK = QPixmap(':/VERTBACK.png').scaled(size,size)
HORIBACK = QPixmap(':/HORIBACK.png').scaled(size,size)
HORIFRONT = QPixmap(':/HORIFRONT.png').scaled(size,size)

def encode(input):
    output = []
    for char in input:
        if char == '.':
            output.append('l')
        else:
            output.append('abcdefghijk'[int(char)])
    return ''.join(output)

def decode(input):
    output = []
    for char in input:
        if char == 'l':
            output.append('.')
        else:
            output.append('0123456789'['abcdefghijk'.index(char)])
    return ''.join(output)

class square(QLabel):
    def __init__(self, row, column, parent=None, value="EMPTY"):
        super(square, self).__init__(parent)
        
        self.value = value
        
        self.setPixmap(eval(value))
        
        self.row = row
        
        self.column = column
    
    def changeType(self, value):
        if value in ["HORIFRONT", "HORIBACK", "VERTFRONT", "VERTBACK"]:
            self.value = "SHIP"
        else:
            self.value = value
        
        self.setPixmap(eval(value))

class ConnectionDialog(QDialog):
    def __init__(self, parent=None):
        super(ConnectionDialog, self).__init__(parent)
        
        clientlayout = QVBoxLayout()
        clientlayout.addWidget(QLabel('<center><h4>If you have a connection code'))
        clientlayout.addWidget(QLabel('<center>Enter your connection code below'))
        self.Input = QLineEdit()
        clientlayout.addWidget(self.Input)
        
        serverlayout = QVBoxLayout()
        serverlayout.addWidget(QLabel('<center><h4>If you require a connection code'))
        serverlayout.addWidget(QLabel('<center>Your connection code is:\n\n'))
        serverlayout.addWidget(QLineEdit('%s' % encode(IP)))
        
        seperator = QFrame()
        seperator.setFrameShape(QFrame.VLine)
        
        mainsplitter = QHBoxLayout()
        mainsplitter.addLayout(clientlayout)
        mainsplitter.addWidget(seperator)
        mainsplitter.addLayout(serverlayout)
        
        layout = QVBoxLayout()
        layout.addLayout(mainsplitter)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)
        self.setLayout(layout)
        self.connect(buttonbox, SIGNAL('accepted ()'),
                     self.accept)
        self.connect(buttonbox, SIGNAL('rejected ()'),
                     self.reject)

class ReciveThread(QThread):
    
    over = pyqtSignal()
    
    def shot(self, parent):
        returncode = parent.game.reciveShot(type='NonBlocking')
        if returncode:
            parent.Output.append('\n\nOne of your ships was hit.')
            return True
        elif returncode == None:
            return None
        else:
            parent.Output.append('\n\nThe enemy missed.')
            return False
        
        parent.Output.append('\n\nPlease enter the coordinates you would like us to target')
    
    def run(self):
        self.parent.Output.append('\n\nWaiting for a shot.')
        
        shot = None
        while shot == None:
            try:
                shot = self.shot(self.parent)
            except battleshipslib.NetworkError:
                log ('Network Error')
                self.parent.NetworkErrorHandle.emit()
                return
            except battleshipslib.Shutdown:
                log ('Shutdown')
                self.parent.ShutdownHandle.emit()
                return
            self.msleep(200)
        
        self.over.emit()
        
        self.parent.presendShot()
        self.connect(self.parent.Input, SIGNAL("editingFinished ()"),
                                        self.parent.sendShot)  

class CheckThread(QThread):
    shutdown = pyqtSignal()
    def run(self):
        self.moving = 0
        while 1:
            status = self.parent.game.connection.check()
            if status[0]:
                self.moving += 1
                if self.moving >= self.parent.game.connection.timeout:
                    self.shutdown.emit()
                    return
            else:
                self.moving = 0
            self.msleep(200)
                    


class GameWindow(QMainWindow):
    NetworkErrorHandle = pyqtSignal()
    ShutdownHandle = pyqtSignal()
    
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        
        #GAME
        self.game = battleshipslib.board()
        self.game.ships = [3]
        
        self.VALUES = []
        self.SHOTS = []
        
        for row in range(0, len(self.game.values)):
            shots = []
            values = []
            for column in range(0, len(self.game.values[row])):
                shots.append(square(row, column))
                values.append(square(row, column))
            self.SHOTS.append(shots)
            self.VALUES.append(values)
        
        self.Output = QTextBrowser()
        Font = QFont()
        Font.setStyleHint(QFont.TypeWriter)
        Font.setFamily('Monospace')
        self.Output.setCurrentFont(Font)
        self.Output.setText('Welcome to BattLeships')
        self.Input = QLineEdit()
        
        self.statusBar().setSizeGripEnabled(False)
        
        self.createsetLayout()
        
        self.setWindowTitle('Battleships')
        
        
        menu = self.menuBar()
        file = menu.addMenu('&File')
        
        connect = self.createAction('Connect', shortcut='Ctrl+N', slot=self.createConnection, icon='CONNECT')
        file.addAction(connect)
        
        quit = self.createAction('Quit',shortcut='Ctrl+Q', slot=self.close)
        file.addAction(quit)
        
        content = ['Place ships please. Lengths are: 5, 4, 3, 2, 2',
                   '\n\nEnter coordinates in the form \'A1,B3\', with A1 being the start of the ship, and B3 being the end',
                   '\n\n']
        
        self.Output.setText(''.join(content))
        
        self.connect(self.Input, SIGNAL("editingFinished ()"),
                                        self.placeShip)
        
        self.NetworkErrorHandle.connect(self.NetworkError)
        self.ShutdownHandle.connect(self.Shutdown)
    
    def createConnection(self):
        dialog = ConnectionDialog()
        if dialog.exec_():
            text = decode(dialog.Input.text())
            
            if len(text.split('.')) == 4:
                try:
                    self.game.connection.setClient(text)
                #except Exception, e:
                 #   log(Exception, e)
                  #  QMessageBox.critical(self, 'Error', 'Could not connect to the other player')
                else:
                    self.finishedConnecting()
            elif text == '':
                #Because the socket.accept() call blocks, this message will never be shown.
                #I don't think it is possible to fix this atm. Timeout on accept() maybe?
                #self.statusBar().showMessage('Waiting for other player to connect',15000)
                try:
                    self.game.connection.setServer()
                except Exception, e:
                    log(Exception, e)
                    QMessageBox.critical(self, 'Error', 'Could not connect to the other player')
                else:
                    self.finishedConnecting()
            else:
                QMessageBox.critical(self, 'Error', 'Invalid connection code')
        
    def finishedConnecting(self):
        self.statusBar().showMessage('Connected', 5000)
        if self.game.ships == []:
            if self.game.connection.type == "Server":
                self.presendShot()
                self.connect(self.Input, SIGNAL("editingFinished ()"),
                                self.sendShot)
            else:
                self.reciveShot()
                self.syncLists()
        
    def placeShip(self):
        input = self.Input.text().split(',')
        self.Input.setText('')
        if not str(input[0][0]).isalpha() and not str(input[0][1:]).isnumeric():
            return
        if not str(input[1][0]).isalpha() and not str(input[1][1:]).isnumeric():
            return
        start = input[0]
        start = (int(start[1:])-1,'ABCDEFGHIJKL'.index(unicode(start[0]).capitalize()))
        end = input[1]
        end = (int(end[1:])-1,'ABCDEFGHIJKL'.index(unicode(end[0]).capitalize()))
        returncode = self.game.placeShip(start, end)
        if returncode:
            self.syncLists()
            if self.game.ships == []:
                self.disconnect(self.Input, SIGNAL("editingFinished ()"),
                                            self.placeShip)
                self.Output.append('\n\nFinished placing ships')
                
            else:
                self.Output.append('\nYou have %i ships left to place %s' % (len(self.game.ships), str(tuple(self.game.ships))))
                return
        else:
            self.Output.append('\nInvalid coordinates')
            return
        self.Input.setText('')
        self.syncLists()
        try:
            self.game.connection.type
        except AttributeError:
            self.Output.append('\nShips placed, please now connect to your opponent')
            return
        
        
        if self.game.connection.type == "Server":
            self.presendShot()
            self.connect(self.Input, SIGNAL("editingFinished ()"),
                                    self.sendShot)
        else:
            self.reciveShot()
            self.syncLists()
    
    def reciveShot(self):
        
        self.thread = ReciveThread()
        self.thread.parent = self
        self.thread.start()
        self.thread.over.connect(self.syncLists)
    
    def presendShot(self):
        self.Output.append('\nEnter the coordinates for us to target')
        
        self.checkthread = CheckThread()
        self.checkthread.parent = self
        self.checkthread.start()
        self.checkthread.shutdown.connect(self.Shutdown)
        self.checkthread.shutdown.connect(self.checkthread.quit)
    
    def sendShot(self):
        
        coord = self.Input.text()
        self.Input.setText('')
        
        if coord == '':
            return
        try:
            if int(coord[1:]) > len(self.VALUES):
                raise ValueError
            coord = (int(coord[1:])-1,'ABCDEFGHIJKL'.index(coord[0]))
            log (coord)
        except ValueError:
            self.Output.append('\nInvalid coordinates')
            return
        
        self.checkthread.quit()
        
        self.disconnect(self.Input, SIGNAL("editingFinished ()"),
                                self.sendShot)
        
        returncode = self.game.sendShot(coord)
        if returncode:
            self.Output.append('\n\nYou hit the enemy.')
            if self.game.game == "WON":
                self.WonGame()
            elif self.game.game == "LOST":
                self.LostGame()
        else:
            self.Output.append('\n\nYou missed the enemy.' )
        
        
        self.reciveShot()
        self.syncLists()
    
    def close(self):
        self.game.close()
        app.quit()
        
    def WonGame(self):
        #TODO: Make sparkly
        QMessageBox.information(self, 'Won', 'You won the game. Well done')
        app.quit()
    
    def LostGame(self):
        #TODO: Make sparkly
        QMessageBox.information(self, 'Lost', 'You lost the game. Better luck next time')
        app.quit()
    
    def NetworkError(self):
        log ('Entered NetworkError()')
        QMessageBox.critical(self, 'Error', 'There appears to be a network error. This could mean that you have lost your internet connection. Battleships will now quit.')
        app.quit()
    
    def Shutdown(self):
        log ('Entered Shutdown()')
        QMessageBox.critical(self, 'Disconection', 'Your partner seems to have disconnected. Battleships cannot continue, and will now quit.')
        app.quit()
    
    def createsetLayout(self):
        Layout = QGridLayout()
        Layout.addLayout(self.createBoard(),0,0)
        Layout.addWidget(self.Output,1,0)
        Layout.addWidget(self.Input,2,0)
        Widget = QWidget()
        Widget.setLayout(Layout)
        self.setCentralWidget(Widget)
        
    def syncLists(self):
        def ship(value):
            if value == "SHIP":
                return True
            return False
        
        for row in range(0, len(self.game.values)):
            for column in range(0, len(self.game.values[row])):
                
                self.SHOTS[row][column].changeType(self.game.shots[row][column])
                
                if self.game.values[row][column] == "SHIP":
                    if row - 1 < 0:
                        above = "EMPTY"
                    else: 
                        above = self.game.values[row - 1][column]
                    if row + 1 == len(self.VALUES):
                        below = "EMPTY"
                    else:
                        below = self.game.values[row + 1][column]
                    if column - 1 < 0:
                        left = "EMPTY"
                    else:
                        left = self.game.values[row][column - 1]
                    if column + 1 == len(self.VALUES[0]):
                        right = "EMPTY"
                    else:
                        right = self.game.values[row][column + 1]
                    
                    if ship(above) and not ship(below):
                        self.VALUES[row][column].changeType("VERTBACK")
                    elif not ship(above) and ship(below):
                        self.VALUES[row][column].changeType("VERTFRONT")
                    elif ship(left) and not ship(right):
                        self.VALUES[row][column].changeType("HORIBACK")
                    elif not ship(left) and ship(right):
                        self.VALUES[row][column].changeType("HORIFRONT")
                    else:
                        self.VALUES[row][column].changeType("SHIP")
                    
                    continue
                
                self.VALUES[row][column].changeType(self.game.values[row][column])
    
    def createBoard(self):
        FullLayout = QGridLayout()
        
        ShotsFrame = QFrame()
        ShotsFrame.setFrameShape(QFrame.StyledPanel)
        ShotsFrame.setFrameShadow(QFrame.Sunken)
        ShotsLayout = QGridLayout()
        ShotsLayout.addWidget(QLabel("<h3><center><u>Shots"),0,0,1,len(self.game.values))
        
        ValuesFrame = QFrame()
        ValuesFrame.setFrameShape(QFrame.StyledPanel)
        ValuesFrame.setFrameShadow(QFrame.Sunken)
        ValuesLayout = QGridLayout()
        ValuesLayout.addWidget(QLabel("<h3><center><u>Ships"),0,0,1,len(self.game.values))
        
        for index, character in enumerate(' ABCDEFGHIJKL'):
            ShotsLayout.addWidget(QLabel('<center>' + character), 1, index)
            ValuesLayout.addWidget(QLabel('<center>' + character), 1, index)
        
        for row in range(0, len(self.game.values)):
            ShotsLayout.addWidget(QLabel('<center>' + str(row + 1)), row + 2, 0)
            ValuesLayout.addWidget(QLabel('<center>' + str(row + 1)), row + 2, 0)
            for column in range(0, len(self.game.values[row])):
                ShotsLayout.addWidget(self.SHOTS[row][column], row + 2, column + 1)
                ValuesLayout.addWidget(self.VALUES[row][column], row + 2, column + 1)
        
        ShotsFrame.setLayout(ShotsLayout)
        ValuesFrame.setLayout(ValuesLayout)
        
        FullLayout.addWidget(ShotsFrame, 0, 0)
        FullLayout.addWidget(ValuesFrame, 0, 1)
        
        
        return FullLayout
    
    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
    
        

game = GameWindow()
game.show()
app.exec_()
