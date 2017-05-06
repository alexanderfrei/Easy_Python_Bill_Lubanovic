# порядок ключей в словаре может быть произвольным
some_dict = {}
place = {
    1: 'gold',
    2: 'silver',
    3: 'bronze'
}
some_list = [['a','b'],['c',1]]
print(dict(some_list))

place[1] = 'win'
print(place)

other = {
    'other': 'такие дела'
}

place.update(other)
print(place)

del place['other']
print(place)

print(place.get(2))
print(place.get(4))
try:
    print(place[4]) # KeyError
except:
    pass

print('other' in place)
print(1 in place)

print(place.keys()) # return dict_keys type
print(list(place.keys()))
print(list(place.values()))
print(list(place.items()))
