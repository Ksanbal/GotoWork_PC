import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from funcs import *

# ui 연결
login_class = uic.loadUiType('UIs/Login.ui')[0]     # 로그인창
signup_class = uic.loadUiType('UIs/Signup.ui')[0]   # 회원가입창
main_class = uic.loadUiType("UIs/Main_v2.ui")[0]    # 메인창


# 로그인창
class LoginWindowClass(QDialog, login_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # lable 관리
        self.setlabel_date()
        self.setlabel_logo()

        # btn 관리
        self.btn_signin.clicked.connect(self.pushbtn_signin)
        self.btn_signup.clicked.connect(self.pushbtn_signup)

    # 메소드 모음
    # label 관련
    # label에 현재 날짜를 띄우는 메소드
    def setlabel_date(self):
        self.label_nowdate.setText('{0}.{1}.{2}'.format(now.year, now.month, now.day))

    # label에 로고를 넣는 메소드
    def setlabel_logo(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('img/bella_logo.png')
        self.qPixmapVar = self.qPixmapVar.scaled(280, 101)

        self.label_logo.setPixmap(self.qPixmapVar)  # 적용

    # btn 관련
    # 로그인 기능
    def pushbtn_signin(self):
        id = self.lineEdit_id.text()
        passwd = self.lineEdit_passwd.text()
        result, issuccess, isadmin = signin(id, passwd)
        if issuccess:  # 로그인 성공
            ok = QMessageBox.information(None, 'Notice', result)

            if ok:  # 확인버튼 클릭 후 메인창 띄우고, 로그인 정보와 권한 정보 전
                self.close()
                mainWindow = MainWindowClass(id, isadmin)
                mainWindow.exec_()
        else:
            QMessageBox.about(None, 'Notice', result)

    # 회원가입 기능
    def pushbtn_signup(self):
        print('signup')
        signupWindow = SignupWindowClass()
        signupWindow.exec_()


# 회원가입 창
class SignupWindowClass(QDialog, signup_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # btn 관리
        self.btn_confirm.clicked.connect(self.confirm)
        self.btn_cancel.clicked.connect(self.cancel)

    # 메소드 모음
    # btn 관련
    # 회원가입을 진행 기능
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

    # 회원가입 취소 기능
    def cancel(self):
        print('취소')
        self.close()


# 메인창
class MainWindowClass(QDialog, main_class):
    def __init__(self, nowid, isadmin):
        super().__init__()
        self.setupUi(self)
        self.nowid = nowid              # 현재 로그인한 사람의 id
        self.isadmin = isadmin          # 현재 로그인한 사람의 권환(True: admin, False: user)

        # lable 관리
        self.setlabel_logo()            # 로고 업데이트
        self.setlabel_date()            # 현재 날짜로 업데이트
        self.setlabel_time()            # 현재 시간으로 업데이트
        self.setlabel_welcome(nowid)    # 로그인한 계정의 닉네임으로 업데이트

        # btn 관리
        self.setDisablebtn_manage(isadmin)                              # 권한에 따른 관리버튼 활성화 비활성화
        self.btn_attendance.clicked.connect(self.pushbtn_attendance)    # 출근 버튼
        self.btn_leavework.clicked.connect(self.pushbtn_leavework)      # 퇴근 버튼

    # 메소드 모음
    # label 관련
    # label에 로고를 넣는 메소드
    def setlabel_logo(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load('img/bella_logo.png')
        self.qPixmapVar = self.qPixmapVar.scaled(201, 80)

        self.label_logo.setPixmap(self.qPixmapVar)  # 적용

    # label에 현재 날짜를 띄우는 메소드
    def setlabel_date(self):
        self.label_nowdate.setText('{0}.{1}.{2}'.format(now.year, now.month, now.day))

    # label에 현재 시간을 띄우는 메소드
    def setlabel_time(self):
        self.label_nowtime.setText('{0}시 {1}분'.format(now.hour, now.minute))

    # lable에 현재 로그인한 게정의 닉네임을 띄워는 메소드
    def setlabel_welcome(self, id):
        nickname = get_nickname(id)
        self.label_welcome.setText('어서오세요 {0}님'.format(nickname))  # 받아온 닉네임을 출력
        pass

    # btn 관련
    # 로그인한 계정의 권한이 user일때 관리 버튼을 비활성화하는 메소드
    def setDisablebtn_manage(self, isadmin):
        if not isadmin:  # 권한이 user인 경우
            self.btn_manage.setDisabled(True)

    # 출근 기능을 실행하는 메소드
    def pushbtn_attendance(self):
        print(" 출근")
        result = attendance(self.lineEdit_name.text())
        QMessageBox.about(None, 'Notice', result)

    # 퇴근 기능을 실행하는 메소드
    def pushbtn_leavework(self):
        print(" 퇴근")
        result = leavework(self.lineEdit_name.text())

        QMessageBox.about(None, 'Notice', result)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 프로그램을 실행시켜주는 클래스
    loginWindow = LoginWindowClass()
    loginWindow.show()
    app.exec_()  # 프로그램을 이벤트루프로 진입시키는 코드
