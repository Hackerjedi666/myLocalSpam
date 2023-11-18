import requests
import re

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

session = requests.Session()
url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
response = session.post(url, data = {"username" : 'please', "password" : "password"}, auth = (username, password))
response = session.get(url, auth = (username, password))
content = response.text

print(content)
