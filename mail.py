import requests
import re

class Numasa:
    def __init__(self):
        self.session = requests.session()
        self.session.cookies.clear()
        source = self.session.get('https://numasa.net').text
        self.token = re.search(r'"csrf-token" content="(.*?)"', source).group(1)
        self.mail = self.messages()['mailbox']

    def messages(self, token: str=None):
        api = self.session.post('https://numasa.net/messages', data={'_token': self.token if token is None else token, 'captcha': ''}).json()
        return api

