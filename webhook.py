import requests
import json

webhook_url = "https://davidprojects.pythonanywhere.com/notify"

data = {"telegram": "-1001819896075", "msg": "BUY AAPL", "key": "asd12dsdf13-a"}

r1 = requests.post(webhook_url, data = json.dumps(data), headers = {'Content-type' : 'application/json'})