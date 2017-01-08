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

#генератор
#генераторы нужны для создания огромных последовательностей без их полной загрузки в память
#генератор можно создать включением или функцией
#генератор срабатывает лишь однажды

number_gen = (number for number in range(1,1000)) # круглые () скобки
print(type(number_gen))
for num in number_gen:
    if num> 997: print(num)
number_gen = (number for number in range(1,1000)) # повторяем создание генератора
number_list = list(number_gen)
print(number_list)
number_list = list(number_gen) # пустой лист, т.к. генератор уже сработал раньше
print(number_list)

#Функции
#Удобочитаемость имеет значение

def get_arg(*args,**kwargs):
    """
    функция теста аргументов python
    :param args: int
    :param kwargs: str = str
    :return:
    """
    try:
        print('1:', args[0]) # 1ый аргумент
        print('Сумма:', sum(args)) # сумма аргументов
        print('Именованные аргументы: ', kwargs)
        [print(k) for k in kwargs.items()]
    except:
        pass

get_arg(1,2,3,4, red_pill = 'reality', blue_pill = 'illusion')


