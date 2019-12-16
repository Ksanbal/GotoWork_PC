import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from funcs import *

now = datetime.now()

form_class = uic.loadUiType("UIs/Main_ver1.ui")[0]  # UI파일 연결


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setlabel_date()  # 현재 날짜로 업데이트
        self.setlabel_time()  # 현재 시간으로 업데이트
        self.setlabel_logo()  # 로고 업데이트

        self.btn_attendance.clicked.connect(self.pushbtn_attendance)  # 출근 버튼
        self.btn_leavework.clicked.connect(self.pushbtn_leavework)  # 퇴근 버튼

    # 메소드 모음

    def setlabel_date(self):  # label에 현재 날짜를 띄우는 메소드
        self.label_nowdate.setText('{0}.{1}.{2}'.format(now.year, now.month, now.day))

    def setlabel_time(self):  # label에 현재 시간을 띄워주는 메소드
        self.label_nowtime.setText('{0}시 {1}분'.format(now.hour, now.minute))

    def setlabel_logo(self):  # label에 로고를 넣는 메소드
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('img/bella_logo.png')
        self.qPixmapVar = self.qPixmapVar.scaled(201, 80)

        self.label_logo.setPixmap(self.qPixmapVar)  # 적용

    def pushbtn_attendance(self):  # 출근 기능을 실행하는 메소드
        print(" 출근")
        issuccess = attendance(self.lineEdit_name.text())

        if issuccess == True:
            QMessageBox.about(self, 'Success', '출근이 완료되었습니다.')
        else:
            QMessageBox.about(self, 'Error', '출근기록이 생성되지 않았습니다.')

    def pushbtn_leavework(self):  # 퇴근 기능을 실행하는 메소드
        print(" 퇴근")
        leavework(self.lineEdit_name.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass()
    myWindow.show()  # 프로그램 화면을 보여주는 코드
    app.exec_()  # 프로그램을 이벤트루프로 진입시키는 코드
