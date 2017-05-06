names = ["Z", "G", 12]
print("""{0:~^5} and {1:#>5} sat in the tree.
{0:-<5} had fallen, {2} was stolen.
What's remaining in the tree?
{2:05} angry mans.
Oceans {2:.2f}
Hexadecimal: {2:x}
Binary: {2:b}
""".format(*names))

names_d = {'a1': "Z", 'a2': "G", 'a3': 1}
print("""{a1:~^5} and {a2:#>5} sat in the tree.
{a1:-<5} had fallen, {a3} was stolen.
What's remaining in the tree?
""".format(**names_d))