import requests
import json
from flask import Flask , request
from flask import jsonify

app = Flask(__name__)








def write_json(request):
    with open('data.json', 'w') as f:
        json.dump(request, f, indent=2, ensure_ascii=False)



def send_message(chat_id, text):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def json_parser(js):
    chat_id = js['result'][-1]['message']['chat']['id']
    text = js['result'][-1]['message']['text']
    return chat_id, text



@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()   # get chat id of new user who texted my bot
        write_json(r)
        return jsonify(r)
    return '<h1>Hello bot</h1>'




def run():
    re = requests.get(URL+'getUpdates')
    js = re.json()
    chat_id, text = json_parser(js)
    send_message(chat_id, text)




if __name__ == '__main__':
    app.run()



#     https://api.telegram.org/bot827325038:AAF0ypg1nF575Vs-qI2TwCdSWgQMQBlR1e4/setwebhook?url=https://342b81d4.ngrok.io/