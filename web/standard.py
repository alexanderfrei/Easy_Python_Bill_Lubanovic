import urllib.request as ur
url = 'https://github.com/alexanderfrei/Easy_Python_Bill_Lubanovic'
# url = 'http://www.iheartquotes.com/api/v1/random' вернет ошибку 503
conn = ur.urlopen(url)
print(conn) # HTTPResponse object
data = conn.read()
print(data)
print(conn.status)
for key, value in conn.getheaders():
    print(key, value)
