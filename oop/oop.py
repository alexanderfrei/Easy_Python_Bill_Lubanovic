# oop

# init class

class Person():
    def __init__(self, name): # параметры, задаваемые с созданием экземпляра класса
        self.name = name
    def hello(self):
        print("Hello!")

hunter = Person("Elmer Fudd")
print(hunter)
print(hunter.name)

# наследование, перегрузка

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

esq = JDPerson("Elmer Fudd")
print(hunter.name, esq.name)
esq.hello()

# обращение к предку - super()

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

ep = EmailPerson('name', "email@mail.domain")
print(ep.name)

# геттеры и сеттеры
# г. и с. - это функции, оборачивающие запись и чтение атрибутов ( к которым нельзя обратиться непосредственно)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property # геттер-декоратор
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter # сеттер-декоратор
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

duck = Duck('Howard')
print(duck.name)
duck.name = 'Donald'
print(duck.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(10)
print(c.radius, c.diameter)
c.radius = 20
print(c.radius, c.diameter) # свойство diameter изменилось вместе с радиусом

# искажение имен для безопасности __

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

duck = Duck('Howard')
print(duck.name)
print(duck._Duck__name) # так называется скрытый атрибут


# методы

class A():
    count = 0 # атрибут класса
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod # метод класса
    def kids(cls):
        print("A has", cls.count, "little objects")
    @staticmethod # статический метод
    def st_example():
        print("this is static method")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
A.st_example() # для вызова этой функции необязательно создавать экземпляр класса

# полиморфизм

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

def who_says(obj):
    print(obj.who(), 'says', obj.says())

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")

who_says(hunter)
who_says(hunted1)
who_says(hunted2)

# композиция

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')

bill = Bill('wide orange')
tail = Tail('long')
duck = Duck(bill, tail)
duck.about()