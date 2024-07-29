import requests
import random
from utils import bs4, form_requirements, host, save

class Automation:
    def __init__(self, session):
        self.session = session
        self.img = [bs4(requests.get(url).text) for url in ['https://ibb.co/Vm648NL','https://ibb.co/yBN6Y5V','https://ibb.co/WWRCtWj','https://ibb.co/KrzSrGj','https://ibb.co/y64D0dV','https://ibb.co/3C28MW1']]

    def change_pp(self):
        images = requests.get(random.choice(self.img).find('link', {'rel': 'image_src'})['href']).content

        try: 
            add_url = bs4(self.session.get(host('me')).text).find('a', href=lambda href: '/photos/change/profile_picture/' in href)['href']
            upload_url = bs4(self.session.get(host(add_url)).text).find('a', href=lambda href: 'photos/upload' in href)['href']
        except TypeError:
            x = bs4(self.session.get(host('me')).text).find_all('a', href=lambda href: '/profile_picture/' in href)
            try: upload_url = x[1]['href']
            except IndexError: upload_url = x[0]['href']

        form = bs4(self.session.get(host(upload_url)).text).find('form', {'method': 'post', 'action': True})
        data = form_requirements(form)
        files = {'file1': images}

        upload = self.session.post(form['action'], data=data, files=files, allow_redirects=True)
        if 'success=1' in upload.url:
            print(f'LOG -> Successfully changed profile picture.')
        else:
            print(f'LOG -> Failure changed profile picture.')


