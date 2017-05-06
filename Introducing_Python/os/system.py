# запись вывода в файл
fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file= fout)
fout.close()

# os.path.exists
import os
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('.'))
print(os.path.exists('..')) # родительская папка

# проверка типа файла
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isabs('/')) # проверка абсолютного пути на правильность
print(os.path.isabs('incorrect/name'))

# операции
import shutil
shutil.copy('oops.txt','oops_copy.txt')
shutil.move('oops_copy.txt','oops_copy2.txt') # перемещение файла
os.rename('oops_copy2.txt','oops_copy3.txt')
os.remove('oops_copy3.txt')
print(os.path.abspath(name)) # return abspath

# каталоги
if os.path.exists('test'):
    os.rmdir('test')
os.mkdir('test')
print(os.listdir('..'))
print(os.listdir('.'))
os.chdir('test')
print(os.listdir('.'))

# поиск glob()
# Правила оболочки Unix:
# * - все символы
# ? - один символ
# [символы] - символы в скобках
# [!символы] - НЕсимволы в скобках

import glob
search = glob.glob('../../../*B??[l]*')[0]
print(os.path.abspath(search))

# процессы
print(os.getpid()) # id интерпретатора python
print(os.getcwd()) # текущая рабочая папка
print(os.getuid()) # id пользователя
print(os.getgid()) # id группы

import subprocess as sb
ret = sb.getoutput('date') # получение результата выполнения системной команды date() Unix
print(ret)
ret = sb.check_output(['date','-u']) # результат со списком параметров
print(ret)
print("---- Status ----")
ret = sb.getstatusoutput('date') # результат + статус
print(ret)

print("---- Call ----")
ret = sb.call('date -u', shell=True) # операция выполняется и дает вывод на экран
print(ret) # сохранен статус
sb.call(['date','-u'])

