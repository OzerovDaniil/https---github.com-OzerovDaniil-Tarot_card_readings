import csv
import random
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError

from test2 import get_value

credentials_path = 'C:\\Users\\Tkach\\Downloads\\glass-ally-414719-d0c89a69ae01.json'

credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
spreadsheet_id = '1cjoEtpVmRHn8CXZDJWtXkd86bVgmsXjqw5FeNIiay2E'
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(spreadsheet_id)

def get_random_combination():
    try:
        # Отримання аркуша за замовчуванням
        worksheet = spreadsheet.sheet1

        # Отримання всіх записів у вигляді списку словників, де ключі - це назви стовпців
        all_records = worksheet.get_all_records()

        # Отримання унікальних комбінацій карт
        all_combinations = set(row['Комбінації карт'] for row in all_records)

        # Вибір випадкової комбінації
        random_combination = random.choice(list(all_combinations))

        return random_combination
    except APIError as e:
        print(f'APIError: {e.response}')
        return 'APIError'

# Get a random combination
random_card = get_random_combination()

# Get value for the random combination
value = get_value(random_card)

print(f'Random combination: {random_card}')
print(f'Corresponding value: {value}')
