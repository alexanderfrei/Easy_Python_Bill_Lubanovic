import urllib.request as ur
url = 'https://github.com/alexanderfrei/Easy_Python_Bill_Lubanovic'
# url = 'http://www.iheartquotes.com/api/v1/random' вернет ошибку 503
conn = ur.urlopen(url)
print(conn) # HTTPResponse object
data = conn.read()
print(data)
print(conn.reason)
# for key, value in conn.getheaders():
#     print(key, value)

import requests
url = "http://coub.com/"
resp = requests.get(url)
print(resp)
# print(resp.text)

# bs4

def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page, "lxml")
    links = [element.get('href') for element in doc.find_all('a')]
    return links
url = "http://boingboing.net/"
print(get_links(url))