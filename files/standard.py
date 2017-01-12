poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

len(poem)
f_out = open('some_file','w')
f_out.write(poem)
f_out.close()

f_in = open('some_file','r')
poem = f_in.read()
f_in.close()
print(poem)

# чтение по частям

poem_r = ''
f_in = open('some_file', 'r')
chunk = 100 # 100 символов
while True:
    fragment = f_in.read(chunk)
    if not fragment:
        break
    poem_r += fragment
    print('-- ', poem_r)
f_in.close()

# чтение по строкам

f_in = open('some_file', 'r')
poem_lines = f_in.readlines()
f_in.close()
print(poem_lines)
print(len(poem_lines))

# binary mode

bdata = bytes(range(0, 256))
size = len(bdata)
offset = 0
chunk = 100
f_out = open('bfile', 'wb')
while True:
    if offset > size:
        break
    f_out.write(bdata[offset: offset+chunk])
    offset += chunk
f_out.close()

f_in = open('bfile', 'rb')
print(f_in.read())
f_out.close()

# with

with open('bfile', 'rb') as f_in:
    print(f_in.read())

# tell и seek

with open('bfile', 'rb') as f_in:
    print(f_in.tell()) # текущая позиция в файле
    print(f_in.seek(254, 0)) # перейти к 254 символу с начала
    print(f_in.seek(1, 1))  # перейти к предпоследнему символу

# seek(offset, whence), второй параметр:
# если значение whence равно 0 (по умолчанию), сместиться на offset байт с начала файла
# если значение whence равно 1, сместиться на offset байт с текущей позиции
# если значение whence равно 2, сместиться на offset байт с конца файла

