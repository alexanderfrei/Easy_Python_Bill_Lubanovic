# CSV
# pandas csv read!

import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']]

with open('villains.csv', 'wt') as f_out:
    csv_out = csv.writer(f_out)
    csv_out.writerows(villains) # почему-то пилит пустые строки

with open('villains.csv', 'rt') as f_in:
    csv_in = csv.reader(f_in)
    villains_ = [row for row in csv_in if row]

print(villains_)

# JSON

import json
with open('menu.json') as data_file:
    menu = json.load(data_file) # load dict from file
print(menu)
print(type(menu))

menu_csv = json.dumps(menu) # convert dict to str
print(type(menu_csv))

menu_loaded = json.loads(menu_csv) # convert str to dict
print(type(menu_loaded))

# обработка datetime в JSON

from time import mktime
import datetime
now = datetime.datetime.utcnow()

class DTEncoder(json.JSONEncoder): # класс для перевода datetime в Unix-время
    def default(self, obj):
        # isinstance() checks the type of obj
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # else it's something the normal decoder knows:
        return json.JSONEncoder.default(self, obj)

print(now)
print(json.dumps(now, cls=DTEncoder))
print(type(json.dumps(now, cls=DTEncoder)))

# menu_loaded = json.loads(menu)
# print(menu_loaded)
# print(type(menu_loaded))

# menu_json = json.dumps(menu)

# YAML

