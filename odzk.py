from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window2( QDialog ):
        
    def __init__(self, z, w, parent):
        super().__init__(parent)
        self.zewnatrz = z
        self.wewnatrz = w
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ustaw koła')

        grid = QGridLayout()
        
        l1 = QLabel('Na zewnątrz')
        l2 = QLabel('Wewnątrz')
        l1.setAlignment(Qt.AlignRight)
        l2.setAlignment(Qt.AlignRight)
        grid.addWidget( l1, 0, 0, Qt.AlignVCenter | Qt.AlignRight )
        grid.addWidget( l2, 1, 0, Qt.AlignVCenter | Qt.AlignRight )

        self.sliderZewnatrz = QSlider(Qt.Horizontal,self)
        self.sliderWewnatrz = QSlider(Qt.Horizontal,self)
        self.textZewnatrz = QLineEdit(self)
        self.textWewnatrz = QLineEdit(self)
        self.podglad = QLabel(self)
        
        self.sliderZewnatrz.setMaximum(300)
        self.sliderWewnatrz.setMaximum(300)
        self.sliderZewnatrz.valueChanged.connect( self.sliderZewnatrzControl )
        self.sliderWewnatrz.valueChanged.connect( self.sliderWewnatrzControl )
        self.sliderZewnatrz.setValue(self.zewnatrz)
        self.sliderWewnatrz.setValue(self.wewnatrz)
        self.sliderZewnatrz.setMinimumWidth( 100 )
        self.sliderWewnatrz.setMinimumWidth( 100 )
        
        grid.addWidget( self.sliderZewnatrz, 0, 1)
        grid.addWidget( self.sliderWewnatrz, 1, 1)

        self.textZewnatrz.setMaxLength(3)
        self.textWewnatrz.setMaxLength(3)
        self.textZewnatrz.textEdited.connect( self.textZewnatrzControl )
        self.textWewnatrz.textEdited.connect( self.textWewnatrzControl )
        self.textZewnatrz.setMaximumWidth(25)
        self.textWewnatrz.setMaximumWidth(25)
        grid.addWidget( self.textZewnatrz, 0, 2)
        grid.addWidget( self.textWewnatrz, 1, 2)

        grid.setRowStretch( 2, 1 )
        grid.setRowMinimumHeight( 0, 30 )
        grid.setRowMinimumHeight( 1, 30 )

        exitBox = QHBoxLayout()
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        exitBox.addWidget(buttons)
        self.findChildren(QPushButton)[1].setText('Anuluj')
        self.findChildren(QPushButton)[1].setMinimumWidth( 150 )
        self.findChildren(QPushButton)[0].setMinimumWidth( 150 )

        #self.podglad.setMargin(5)
        self.podglad.setContentsMargins( 20, 2, 5, 2)

        contentBox = QHBoxLayout()
        contentBox.addLayout( grid )
        contentBox.addWidget( self.podglad )
        contentBox.setContentsMargins( 5, 5, 5, 5 )

        mainBox = QVBoxLayout()
        mainBox.addLayout( contentBox )
        mainBox.addLayout( exitBox )
        self.setLayout( mainBox )

    def sliderZewnatrzControl(self):
        self.zewnatrz = self.sliderZewnatrz.value()
        self.textZewnatrz.setText( str( self.zewnatrz ) )

    def sliderWewnatrzControl(self):
        self.wewnatrz = self.sliderWewnatrz.value()
        self.textWewnatrz.setText( str( self.wewnatrz ) )

    def textZewnatrzControl(self):
        validator = QIntValidator(0, 300)
        text = self.textZewnatrz.text()
        if validator.validate( text, 0 )[0] == QValidator.Acceptable:
            self.sliderZewnatrz.setValue(int(text))
        
    def textWewnatrzControl(self):
        validator = QIntValidator(0, 300)
        text = self.textWewnatrz.text()
        if validator.validate( text, 0 )[0] == QValidator.Acceptable:
            self.sliderWewnatrz.setValue(int(text))
    
    def paintEvent(self, e):
        obrazPodgladu = QPicture()
        painter = QPainter()
        center = QPoint( 51, 50 )
        
        painter.begin(obrazPodgladu)
        painter.setBrush( Qt.white )
        painter.drawRect(0, 0, 101, 100)

        painter.setPen( Qt.NoPen )
        painter.setBrush( Qt.gray )
        painter.drawEllipse( center, self.zewnatrz/6, self.zewnatrz/6 )
        painter.setBrush( Qt.white )
        painter.drawEllipse( center, self.wewnatrz/6, self.wewnatrz/6 )

        painter.end()
        self.podglad.setPicture( obrazPodgladu )

    @staticmethod
    def getKolo(z, w, parent = None):
        w2 = Window2(z, w, parent)
        result = w2.exec_()
        return ( w2.zewnatrz, w2.wewnatrz, result == QDialog.Accepted)
