text = "aut\t1;4;1\naut\t2;2;1\nbene\t2;1;1\nde\t2;1;1\nmortuis\t2;1;1\nnihil\t1;1;1\nnihil\t2;1;1\nCaesar\t1;1;1\nCaesar\t2;1;1"
text = "aut\t1;4;1\naut\t2;2;1\nbene\t2;1;1\nde\t2;1;1\nmortuis\t2;1;1\nnihil\t1;1;1\nnihil\t2;1;1"
text = "aut\t1;4;1\nbbb\t2;4;1"
text = "aut\t12345;1;1"
text = "aut\t1;4;1\naut\t2;2;1\naut\t3;5;1\naut\t4;2;1"
text = text.split('\n')

old_word = "-1"
sum = 0
d = []
t = []
for line in text:
    word = line.strip().split('\t')[0]
    doc = line.strip().split('\t')[1].split(';')[0]
    tf = line.strip().split('\t')[1].split(';')[1]
    if old_word == word or old_word == "-1":        
        d.append(doc)
        t.append(tf)
        sum += 1
    if old_word != word and old_word != "-1":
        for i in range(len(d)):
            print("{0}#{1}\t{2}\t{3}".format(old_word,d[i],t[i],sum))
        iter = True
        sum = 1
        d = [doc]
        t = [tf]
    old_word = word
# отдельная обработка слова последнего слова    
for i in range(len(d)):
    print("{0}#{1}\t{2}\t{3}".format(old_word,d[i],t[i],sum))