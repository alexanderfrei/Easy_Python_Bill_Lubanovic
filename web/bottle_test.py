import requests
resp = requests.get('http://localhost:9999/echo/Pikachu')
if resp.status_code == 200 and resp.text == 'Say hello to my little friend: Pikachu':
    print('It worked!')
else:
    print('No way (:', resp.text)
