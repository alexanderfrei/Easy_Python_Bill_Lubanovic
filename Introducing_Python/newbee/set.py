a = {2,3}
b = {2,3,4}
print(a & b) # пересечение
print(a | b) # объединение
print(a - b) # разница
print(a ^ b) # исключающее или (уникальные для одного из множеств элементы)
print(a <= b) # а подможество b?
print(a >= a) # а включает в себя a?
print(a > a)  #a включает в себя а и больше а?

s = set()
s.add(3)
s.add(2)
s.add(3)
s.add(5)

s2 = set([1,1,2,12,2,3])

union = s.union(s2)
print(s, 'union', s2, ':', union)

inter = s.intersection(s2)
print(s, '/', s2, ':', inter)

diff = s.difference(s2)
print(s, 'diff', s2, ':', diff)

s_diff = s.symmetric_difference(s2)
print(s, 'sym_diff', s2, ':', s_diff)

subset = s.issubset(s2)
print(s, 'is subset of', s2, ':', subset)

superset = s.issuperset(s2)
print(s, 'is superset of', s2, ':', superset)

disjoint = s.isdisjoint(s2)
print(s, 'is disjoint with', s2, ':', disjoint)

