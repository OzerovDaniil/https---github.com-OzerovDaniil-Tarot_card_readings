import random 
import nltk # Імпортуємо бібліотеку, котра надає інструмент для обробки звичайної мови 
from nltk import word_tokenize # Поділяє текст на роздільні слова

nltk.download('punkt') # додаткові данні

#Токенізація та перевірка питання (Якщо я щось забув, додай, будь ласка, та подумай, чи потрібно нам робити так, щоб можна було запитати англійською мовою) 
def open_question_check(question):
    open_words = ["Що","Де","Коли","Чому","Хто","Як","Які","Чи","Яка","Яке"]

#Надо придумать что будет возвращать этот класс, по идее надо будет туда встаивть функцию которую мы пропишем потом с аи'шкой
class TarotMeanings:
    def predict(self, cards):
        return ["Chto to poka chto"]
Tarot_Cards = [""] #Напиши сюда названия всех карт

#Ініціалізація значення
meanings = TarotMeanings()

user_question = input("Enter your question: ")