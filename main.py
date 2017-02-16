from bot import get_message
from bot import send_message

def main():
    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
            else:
                continue
    sleep(3)

if __name__ == '__main__':
    main()