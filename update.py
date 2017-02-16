import requests
import misc

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()