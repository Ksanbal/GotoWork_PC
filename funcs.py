from datetime import datetime
from Controlsheet import doc
import Vars as vars

now = datetime.now()

# 구글 시트 운용 코드
Attendance = doc.worksheet('Attendance')
Accounts = doc.worksheet('Accounts')


# 로그인 : 입력된 정보를 Accounts의 정보와 비교해 로그인을 수행하는 함수
def signin(id, passwd):
    findow = 0
    issuccess = False
    isadmin = False

    try:
        findrow = Accounts.find(id).row
    except:
        return '존재하지 않는 id입니다', issuccess, isadmin  # False 반환

    if findrow != 0:  # 아이디는 맞은 경우
        if passwd == Accounts.cell(findrow, 5).value:   # 비밀번호 체크(비밀번호 열 번호 : 5)
            issuccess = True
            permission = Accounts.cell(findrow, 6).value    # 권한정보 가져오기
            if permission == 'admin':
                isadmin = True
                return '환영합니다 관리자님', issuccess, isadmin
            else:
                isadmin = False
                return '로그인 성공', issuccess, isadmin
        else:
            return '비밀번호가 맞지 않습니다', issuccess, isadmin


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
    name = get_name(id)
    nickname = get_nickname(id)
    isfind = checkhistory(nickname, 4)  # 출근시간의 열 번호 : 4

    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    if isfind == 0:
        try:
            if islate(now.hour, now.minute):
                Attendance.append_row([return_date(), name, nickname, return_time(), '', '', '', '지각'], 'USER_ENTERED')
            else:
                Attendance.append_row([return_date(), name, nickname, return_time(), '', '', '', '정상출근'], 'USER_ENTERED')
            return '출근이 완료되었습니다.'
        except Exception as ex:
            return '출근이 정상적으로 실행되지 않았습니다. {0}'.format(ex)

    elif isfind == 1:
        return '퇴근이 기록되어 있어 출근이 기록되지 않습니다.'

    elif isfind == 2:
        return '이미 출근하였습니다.'


# 퇴근 : 출근한 날짜를 찾아 퇴근시간을 시트에 추가하는 함수
def leavework(id):
    name = get_name(id)
    nickname = get_nickname(id)
    isfind = checkhistory(nickname, 5)  # 퇴근시간의 열 번호 : 5

    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    if isfind == 0:
        Attendance.append_row([return_date(), name, nickname, '', return_time()], 'USER_ENTERED')
        return '출근기록이 없어서 퇴근시간만 기록되었습니다.'

    elif isfind == 1:  # 퇴근 기능 정상 실행
        row = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row  # 해당 날짜의 첫 기록 탐색
        while Attendance.cell(row, 1).value != '':
            if Attendance.cell(row, 3).value == nickname:
                findrow = row
                break
            row = row + 1

        Attendance.update_cell(findrow, 5, return_time())  # 퇴근시간 기록

        hour, minute = gettime(findrow)

        Attendance.update_cell(findrow, 6, hour)  # 근무시간 기록
        Attendance.update_cell(findrow, 7, minute)
        return '퇴근이 완료되었습니다.'

    elif isfind == 2:
        return '이미 퇴근하였습니다.'


# 해당 이름의 기록이 있는지 확인
def checkhistory(nickname, col):
    # 0:기록이 아예 없는 경우, 1:퇴근 기록만 있고 출근이 없는 경우 또는 그 반대, 2: 기록이 이미 있는 경우
    isfind = 0
    try:
        findrow = Attendance.find('{0}. {1}. {2}'.format(now.year, now.month, now.day)).row  # 해당 날짜의 첫 기록 탐색
    except:
        return isfind  # 기록이 없는 경우
    
    while Attendance.cell(findrow, 1).value != '':
        if Attendance.cell(findrow, 3).value == nickname:
            if Attendance.cell(findrow, col).value == '':  # 날짜와 이름은 있지만 해당 기록이 없는 경우
                isfind = 1
                return isfind
            else:  # 기록이 이미 다 있는 경우
                isfind = 2
                return isfind
        findrow = findrow + 1

    return isfind  # 기록이 없는 경우


# 시간 - 시간의 차 구해주는 함수
def gettime(row):
    mintime = Attendance.cell(row, 5).value  # 피감수
    subtime = Attendance.cell(row, 4).value  # 감수

    minhour, minmin = time2int(mintime)
    subhour, submin = time2int(subtime)

    if islate(subhour, submin):     # 지각인 경우 기록된 퇴근시간 - 출근시간
        if minmin < submin:
            minhour = minhour - 1
            minmin = minmin + 60

        resulthour = minhour - subhour
        resultmin = minmin - submin
    else:                           # 정상출근인 경우 퇴근시간 - 정해진 출근시
        subhour, submin = vars.attendance_hour, vars.attendance_min

        if minmin < submin:
            minhour = minhour - 1
            minmin = minmin + 60

        resulthour = minhour - subhour
        resultmin = minmin - submin

    # 점심시간이 포함되는지 확인
    if subtime.hour < 12:  # 점심시간(12시-1) 1시간을 뺀 시간을 반환
        return resulthour-1, resultmin
    else:
        return resulthour, resultmin


# 출근시간이 지각인지 체크해주는 함수
def islate(hour, minute):
    isover = False
    if hour > vars.attendance_hour:
        if minute > vars.attendance_min:
            isover = True   # 지각
    return isover


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


# 고유한 아이디의 사용자 이름을 가져오는 함수
def get_name(id):
    findrow = Accounts.find(id).row
    return Accounts.cell(findrow, 1).value


# 고유한 아이디의 닉네임을 가져오는 함수
def get_nickname(id):
    findrow = Accounts.find(id).row
    return Accounts.cell(findrow, 2).value

