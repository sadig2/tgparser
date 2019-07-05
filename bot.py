import requests
import json




URL = 'https://api.telegram.org/bot827325038:AAF0ypg1nF575Vs-qI2TwCdSWgQMQBlR1e4/'



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





def run():
    re = requests.get(URL+'getUpdates')
    js = re.json()
    chat_id, text = json_parser(js)
    send_message(chat_id, text)




if __name__ == '__main__':
    run()