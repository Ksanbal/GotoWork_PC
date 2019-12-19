from datetime import datetime
from Controlsheet import doc

now = datetime.now()

# 구글 시트 운용 코드
Attendance = doc.worksheet('Attendance')
Accounts = doc.worksheet('Accounts')


# 로그인 : 입력된 정보를 Accounts의 정보와 비교해 로그인을 수행하는 함수
def signin(id, passwd):
    findow = 0
    issuccess = False
    try:
        findrow = Accounts.find(id).row
    except:
        return '존재하지 않는 id입니다', issuccess

    if findrow != 0:  # 아이디는 맞은 경우
        if passwd == Accounts.cell(findrow, 5).value:  # 비밀번호 열 번호 : 5
            issuccess = True
            permission = Accounts.cell(findrow, 6).value
            if permission == 'admin':
                isadmin = True
                return '환영합니다 관리자님', issuccess, isadmin
            else:
                isadmin = False
                return '로그인 성공', issuccess, isadmin
        else:
            return '비밀번호가 맞지 않습니다', issuccess


# 회원가입 : 입력된 정보를 Accounts시트에 추가하는 함수
def signup(name, nickname, birth, id, passwd):

    issuccess = False
    try:  # 중복 닉네임 검사
        Accounts.find(nickname)
        return '이미 존재하는 닉네임입니다.', issuccess
    except:
        pass
    try:  # 중복 아이디 검사
        Accounts.find(id)
        return '이미 존재하는 아이디입니다.', issuccess
    except:
        pass

    # 중복된 데이터가 없는 경우
    Accounts.append_row([name, nickname, birth, id, passwd, 'user'], 'USER_ENTERED')
    issuccess = True
    return '회원가입이 완료되었습니다.', issuccess


# 출근 : 출근날짜와 시간을 시트에 추가하는 함수
def attendance(id):
    isfind = checkhistory(id, 3)  # 출근시간의 열 번호 : 3

    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    if isfind == 0:
        try:
            Attendance.append_row([return_date(), id, return_time()], 'USER_ENTERED')
            return '출근이 완료되었습니다.'
        except:
            return '출근이 정상적으로 실행되지 않았습니다.'

    elif isfind == 1:
        return '퇴근이 기록되어 있어 출근이 기록되지 않습니다.'

    elif isfind == 2:
        return '이미 출근하였습니다.'


# 퇴근 : 출근한 날짜를 찾아 퇴근시간을 시트에 추가하는 함수
def leavework(id):
    isfind = checkhistory(id, 4)  # 퇴근시간의 열 번호 : 4

    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    if isfind == 0:
        Attendance.append_row([return_date(), id, '', return_time()], 'USER_ENTERED')
        return '출근기록이 없어서 퇴근시간만 기록되었습니다.'

    elif isfind == 1:  # 퇴근 기능 정상 실행
        row = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row  # 해당 날짜의 첫 기록 탐색
        while Attendance.cell(row,2).value != '':
            if Attendance.cell(row, 2).value == id:
                findrow = row
                break
            row = row + 1

        Attendance.update_cell(findrow, 4, return_time())  # 퇴근시간 기록

        hour, minute = gettime(findrow)
        Attendance.update_cell(findrow, 5, hour)  # 근무시간 기록
        Attendance.update_cell(findrow, 6, minute)
        return '퇴근이 완료되었습니다.'

    elif isfind == 2:
        return '이미 퇴근하였습니다.'

# 해당 이름의 기록이 있는지 확인
def checkhistory(id, col):
    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    isfind = 0
    try:
        row = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row  # 해당 날짜의 첫 기록 탐색
    except:
        return isfind  # 기록이 없는 경우
    
    while Attendance.cell(row, 2).value != '':
        if Attendance.cell(row, 2).value == id:
            if Attendance.cell(row, col).value == '':  # 날짜와 이름은 있지만 해당 기록이 없는 경우
                isfind = 1
                return isfind
            else:  # 기록이 이미 다 있는 경우
                isfind = 2
                return isfind
        row = row + 1

    return isfind  # 기록이 없는 경우


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


# 고유한 아이디의 닉네임을 가져오는 함수
def get_name(id):
    pass


# 이름설정 : 사용자의 이름을 받아 시트에 chat_id와 이름을 추가하는 함수
def set_name(id, name):
    pass
