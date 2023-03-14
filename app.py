from flask import Flask, request, abort
from pymongo import MongoClient
import requests

app = Flask(__name__)

def send_alert(data):
    key = data["key"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    chatID = data["telegram"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if key == "asd12dsdf13-a":
        try:
            requests.post('https://api.telegram.org/bot5916087740:AAH9z84E0qVRyZC6q5sg9BdsLPxPKuPjHVQ/sendMessage?chat_id=' + str(chatID) + '&text=' + msg)
        except KeyError:
            requests.post('https://api.telegram.org/bot5916087740:AAH9z84E0qVRyZC6q5sg9BdsLPxPKuPjHVQ/sendMessage?chat_id=-1819896075&text=ERORR')
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

@app.route('/notify', methods=['POST'])
def webhook():
    myclient = MongoClient("mongodb+srv://Antoine:123@cluster0.yraw2.mongodb.net/?retryWrites=true&w=majority")
    db = myclient["fx-trading"]
    options = db["Options"]
    
    if request.method == 'POST':
        data = request.get_json()
        send_alert(data) 
        options.insert_one({"data" : data})
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)