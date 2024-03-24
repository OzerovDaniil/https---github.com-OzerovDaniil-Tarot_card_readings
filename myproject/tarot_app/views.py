from django.shortcuts import render

# Create your views here.

import random
import nltk
from nltk import word_tokenize
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError
import time

nltk.download('punkt')

def index(request):
    return render(request, 'tarot_app/index.html')

def about(request):
    return render(request, 'tarot_app/about.html')

# def question_check(user_question):
#     words = word_tokenize(user_question)
#     if words[-1] == '?' and len(words) > 1:
#         return True
#     return False

# def open_question_check(user_question):
#     open_key_words = ["Що", "Чому", "Як", "Які", "Яка", "Яке"]
#     words = word_tokenize(user_question)
#     for key_word in open_key_words:
#         if key_word in words:
#             return True
#     return False

# class TarotMeanings:
#     def predict(self, cards):
#         return ["Chto to poka chto"]

# Tarot_Cards = ["Жрець", "Блазень", "Маг", "Жриця", "Імператриця", "Імператор", "Ієрофант", "Закохані", "Колісниця", "Сила", "Пустельник", "Колесо Фортуни", "Справедливість", "Повішений", "Смерть", "Помірність", "Диявол", "Башта", "Зірка", "Місяць", "Сонце", "Страшний суд", "Світ", "Туз жезлів", "Двійка жезлів", "Трійка жезлів", "Четвірка жезлів", "П’ятірка жезлів", "Шістка жезлів", "Сімка жезлів", "Вісімка жезлів", "Дев’ятка жезлів", "Десятка жезлів", "Паж жезлів", "Лицар жезлів", "Королева жезлів", "Король жезлів", "Туз мечів", "Двійка мечів", "Трійка мечів", "Четвірка мечів", "П’ятірка мечів", "Шістка мечів", "Сімка мечів", "Вісімка мечів", "Дев’ятка мечів", "Десятка мечів", "Паж мечів", "Лицар мечів", "Королева мечів", "Король мечів", "Туз пентаклей", "Двійка пентаклей", "Трійка пентаклей", "Четвірка пентаклей", "П’ятірка пентаклей", "Шістка пентаклей", "Сімка пентаклей", "Вісімка пентаклей", "Дев’ятка пентаклей", "Десятка пентаклей", "Паж пентаклей", "Лицар пентаклей", "Королева пентаклей", "Король пентаклей"]

# meanings = TarotMeanings()

# def get_combination_for_pair(card1, card2):
#     try:
#         credentials_path = 'glass-ally-414719-d0c89a69ae01.json'
#         credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])
#         spreadsheet_id = '1cjoEtpVmRHn8CXZDJWtXkd86bVgmsXjqw5FeNIiay2E'
#         client = gspread.authorize(credentials)
#         spreadsheet = client.open_by_key(spreadsheet_id)

#         worksheet = spreadsheet.sheet1
#         all_records = worksheet.get_all_records()

#         for row in all_records:
#             if row['Комбінації карт'] == search_cards:
#                 return row['Значення комбінацій карт']
#     except APIError as e:
#         print(f'APIError: {e.response}')
#         return 'APIError'

# while True:
#     user_question = input("Enter your question: ")
#     if question_check(user_question) is False:
#         print("Помилка, ви не поставили знак питання, або написали меньше одного слова")
#     elif question_check(user_question) is True:
#         if open_question_check(user_question) is False:
#             print("Помилка, ви задали не відкрите питання")
#         elif open_question_check(user_question) is True:
#             break

# # Рандомний вибір двох карт зі списку
# while True: 
#     random_cards = random.sample(Tarot_Cards, 2)
#     card1, card2 = random_cards
  
#     search_cards = card1 + " " + "and" + " " + card2

#     # Пошук комбінації для кожної пари карт
#     combination = get_combination_for_pair(card1, card2)

#     # Додайте затримку між ітераціями, якщо потрібно
#     time.sleep(2)
#     print('\n') 
    
#     if combination:
#         print(f'Комбінація для пари {card1} і {card2}: {combination}')
#         break
