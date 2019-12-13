from datetime import datetime
from Controlsheet import doc

now = datetime.now()

# 구글 시트 운용 코드
Attendance = doc.worksheet('Attendance')
Accounts = doc.worksheet('Accounts')


# 출근 : 출근날짜와 시간을 시트에 추가하는 함수
def attendance(id):
    Attendance.append_row([return_date(), id, return_time()], 'USER_ENTERED')


# 퇴근 : 출근한 날짜를 찾아 퇴근시간을 시트에 추가하는 함수
def leavework(id):
    try:
        row = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row
        findrow = 0  # 날짜와 이름이 같은 셀의 row

        while findrow == 0:
            if Attendance.acell('B'+row).value == id:
                findrow = row

            row = row + 1

    except:
        print("찾지 못했습니다.")

# 시트의 날짜형식으로 반환해주는 함수
def return_date():
    return '=DATE({0},{1},{2})'.format(now.year, now.month, now.day)


# 시트의 시간형식으로 반환해주는 함수
def return_time():
    return '=TIME({0},{1},{2})'.format(now.hour, now.minute, now.second)


# 고유한 아이디의 이름을 가져오는 함수
def get_name(id):
    pass


# 이름설정 : 사용자의 이름을 받아 시트에 chat_id와 이름을 추가하는 함수
def set_name(id, name):
    pass
