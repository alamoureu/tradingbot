import requests
import json

webhook_url = "http://192.168.2.51:80/webhook"

data =[{"telegram": "-680210585", "msg": "Allo Antoine CHAT 1", "key": "asd12dsdf13-a"},{"telegram": "-773242778", "msg": "Allo Antoine CHAT 2", "key": "asd12dsdf13-a"}]

r1 = requests.post(webhook_url, data = json.dumps(data[0]), headers = {'Content-type' : 'application/json'})

#r2 = requests.post(webhook_url, data = json.dumps(data[1]), headers = {'Content-type' : 'application/json'})