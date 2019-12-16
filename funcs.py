from datetime import datetime
from Controlsheet import doc

now = datetime.now()

# 구글 시트 운용 코드
Attendance = doc.worksheet('Attendance')
Accounts = doc.worksheet('Accounts')


# 출근 : 출근날짜와 시간을 시트에 추가하는 함수
def attendance(id):
    try:
        Attendance.append_row([return_date(), id, return_time()], 'USER_ENTERED')
        return True
    except:
        print('출근이 정상적으로 실행되지 않았습니다.')
        return False


# 퇴근 : 출근한 날짜를 찾아 퇴근시간을 시트에 추가하는 함수
def leavework(id):
    try:
        row = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row  # 해당 날짜의 첫 기록 탐색
        for _ in range(4):
            if Attendance.cell(row, 2).value == id:
                findrow = row
                break
            row = row + 1

        Attendance.update_cell(findrow, 4, return_time())  # 퇴근시간 기록

        hour, minute = gettime(findrow)
        Attendance.update_cell(findrow, 5, hour)  # 근무시간 기록
        Attendance.update_cell(findrow, 6, minute)
        return True
    except:
        print('탐색실패')
        Attendance.append_row([return_date(), id, '',return_time()], 'USER_ENTERED')
        return False
    

# 시간 - 시간을 구해주는 함수
def gettime(row):
    mintime = Attendance.cell(row, 4).value  # 피감수
    subtime = Attendance.cell(row, 3).value  # 감수

    minhour, minminute = time2int(mintime)
    subhour, subminute = time2int(subtime)

    if minminute < subminute:
        minhour = minhour - 1
        minminute = minminute + 60

    resulthour = minhour - subhour
    resultminute = minminute - subminute

    return resulthour, resultminute

 # 시트의 날짜형식을 숫자 시간과 분으로 반환하는 함수
def time2int(s_time):
    splitedtime = s_time.split()
    hourclock12 = splitedtime[0]
    time = splitedtime[1]

    # 0:hour, 1:minute, 2:second
    inttime = time.split(':')
    hour = int(inttime[0])
    minute = int(inttime[1])

    if hourclock12 == '오후':
        hour = hour + 12

    return hour, minute

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
