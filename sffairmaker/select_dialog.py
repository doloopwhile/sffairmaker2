#encoding:shift-jis
from __future__ import division, print_function
__metaclass__ = type 
from sffairmaker.qutil import *

class SelectDialog(QDialog):
    def __init__(self, caption, strings, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setWindowTitle(caption)
        self._listWidget = QListWidget(parent=self)
        
        strings = [unicode(s) for s in strings]
        assert strings
        self._listWidget.addItems(strings)
        
        self.setLayout(vBoxLayout(
            (self._listWidget, 1),
            dialogButtons(self),
        ))
        
    def currentIndex(self):
        row = self._listWidget.currentRow()
        if 0 <= row < self._listWidget.count():
            return row
        else:
            return None
    
    def ask(self):
        if self.exec_():
            return self.currentIndex()
        else:
            return None
    
    @classmethod
    def get(cls, caption, strings, parent=None):
        return cls(caption, strings, parent=None).ask()
        

def main():
    app = QApplication([])
    
    i = SelectDialog.get(u"ああああ", [x*5 for x in u"かきくけこ"])
    print(i)
    
    
    

if "__main__" == __name__:
    main()