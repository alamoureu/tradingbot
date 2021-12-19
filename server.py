from flask import Flask, request, abort
import telegram_send
import requests

app = Flask(__name__)

def send_alert(data):
    key = data["key"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    chatID = data["telegram"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if key == "asd12dsdf13-a":
        try:
            requests.post('https://api.telegram.org/bot5074796706:AAGbPAthMi0ZIty0ioc2j_31WvrvNQs8MQU/sendMessage?chat_id=' + str(chatID) + '&text=' + msg)
        except KeyError:
            requests.post('https://api.telegram.org/bot5074796706:AAGbPAthMi0ZIty0ioc2j_31WvrvNQs8MQU/sendMessage?chat_id=-776291763&text=ERORR')
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        data = request.get_json()
        send_alert(data)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)