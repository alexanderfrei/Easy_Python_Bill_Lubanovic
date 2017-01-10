# zip
english = 'Monday', 'Tuesday', 'Wednesday'
russian = "Понедельник", "Вторник", "Среда"
print(list(zip(english,russian)))
print(dict(zip(english,russian)))

#списковое включение
rows = list(range(1,3))
cols = list(range(1,3))
cells = [(row,col) for row in rows for col in cols if row % 2 == 1 ]
for cell in cells:
    print(cell)

#словарное включение
word = 'слово'
letter_count = {letter: word.count(letter) for letter in word}
print(letter_count)

#включение множества
some_set = {number for number in [1,2,3,1,4,5,2]}
print(some_set)

# пространства имен
# global
# словари пространств имен: globals() и locals()

print('-- scope --')
animal = 'fruitbat'

def print_global():
    print('inside print_global: ', animal)
print('global:', animal)
print_global()

def change_global():
    global animal # иначе создастся локальная переменная
    animal = 'wombat'
    local_animal = 'raccoon'
    print('local variables:', locals())
    print('inside change_global: ', animal)

change_global()
print('global:', animal)
print('global variables:', globals())


# обращение к модулям пакета

print("--- source & modules ---")
from sources import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# setdefault() defaultdict()

print("--- standard library ---")
periodic_table = {'Hydrogen': 1, 'Helium': 2}
periodic_table.setdefault('Oxygen', 8)
periodic_table.setdefault('Helium', 777) # не сработает, если ключ уже существует
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int) # аргумент - функция
periodic_table['Oxygen'] = 8
periodic_table['Lithium']
print(periodic_table)

# Counter
from collections import Counter
breakfast = ['spam','spam','egg']
breakfast_counter = Counter(breakfast)
print(type(breakfast_counter),
      breakfast_counter,
      breakfast_counter.most_common(1)  )
lunch_counter = Counter(['coffee','bagel','bacon','egg'])
print(lunch_counter & breakfast_counter)
print(lunch_counter | breakfast_counter) # при объединении для одинаковых ключей
# выбирается наибольшее значение (не равно сложению)
print(lunch_counter + breakfast_counter)
print(lunch_counter - breakfast_counter)

# OrderedDict

from collections import OrderedDict # запоминает порядок ключей

quotes = OrderedDict([
    ('Curly', 'Nyuk nyuk!'),
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!')
])

for stooge in quotes:
    print(stooge)

# itertools

import itertools
for item in itertools.chain([1,2,3],['a','b','c']):
    print(item, end=' ')
i = 0

print('')
for item in itertools.cycle([1,2,3]):
    print(item, end=' ')
    i += 1
    if i == 50:
        break

print('')
for item in itertools.accumulate([1,2,3,4]):
    print(item, end=' ')

print('')
def multiply(a,b):
    return a * b
for item in itertools.accumulate([1,2,3,4], multiply):
    print(item, end=' ')

# создание собственных исключений
# исключение - класс

# class UppercaseException(Exception):
#     pass
#
# words = ['eeenie', 'meenie', 'miny', 'MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
