import random # Бібліотека додающа рандом, необхідна для випадкового видання карт Таро
import nltk # Імпортуємо бібліотеку, котра надає інструмент для обробки звичайної мови 
from nltk import word_tokenize # Поділяє текст на роздільні слова

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
Tarot_Cards = [""] #Напиши сюда названия всех карт

#Ініціалізація значення
meanings = TarotMeanings()

user_question = input("Enter your question: ")