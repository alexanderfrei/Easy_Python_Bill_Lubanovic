ls = []
a = [1] * 5
print(a)
a = [1 for i in range(5)]
print(a)
a = [i ** 2 for i in range(5)]
print(a)

dogs = ['Белка', 'Стрелка']
dogs2 = ["Лэсси", "Хатико"]
gb = "The Good, the Bad, the Weird"

print(ls)
print(list('Котики и совы'))
print(dogs[1])

dogs.extend(dogs2) #равнозначно +=
print(dogs)
print("Лэсси" in dogs)

del dogs[-2:]
dogs.append(dogs2)
print(dogs)
print("Лэсси" in dogs)

dogs += ['Белка']
print(dogs.count("Белка"))

print(gb.split(','))
print(','.join(gb.split(',')))

sorted(dogs2, reverse=True) # не меняет список
print(dogs2)
dogs2.sort(reverse=True) # меняет список
print(dogs2)

dogs3 = sorted(dogs2).copy()
print(dogs2, dogs3)

#####################################
# tuples

print('-' * 40, 'tuples', sep='\r\n')
some_tuple = (1,2,3)
a,b,c = some_tuple
print(a,b,c)
a,b=b,a
print(a,b,c)
some_tuple = tuple(dogs3)
print(some_tuple)