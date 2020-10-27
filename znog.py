from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window1( QInputDialog ):
        
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setModal(False)
        self.setWindowTitle('Nazwa okna głównego')
        self.setOption(QInputDialog.NoButtons, True)
        self.setOption(QInputDialog.UseListViewForComboBoxItems, True)
        self.installEventFilter( self )
        self.setComboBoxEditable( True )

        self.tytuly = [ 'Dialogi' ]
        self.setComboBoxItems( self.tytuly )
        
        self.findChildren(QLabel)[0].setVisible(False)
        
        self.cb = self.findChildren(QComboBox)[0]
        self.cb.setMinimumWidth(300)
        self.cb.setCurrentIndex(0)
        self.cb.currentIndexChanged.connect(self.zmienTytul)

    def zmienTytul(self):
        self.parent().setWindowTitle( self.cb.currentText() )

    def closeEvent(self, evnt):
        evnt.ignore()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Escape:
                return True
            if event.key() == Qt.Key_Enter:
                return True
        return QWidget.eventFilter(self, obj, event)
