import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from znog import Window1
from odzk import Window2
from zi import Window3


class OknaDialogowe(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Dialogi')
        self.setWindowIcon(QIcon('img\\smiling_face.png'))
        menu = self.menuBar()
        dialogMenu = menu.addMenu('&Dialog')

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(p)
        
        self.nazwaOknaGlownego = QAction('Nazwa okna głównego', self,
                                         checkable=True )
        self.ustawKola = QAction('Ustaw koła', self)
        self.zmienIkone = QAction('Zmień ikonę', self)
        
        self.w1 = Window1(self)
        self.nazwaOknaGlownego.toggled.connect( self.w1Behawior )

        self.srednicaWewnetrzna = 100
        self.srednicaZewnetrzna = 190
        self.ustawKola.triggered.connect( self.w2Behawior )

        self.stan = 1;
        self.zmienIkone.triggered.connect( self.w3Behawior )
        
        dialogMenu.addAction(self.nazwaOknaGlownego)
        dialogMenu.addAction(self.ustawKola)
        dialogMenu.addAction(self.zmienIkone)
        
        self.show()
    
    def paintEvent(self, e):

        painter = QPainter()
        korekta = (self.frameGeometry().height() - self.geometry().height())/2
        center = QPoint( self.geometry().width()/2,
                         (self.geometry().height() + korekta)/2)
        
        painter.begin(self)
        painter.setPen( Qt.NoPen )
        
        painter.setBrush( Qt.gray )
        painter.drawEllipse( center, self.srednicaZewnetrzna/2,
                             self.srednicaZewnetrzna/2 )
        painter.setBrush( Qt.green )
        painter.drawEllipse( center, self.srednicaWewnetrzna/2,
                             self.srednicaWewnetrzna/2 )
        
        painter.end()
    
    def w1Behawior(self):
        if self.nazwaOknaGlownego.isChecked():
            self.w1.show()
        else:
            self.w1.reject()

    def w2Behawior(self):
        z, w, ok = Window2.getKolo(self.srednicaZewnetrzna,
                                   self.srednicaWewnetrzna)
        if ok:
            self.srednicaWewnetrzna = w
            self.srednicaZewnetrzna = z

    def w3Behawior(self):
       emoticonIndex, emoticon, ok = Window3.getEmoticon(self.stan)
       if ok:
           self.stan = emoticonIndex
           self.setWindowIcon( QIcon( emoticon ) )

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    od = OknaDialogowe()
    sys.exit(app.exec_())
