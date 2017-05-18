# прямая адресация

commands = "12\nadd 911 police\nadd 76213 Mom\nadd 17239 Bob\nfind 76213\nfind 910\nfind 911\ndel 910\ndel 911\nfind 911\nfind 76213\nadd 76213 daddy\nfind 76213".strip().split('\n')
phone_book = [None] * 10**7
for cm in commands[1:]:
    cm = cm.split()
    number = int(cm[1])
    if cm[0] == 'add':
        phone_book[number] = cm[2]
    if cm[0] == 'find':
        if phone_book[number]:
            print(phone_book[number])
        else:
            print('not found')
    if cm[0] == 'del':
        phone_book[number] = None
