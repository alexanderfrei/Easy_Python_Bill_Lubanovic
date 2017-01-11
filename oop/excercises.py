# 1
class Thing():
    pass

print(Thing)
example = Thing()
print(example)
# 2
class Thing2():
    letters = "abc"
print(Thing2.letters)
# 3
class Thing3():
    def __init__(self, letters):
        self.letters = letters

thing3 = Thing3('xyz')
print(thing3.letters)
# 4,5,6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)
el_1 = Element('Hydrogen','H','1')
el_1.dump()
el_8 = {'name': 'Oxygen',
        'symbol': 'O',
        'number': '8'}
el_8 = Element(**el_8)
el_8.dump()
# print(el_1)
# 7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return '{} {} {}'.format (self.name, self.symbol, self.number)
el_1 = Element('Hydrogen','H','1')
print(el_1)

