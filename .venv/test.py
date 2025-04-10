import requests

x = requests.get('https://w3schools.com/python/demopage.html')

print(x.text)
