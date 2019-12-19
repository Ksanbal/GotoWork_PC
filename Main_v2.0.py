import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from funcs import *

now = datetime.now()

login_class = uic.loadUiType('UIs/Login.ui')[0]  # 로그인창 ui 연결
signup_class = uic.loadUiType('UIs/Signup.ui')[0]
main_class = uic.loadUiType("UIs/Main_v2.ui")[0]  # 메인창 ui 연결


# 로그인창
class LoginWindowClass(QDialog, login_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setlabel_date()
        self.setlabel_logo()

        self.btn_signin.clicked.connect(self.pushbtn_signin)
        self.btn_signup.clicked.connect(self.pushbtn_signup)

    # 메소드 모음
    def setlabel_date(self):  # label에 현재 날짜를 띄우는 메소드
        self.label_nowdate.setText('{0}.{1}.{2}'.format(now.year, now.month, now.day))

    def setlabel_logo(self):  # label에 로고를 넣는 메소드
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('img/bella_logo.png')
        self.qPixmapVar = self.qPixmapVar.scaled(280, 101)

        self.label_logo.setPixmap(self.qPixmapVar)  # 적용

    def pushbtn_signin(self):  # 로그인 기능
        id = self.lineEdit_id.text()
        passwd = self.lineEdit_passwd.text()
        result, issuccess = signin(id, passwd)
        if issuccess:  # 로그인 성공
            ok = QMessageBox.information(None, 'Notice', result)

            if ok:  # 확인버튼 클릭 후 메인창 띄우고, 로그인 정보 전달
                self.close()
                mainWindow = MainWindowClass(id)
                mainWindow.exec_()
        else:
            QMessageBox.about(None, 'Notice', result)

    def pushbtn_signup(self):  # 회원가입 기능
        print('signup')
        signupWindow = SignupWindowClass()
        signupWindow.exec_()


# 회원가입 창
class SignupWindowClass(QDialog, signup_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_confirm.clicked.connect(self.confirm)
        self.btn_cancel.clicked.connect(self.cancel)

    def confirm(self):
        try:
            name = self.lineEdit_name.text()
            nickname = self.lineEdit_nickname.text()
            birth = self.lineEdit_birth.text()
            id = self.lineEdit_id.text()
            passwd = self.lineEdit_passwd.text()
            result, issuccess = signup(name, nickname, birth, id, passwd)
            QMessageBox.about(None, 'Notice', result)
        except Exception as ex:
            print(ex)

        if issuccess:
            self.close()

    def cancel(self):
        print('취소')
        self.close()


# 메인창
class MainWindowClass(QDialog, main_class):
    def __init__(self, nowid):
        super().__init__()
        self.setupUi(self)
        self.nowid = nowid
        print(nowid)
        self.setlabel_date()  # 현재 날짜로 업데이트
        self.setlabel_time()  # 현재 시간으로 업데이트
        self.setlabel_logo()  # 로고 업데이트

        # self.btn_attendance.clicked.connect(self.pushbtn_attendance)  # 출근 버튼
        # self.btn_leavework.clicked.connect(self.pushbtn_leavework)  # 퇴근 버튼

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
        result = attendance(self.lineEdit_name.text())
        QMessageBox.about(None, 'Notice', result)

    def pushbtn_leavework(self):  # 퇴근 기능을 실행하는 메소드
        print(" 퇴근")
        result = leavework(self.lineEdit_name.text())

        QMessageBox.about(None, 'Notice', result)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 프로그램을 실행시켜주는 클래스
    loginWindow = LoginWindowClass()
    loginWindow.show()
    app.exec_()  # 프로그램을 이벤트루프로 진입시키는 코드
