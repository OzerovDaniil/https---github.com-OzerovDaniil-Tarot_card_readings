from django.shortcuts import render
import random
import nltk
from nltk import word_tokenize
import gspread
from google.oauth2 import service_account
from gspread.exceptions import APIError
from django.http import JsonResponse
import time
from django.http import JsonResponse

def my_view(request):
    # Отримання даних для відповіді
    data = {'key': 'value'}
    # Повернення даних у форматі JSON
    return JsonResponse(data)

nltk.download('punkt')

def index(request):
    return render(request, 'tarot_app/index.html')

def about(request):
    return render(request, 'tarot_app/about.html')

def taro(request):
    return render(request, 'tarot_app/taroreading.html')

def question_check(user_question):
    words = word_tokenize(user_question)
    if words[-1] == '?' and len(words) > 1:
        return True
    return False

def open_question_check(user_question):
    open_key_words = ["Що", "Чому", "Як", "Які", "Яка", "Яке", "що", "чому", "як", "які", "яка", "яке"]
    words = word_tokenize(user_question)
    for key_word in open_key_words:
        if key_word in words:
            return True
    return False

def get_random_combination():
    try:
        credentials_path = 'glass-ally-414719-d0c89a69ae01.json'
        credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])
        spreadsheet_id = '1cjoEtpVmRHn8CXZDJWtXkd86bVgmsXjqw5FeNIiay2E'
        client = gspread.authorize(credentials)
        spreadsheet = client.open_by_key(spreadsheet_id)

        worksheet = spreadsheet.sheet1
        all_records = worksheet.get_all_records()

        # Отримуємо випадковий рядок
        random_row = random.choice(all_records)

        # Отримуємо значення двох стовпців для випадкового рядка
        combination = random_row['Комбінації карт']
        value = random_row['Значення комбінацій карт']

        return combination, value
    except Exception as e:
        print(f'Error: {e}')
        return None, None


def your_view(request):
    if request.method == 'POST':
        user_question = request.POST.get('tarot_query', '')
        if question_check(user_question):
            if open_question_check(user_question):
                context = {
                    'question_type': 'Відкрите питання',
                    'user_question': user_question,
                }
                return render(request, 'query_result.html', context)
            else:
                context = {
                    'question_type': 'Закрите питання',
                    'user_question': user_question,
                }
                return render(request, 'query_result.html', context)
        else:
            error_message = ''
            if len(user_question) < 1:
                error_message = 'Помилка: ви не ввели запитання.'
            elif not user_question.endswith('?'):
                error_message = 'Помилка: запитання має закінчуватися знаком питання.'
            return render(request, 'taroreading.html', {'error_message': error_message})
    else:
        combination, value = get_random_combination()

        if combination and value:
            context = {
                'question_type': '...',
                'user_question': '...',
                'combination': combination,
                'value': value,
            }
            if combination and value:
                return JsonResponse({'result': f'Combination: {combination}, Value: {value}'})
            else:
                return JsonResponse({'error': 'Error message here'}, status=400)
