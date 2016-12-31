import requests
import json
import re
import urllib.parse

login_url = 'https://passport.pptv.com/v3/login/login.do'
login_params = {
    'format': 'json',
    'username': 'your name or email',
    'password': 'your password'
}

resp = requests.get(login_url, login_params)
print(resp.json())
user_info = resp.json()['result']

signed_url = 'http://api.usergrowth.pptv.com/doDailyPcard'

signed_params = {
    'username': user_info['username'],
    'token': urllib.parse.unquote(user_info['token']),
    'format': 'json',
    'from': 'client',
    'version': 'unknown',
    'index': 756429,
    'addstr': 'e68e5a53b9467f4a739f009c6e351de1'

}

signed_resp = requests.get(signed_url, signed_params)
print(signed_resp.json())