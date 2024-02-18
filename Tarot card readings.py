import random # Бібліотека додающа рандом, необхідна для випадкового видання карт Таро
import nltk # Імпортуємо бібліотеку, котра надає інструмент для обробки звичайної мови 
from nltk import word_tokenize # Поділяє текст на роздільні слова
import csv      
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError


nltk.download('punkt') # додаткові данні

def question_check(question):
    words = word_tokenize(question.lower()) #Токенізація повідомлення
# Перевірка повідомлення від користувача на присутність знаку питання та присутності більше одного слова
    if words [-1] == '?' and len(words) > 1:
        return True
    return False

#Токенізація та перевірка питання (Якщо я щось забув, додай, будь ласка, та подумай, чи потрібно нам робити так, щоб можна було запитати англійською мовою) 
def open_question_check(question):
    open_key_words = ["Що","Де","Коли","Чому","Хто","Як","Які","Чи","Яка","Яке"]
#Токенізація та перевірка наявності ключових слів
    words = word_tokenize(question.lower())
    for key_word in open_key_words:
        if key_word in words:
            return True
    return False

#Надо придумать что будет возвращать этот класс, по идее надо будет туда встаивть функцию которую мы пропишем потом с аи'шкой
class TarotMeanings:
    def predict(self, cards):
        return ["Chto to poka chto"]
Tarot_Cards = ["Блазень","Маг","Верховна жриця","Імператриця","Імператор","Ієрофант","Закохані","Колісниця","Сила","Відлюдник","Колесо фортуни","Справедливість","Повішений","Смерть","Помірність","Диявол","Вежа","Зірка","Місяць","Сонце","Страшний суд","Світ","Туз Жезлів","Двійка Жезлів","Трійка Жезлів","Четвірка Жезлів","П’ятірка Жезлів","Шістка Жезлів","Сімка Жезлів","Вісімка Жезлів","Дев’ятка Жезлів","Десятка Жезлів","Паж Жезлів","Лицар Жезлів","Королева Жезлів","Король Жезлів","Туз Мечів","Двійка Мечів","Трійка Мечів","Четвірка Мечів","П’ятірка Мечів","Шістка Мечів","Сімка Мечів","Вісімка Мечів","	Дев’ятка Мечів","Десятка Мечів","Паж Мечів","Лицар Мечів","	Королева Мечів","Король Мечів","Туз Пентаклів","Двійка Пентаклів","Трійка Пентаклів","Четвірка Пентаклів","П’ятірка Пентаклів","Шістка Пентаклів","Сімка Пентаклів","Вісімка Пентаклів","Дев’ятка Пентаклів","Десятка Пентаклів","Паж Пентаклів","Лицар Пентаклів","Королева Пентаклів","Король Пентаклів"] #Напиши сюда названия всех карт

#Ініціалізація значення
meanings = TarotMeanings()

user_question = input("Enter your question: ")

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
    


# Get value for the random combination
value = get_value(random_combination)

print(f'Random combination: {random_combination}')
print(f'Corresponding value: {value}')