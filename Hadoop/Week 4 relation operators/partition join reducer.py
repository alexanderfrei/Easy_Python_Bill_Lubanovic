from collections import defaultdict

text = "user1\tquery:гугл\nuser1\turl:google.ru\nuser2\tquery:стэпик\nuser2\tquery:стэпик курсы\nuser2\turl:stepic.org\nuser2\turl:stepic.org/explore/courses\nuser3\tquery:вконтакте"
#text = "1\tquery:a\n1\turl:b\n1\tquery:a\n1\turl:c"
#text = "1\tquery:a\n1\turl:b\n2\tquery:a\n2\turl:b"

text = text.split('\n')

d = defaultdict(list)
old_key = "-1"
for line in text:
    key = line.strip().split('\t')[0]
    marker = line.strip().split('\t')[1].split(':')[0]
    value = line.strip().split('\t')[1].split(':')[1]
    #print("{0}\t{1}\t{2}".format(key,marker,value))
    if old_key == key or old_key == "-1":
        d[marker].append(value)
    if old_key != key and old_key != "-1":
        for q in d["query"]:        
            for u in d["url"]:           
                print("{0}\t{1}\t{2}".format(old_key,q,u))
        d.clear()
        d[marker].append(value)
    #print(d)
    old_key = key
for q in d["query"]:
    for u in d["url"]:
        print("{0}\t{1}\t{2}".format(old_key,q,u))