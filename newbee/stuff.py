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

# создание собственных исключений
# исключение - класс

class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)

print("lalala")