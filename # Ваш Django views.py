# Ваш Django views.py 
 
from django.shortcuts import render 
from django.http import JsonResponse 
from .models import TarotCard  # Предполагаем, что у вас есть модель для карт Таро 
 
def tarot_reading(request): 
    # Ваш существующий код для вопросов и выбора карт 
 
    while True: 
        user_question = input("Enter your question: ") 
        if question_check(user_question) is False: 
            print("Помилка, ви не поставили знак питання, або написали меньше одного слова") 
        elif question_check(user_question) is True: 
            if open_question_check(user_question) is False: 
                print("Помилка, ви задали не відкрите питання") 
            elif open_question_check(user_question) is True: 
                break 
 
    # Ваш существующий код для Google Sheets и выбора комбинации карт 
 
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