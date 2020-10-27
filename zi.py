from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window3( QDialog ):
        
    def __init__(self, stanPoczotkowy, parent):
        super().__init__(parent)
        self.stanInt = stanPoczotkowy
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wybierz ikone')

        stan = ["wesoła", "normalna", "smutna"]
        self.sciezka = ['img\\smiling_face.png', 'img\\neutral_face.png',
                   'img\\sad_face.png']
        self.wartoscWskaznika = [ 80, 50, 20 ]
        
        self.radioButton = []
        self.checkBox = []
        self.grupaRadioButtonow = QButtonGroup()
        self.grupaCheckBoxow = QButtonGroup()
        vBoxRB = QVBoxLayout()
        vBoxCB = QVBoxLayout()
        groupBoxRB = QGroupBox('Wybierz ikone')
        groupBoxCB = QGroupBox('Wybierz ikone')
        
        i = 1;
        for s in stan:
            rb = QRadioButton( s )
            self.radioButton.append( rb )
            self.grupaRadioButtonow.addButton( rb )
            self.grupaRadioButtonow.setId(rb, i)
            vBoxRB.addWidget( rb )
            
            cb = QCheckBox( s )
            cb.setAutoExclusive( True )
            self.checkBox.append( cb )
            self.grupaCheckBoxow.addButton( cb )
            self.grupaCheckBoxow.setId(cb, i)
            vBoxCB.addWidget( cb )

            if i == self.stanInt:
                rb.setChecked( True )
                cb.setChecked( True )
            i = i + 1
            
        groupBoxRB.setLayout( vBoxRB )
        groupBoxCB.setLayout( vBoxCB )
        self.grupaCheckBoxow.buttonClicked.connect( self.noChange )
        self.grupaRadioButtonow.buttonClicked.connect( self.change )

        self.emoticon = QLabel(self)
        self.emoticon.setPixmap( QPixmap( self.sciezka[ self.stanInt-1 ] ) )

        wskaznikBox = QVBoxLayout()
        self.wskaznik = QProgressBar(self)
        self.wskaznik.setOrientation( Qt.Vertical )
        self.wskaznik.setMinimum(0)
        self.wskaznik.setMaximum(100)
        self.wskaznik.setValue( self.wartoscWskaznika[ self.stanInt-1 ] )
        wskaznikBox.addWidget( self.wskaznik )
        wskaznikPodpis = QLabel('Wskaznik \nzadowolenia',self)
        wskaznikBox.addWidget( wskaznikPodpis )

        exitBox = QVBoxLayout()
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Vertical, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        exitBox.addWidget(buttons)

        mainBox = QGridLayout()
        mainBox.addWidget( groupBoxRB, 0, 0 )
        mainBox.addWidget( groupBoxCB, 1, 0 )
        mainBox.addWidget( self.emoticon, 0, 1 )
        mainBox.addLayout( wskaznikBox, 1, 1 )
        mainBox.addLayout( exitBox, 0, 2 )
        self.setLayout( mainBox )

    def noChange(self):
        self.grupaCheckBoxow.button( self.stanInt ).setChecked( True )

    def change(self):
        self.stanInt = self.grupaRadioButtonow.checkedId()
        self.grupaCheckBoxow.button( self.stanInt ).setChecked( True )
        self.emoticon.setPixmap( QPixmap( self.sciezka[ self.stanInt-1 ] ) )
        self.wskaznik.setValue( self.wartoscWskaznika[ self.stanInt-1 ] )

    @staticmethod
    def getEmoticon(stanPoczotkowy, parent = None):
        w3 = Window3(stanPoczotkowy, parent)
        result = w3.exec_()
        return ( w3.stanInt, w3.sciezka[ w3.stanInt-1 ], result == QDialog.Accepted)
        
        
