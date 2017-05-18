# hash chaining
commands = "5\n12\nadd world\nadd HellO\ncheck 4\nfind World\nfind world\ndel world\ncheck 4\ndel HellO\nadd luck\nadd GooD\ncheck 2\ndel good".strip().split('\n')
commands = "4\n8\nadd test\nadd test\nfind test\ndel test\nfind test\nfind Test\nadd Test\nfind Test".strip().split('\n')
commands = "3\n12\ncheck 0\nfind help\nadd help\nadd del\nadd add\nfind add\nfind del\ndel del\nfind del\ncheck 0\ncheck 1\ncheck 2".strip().split('\n')

n = int(commands[0])
chain_list = [[] for i in range(n)]


def hash_(s, l):
    hsh = 0
    for i, s in enumerate(s):
        hsh += ((ord(s) * 263 ** i) % 1000000007)
    hsh %= 1000000007
    hsh %= l
    return hsh

for cm in commands[2:]:
    cm = cm.split()
    if cm[0] == 'add':
        hsh = hash_(cm[1], n)
        if cm[1] not in chain_list[hsh]:
            chain_list[hsh].append(cm[1])
    if cm[0] == 'check':
        i = int(cm[1])
        if chain_list[i]:
            print(' '.join(chain_list[i][::-1]))
        else:
            print('')
    if cm[0] == 'find':
        hsh = hash_(cm[1], n)
        if cm[1] in chain_list[hsh]:
            print('yes')
        else:
            print('no')
    if cm[0] == 'del':
        hsh = hash_(cm[1], n)
        if cm[1] in chain_list[hsh]:
            chain_list[hsh].remove(cm[1])

