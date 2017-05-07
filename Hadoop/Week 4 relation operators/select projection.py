import sys

sys.stdin = "1448713968\tuser2\thttps://ru.wikipedia.org/\n1448764519\tuser10\thttps://stepic.org/\n1448713968\tuser5\thttp://google.com/\n1448773411\tuser10\thttps://stepic.org/explore/courses\n1448709864\tuser3\thttp://vk.com/"
sys.stdin = sys.stdin.split('\n')

# select
for line in sys.stdin:
    user = line.strip('\n').split('\t')[1]
    if user == "user10":
        print(line.strip())

# projection
for line in sys.stdin:
    url = line.strip('\n').split('\t')[2]
    print(url)

