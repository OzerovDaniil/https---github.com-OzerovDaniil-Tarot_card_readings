
import random
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
 
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def generate_random_tarot_cards():
    # Приклад генерації три випадкових карт таро
    tarot_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
    return random.sample(tarot_cards, 3)

def search_tarot_meaning(cards):
    # Створення URL для пошуку значень карт таро
    search_query = "+".join(cards)
        #url = f"search.api.cnn.io/content?q={}"


#source = requests.get(url).text 
#json_reponse = json.loads(source)
    #headers = {'Referer': 'https://biddytarot.com/blog/ultimate-guide-tarot-card-combinations/'}
   # url = requests.get('https://biddytarot.com/blog/ultimate-guide-tarot-card-combinations/' , headers=headers)
    url = 'https://biddytarot.com/blog/ultimate-guide-tarot-card-combinations/' 
    opener = AppURLopener()
    response = opener.open('https://biddytarot.com/blog/ultimate-guide-tarot-card-combinations/' )
    #headers = {'User-Agent': 'Mozilla/6,.0'}
    #page = urlopen(url)
    #html = page.read().decode("utf-8")
    #soup = BeautifulSoup(html, "html.parser")
   # soup = BeautifulSoup(random_tarot_cards.content, "lxml")
   # film_name = soup.find(class_="fright fx-1").find("h1").text

    # Відправлення запиту на веб-сайт
    response = requests.get(url)

    if response.status_code == 200:
        # Використання BeautifulSoup для аналізу HTML сторінки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Отримання значень карт таро з результатів пошуку
        meanings = []
        for result in soup.find_all('div', class_='tarot-meaning'):
            meanings.append(result.text.strip())

        return meanings
    else:
        return None

# Генерація випадкових карт та пошук їх значень
random_tarot_cards = generate_random_tarot_cards()
meanings = search_tarot_meaning(random_tarot_cards)

if meanings:
    for card, meaning in zip(random_tarot_cards, meanings):
        print(f"{card}: {meaning}")
else:
    print("Помилка під час виконання запиту на веб-сайт.")

