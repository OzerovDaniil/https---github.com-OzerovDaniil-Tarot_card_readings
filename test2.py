#import csv
#import random

# Чтение данных из CSV-файла
#with open(r'C:\python\Project\taro.csv', 'r', encoding='utf-8') as csvfile:
#    reader = csv.reader(csvfile)
#    next(reader)  # Пропустить заголовок, если он есть
#    card_values = [row[0] for row in reader]

# Рандомный выбор значения
#random_card_value = random.choice(card_values)

#print(f'Рандомная карта: {random_card_value}')

import csv
import random

def get_value(combination):
    with open(r'C:\python\Project\taro.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Комбінації карт'] == combination:
                return row['Значення комбінацій карт']

    return 'Value not found'

# Random combination
random_combination = "Суд and Десятка чаш"

# Get value for the random combination
value = get_value(random_combination)

print(f'Random combination: {random_combination}')
print(f'Corresponding value: {value}')
