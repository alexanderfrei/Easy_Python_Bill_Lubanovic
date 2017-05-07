import regex

text = "1:aut :C:a:esar aut nihil\n1:aut aut\n2:de mortuis aut bene aut nihil"
#text = "1:a:b\t   c"
text = text.split('\n')

for line in text:
    value = ""
    key = line.strip().split(':')[0]
    sn = line.strip().split(':')
    for i,v in enumerate(sn):
        if i > 0 and i < len(sn) - 1: value += v + ":"
        if i == len(sn) - 1: value += v
    words = regex.split('\s|\W+', value)
    #print(words)
    for w in words:
        if len(w) > 0:
            print("{0}#{1}\t1".format(w,key))