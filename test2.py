# Ваш Django views.py 
import random # Бібліотека додающа рандом, необхідна для випадкового видання карт Таро
import nltk # Імпортуємо бібліотеку, котра надає інструмент для обробки звичайної мови 
from nltk import word_tokenize # Поділяє текст на роздільні слова
from tkinter import *  
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError
import time
from django.shortcuts import render 
from django.http import JsonResponse 
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
from .models import TarotCard # Предполагаем, что у вас есть модель для карт Таро 
import tkinter
 
def question_check(user_question):
    words = word_tokenize(user_question) #Токенізація повідомлення
# Перевірка повідомлення від користувача на присутність знаку питання та присутності більше одного слова
    if words [-1] == '?' and len(words) > 1:
        return True
    return False

#Токенізація та перевірка питання (Якщо я щось забув, додай, будь ласка, та подумай, чи потрібно нам робити так, щоб можна було запитати англійською мовою) 
def open_question_check(user_question):
    open_key_words = ["Що","Чому","Як","Які","Яка","Яке"]
#Токенізація та перевірка наявності ключових слів
    words = word_tokenize(user_question)
    for key_word in open_key_words:
        if key_word in words:
            return True
    return False

#Надо придумать что будет возвращать этот класс, по идее надо будет туда встаивть функцию которую мы пропишем потом с аи'шкой
class TarotMeanings:
    def predict(self, cards):
        return ["Chto to poka chto"]
Tarot_Cards = ["Жрець","Блазень","Маг","Жриця","Імператриця","Імператор","Ієрофант","Закохані","Колісниця","Сила","Пустельник","Колесо Фортуни","Справедливість","Повішений","Смерть","Помірність","Диявол","Башта","Зірка","Місяць","Сонце","Страшний суд","Світ","Туз жезлів","Двійка жезлів","Трійка жезлів","Четвірка жезлів","П’ятірка жезлів","Шістка жезлів","Сімка жезлів","Вісімка жезлів","Дев’ятка жезлів","Десятка жезлів","Паж жезлів","Лицар жезлів","Королева жезлів","Король жезлів","Туз мечів","Двійка мечів","Трійка мечів","Четвірка мечів","П’ятірка мечів","Шістка мечів","Сімка мечів","Вісімка мечів","	Дев’ятка мечів","Десятка мечів","Паж мечів","Лицар мечів","	Королева мечів","Король мечів","Туз пентаклей","Двійка пентаклей","Трійка пентаклей","Четвірка пентаклей","П’ятірка пентаклей","Шістка пентаклей","Сімка пентаклей","Вісімка пентаклей","Дев’ятка пентаклей","Десятка пентаклей","Паж пентаклей","Лицар пентаклей","Королева пентаклей","Король пентаклей"] #Напиши сюда названия всех карт

#Ініціалізація значення
meanings = TarotMeanings()

while True:
    user_question = input("Enter your question: ")
    if question_check(user_question) is False:
        print("Помилка, ви не поставили знак питання, або написали меньше одного слова")
    elif question_check(user_question) is True:
        if open_question_check(user_question) is False:
            print("Помилка, ви задали не відкрите питання")
        elif open_question_check(user_question) is True:
            break

credentials_path = 'glass-ally-414719-d0c89a69ae01.json'


credentials = service_account.Credentials.from_service_account_file(
credentials_path,
scopes=['https://www.googleapis.com/auth/spreadsheets']
)
spreadsheet_id = '1cjoEtpVmRHn8CXZDJWtXkd86bVgmsXjqw5FeNIiay2E'
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(spreadsheet_id)


# Функція для отримання комбінації для вибраної пари карт
def get_combination_for_pair(card1 , card2):
    try:
        # Отримання аркуша за замовчуванням
        worksheet = spreadsheet.sheet1

        # Отримання всіх записів у вигляді списку словників, де ключі - це назви стовпців
        all_records = worksheet.get_all_records()

        for row in all_records:
            if row['Комбінації карт'] == search_cards:
                
                return row['Значення комбінацій карт']

        
    except APIError as e:
        print(f'APIError: {e.response}')
        return 'APIError'



 
    while True: 
        random_cards = random.sample(Tarot_Cards, 2) 
        card1, card2 = random_cards 
 
        search_cards = card1 + " " + "and" + " " + card2 
 
        combination = get_combination_for_pair(card1, card2) 
 
        time.sleep(2) 
        print('\n') 
 
        if combination: 
            print(f'Комбінація для пари {card1} і {card2}: {combination}') 
            break 
 
    # Возвращаем JsonResponse с результатами 
    response_data = { 
        'card1': card1, 
        'card2': card2, 
        'combination': combination, 
    } 
     
    return JsonResponse(response_data) 
 
# Ваш urls.py в Django приложении 
 
from django.urls import path 
from .views import tarot_reading 
 
urlpatterns = [ 
    path('tarot-reading/', tarot_reading, name='tarot_reading'), 
] 
 
# Пример использования в шаблоне (если используется) 
 
<!-- templates/your_app/your_template.html --> 
<!DOCTYPE html> 
<html> 
<head> 
    <title>Tarot Reading</title> 
</head> 
<body> 
    <h1>Welcome to Tarot Reading</h1> 
    <button id="getReading">Get Reading</button> 
    <div id="result"></div> 
 
    <script> 
        document.getElementById('getReading').addEventListener('click', function () { 
            fetch('/tarot-reading/') 
                .then(response => response.json()) 
                .then(data => { 
                    document.getElementById('result').innerHTML = Карта 1: ${data.card1}, Карта 2: ${data.card2}, Комбінація: ${data.combination}; 
                }); 
        }); 
    </script> 
</body> 
</html>