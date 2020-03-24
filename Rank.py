from PySide2 import QtGui,QtWidgets
from PySide2.QtWidgets import (QLineEdit,QPushButton,QApplication,QVBoxLayout,QDialog,QLabel,QWidget)
import time,sys

class Rank(QDialog):
    def __init__(self,rankList,string1,string2):
        super().__init__()
        self.layout=QVBoxLayout()
        label=QLabel(self)
        label.setText("\t\t\t\t"+string1+"\t\t\t\t")
        self.layout.addWidget(label)
        for i in range(1,len(rankList)+1):
            self.updateData(i,rankList[i-1],string2)
        self.setLayout(self.layout)
    def updateData(self,position,player,string2):
        label=QLabel(self)
        label.setText("\t{} {}:\t{}".format(string2,position,player))
        self.layout.addWidget(label)

if __name__=="__main__":
    app=QApplication([])
    rank=Rank([1,2,3],'RankList','Position')
    rank.show()
    app.exec_()
    sys.exit(0)


