#!/usr/bin/python3

from bot import get_message
from bot import send_message
from bot import get_btc

def main():
    answer = get_message()

    if answer != None:
        chat_id = answer['chat_id']
        text = answer['text']

#        if text == '/btc':
        send_message(chat_id, get_btc())
#        else:
#            continue

if __name__ == '__main__':
    main()
