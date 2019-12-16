import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apis import sheet_url, filename

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = sheet_url

doc = gc.open_by_url(spreadsheet_url)

# 구글 스프레드 시트 테스트

