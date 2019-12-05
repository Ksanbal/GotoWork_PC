import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

now = datetime.now()

form_class = uic.loadUiType("UIs/Login.ui")[0]  # UI파일 연결


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setdatelabel()
        self.setlogolabel()

    def setdatelabel(self):  # label에 현재 날짜를 띄우는 메소드
        self.label_nowdate.setText('{0}.{1}.{2}'.format(now.year, now.month, now.day))

    def setlogolabel(self):  # label에 로고를 넣는 메소드
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('img/bella_logo.png')
        self.qPixmapVar = self.qPixmapVar.scaled(271, 121)

        self.label_logo.setPixmap(self.qPixmapVar)  # 적용


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()
    myWindow.show()  # 프로그램 화면을 보여주는 코드
    app.exec_()  # 프로그램을 이벤트루프로 진입시키는 코드
