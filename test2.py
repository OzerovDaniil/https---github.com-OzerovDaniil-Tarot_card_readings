
import csv
import random
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError



credentials_path = 'C:\\Users\\Tkach\\Downloads\\glass-ally-414719-d0c89a69ae01.json'


credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
spreadsheet_id = '1cjoEtpVmRHn8CXZDJWtXkd86bVgmsXjqw5FeNIiay2E'
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(spreadsheet_id)



def get_value(combination):
    try:
        # Отримання аркуша за замовчуванням
        worksheet = spreadsheet.sheet1

        # Отримання всіх записів у вигляді списку словників, де ключі - це назви стовпців
        all_records = worksheet.get_all_records()

        for row in all_records:
            if row['Комбінації карт'] == combination:
                return row['Значення комбінацій карт']

        return 'Value not found'
    except APIError as e:
        print(f'APIError: {e.response}')
        return 'APIError'
# Random combination
random_combination = "Суд and Десятка чаш"

# Get value for the random combination
value = get_value(random_combination)

print(f'Random combination: {random_combination}')
print(f'Corresponding value: {value}')
