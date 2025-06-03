import gspread
from google.oauth2.service_account import Credentials
from modules.envs import sheet_id


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
sheet = client.open_by_key(sheet_id)
sheet = sheet.sheet1
