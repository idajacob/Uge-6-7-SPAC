import requests
import pandas as pd
import json
import mysql.connector

url = "http://192.168.20.171:3306/stocks"
auth = ('curseit', 'curseword')

response = requests.get(url, auth=auth)
raw_text = response.text

first_pass = json.loads(raw_text)
data = json.loads(first_pass) if isinstance(first_pass, str) else first_pass

df = pd.DataFrame(data)
print("Forbindelse oprettet")
print(df.head())