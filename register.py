import requests
import re, json, time, string, random
from utils import bs4, form_requirements, host, save
from fake_useragent import UserAgent
from mail import Numasa
from generator import Generator
from requests.exceptions import ConnectionError

class Facebook:
    def __init__(self, name: str=None):
        self.session = requests.session()
        self.session.cookies.clear()
        self.session.headers.update({"Accept": "text/html,application/xhtml+xml,application/xml;q=-1.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Content-Type": "application/x-www-form-urlencoded","dpr": "2.25","Origin": "https://mbasic.facebook.com","Referer": "https://mbasic.facebook.com/reg/?cid=103&refid=9","sec-ch-prefers-color-scheme": "light","sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"128\", \"Google Chrome\";v=\"128\"","sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "\"macOS\"","Sec-Fetch-Dest": "document","Sec-Fetch-Mode": "navigate","Sec-Fetch-Site": "same-origin","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": UserAgent().random,"viewport-width": "980"})
        
        fname = Generator.name()
        self.name = name if name is not None else fname[1]
        self.sex = fname[0]
        self.number = Generator.phone_number()
        self.passw = ''.join(random.choices(string.ascii_letters+string.digits, k=8))
        ttl = Generator.ttl()
        self.day = ttl[0]
        self.month = ttl[1]
        self.year = ttl[2]
        self.mail = Numasa()


    def register(self):
        source = bs4(self.session.get(host('reg/?cid=103&refid=9')).text)
        form = source.find('form')
        data = form_requirements(form)
        data.update({'firstname': self.name, 'reg_email__': self.number, 'reg_passwd__': self.passw, 'sex': self.sex, 'birthday_day': self.day, 'birthday_month': self.month, 'birthday_year': self.year})
        
        web = self.session.post(host(form['action']), data=data).text
        if 'save-device/cancel' in web:
            self.save_device(web)
        elif 'checkpoint' in web:
            pass
            '''
            print(f'CHECKPOINTS. FAILED TO CREATE ACCOUNT!')
            print(f'Name          : {self.name}')
            print(f'Phone number  : {self.number}')
            print(f'Mailpass      : {self.mail.mail} | {self.passw}')
            print(f'Sex           : {"Woman" if self.sex == 1 else "Man"}')
            print(f'Date of birth : {self.day}/{self.month}/{self.year}')
            '''
        else:
            pass
            #print('Kesalahan tahap 1')

    def save_device(self, source):
        try:
            form = bs4(source).find('form', {'method':'post', 'action': True})
            data = form_requirements(form)

            web = self.session.post(host(form['action']), data=data).text
            if 'confirmemail.php' in web:
                print(f'[{self.number}/{self.mail.mail} - {self.passw}] -> Change to temporary mail!')
                self.replace_tomail(web)
            else:
                pass
                #print('Kesalahan tahap 2')
        except ConnectionError:
            self.save_device(source)

    def replace_tomail(self, source):
        url = bs4(source).find('a', href=lambda href: 'changeemail' in href)
        try:
            form = bs4(self.session.get(host(url['href'])).text).find('form', {'method': 'post', 'action': True})
            data = form_requirements(form)
            data['new'] = self.mail.mail

            web = self.session.post(host(form['action']), data=data).text
            if '/changeemail/' in web:
                self.get_otp(web)
            elif 'setemail' in web:
                self.setmail(web)
            else:
                pass
                #print('Kesalahan tahap 3')
                #save(web)
        except ConnectionError:
            self.replace_tomail(source)

    def setemail(self, source):
        print(self.number)
        print(self.mail.mail)
        print(self.passw)
        save(web)
        
    def get_otp(self, source):
        for i in range(200):
            print(f'Waiting for the OTP code! {i}', end='\r')
            try:
                mailbox = self.mail.messages()['messages']
                if len(mailbox) != 0:
                    break
                else:
                    time.sleep(1)
            except ConnectionError:
                continue

        try: 
            otp = mailbox[0]['subject'].split(' ')[0].replace('FB-', '')
            self.confirm_mail(otp, source)
        except:
            print('VERIFICATION FAILLURE!')
            print(f'Name          : {self.name}')
            print(f'Phone number  : {self.number}')
            print(f'Mailpass      : {self.mail.mail} | {self.passw}')
            print(f'Sex           : {"Woman" if self.sex == 1 else "Man"}')
            print(f'Date of birth : {self.day}/{self.month}/{self.year}')
            
    def confirm_mail(self, otp, source):
        form = bs4(source).find('form', {'method': 'post', 'action': True})
        data = form_requirements(form)
        data['c'] = otp
        try:
            web = self.session.post(host(form['action']), data=data).text
            if 'home.php' in web:
                print(f'SUCCESSFULLY CREATED AN ACCOUNT!')
                print(f'Name          : {self.name}')
                print(f'Phone number  : {self.number}')
                print(f'Mailpass      : {self.mail.mail} | {self.passw}')
                print(f'Sex           : {"Woman" if self.sex == 1 else "Man"}')
                print(f'Date of birth : {self.day}/{self.month}/{self.year}')

            else:
                pass
                #print('Kesalahan tahap akhir 4')
        except ConnectionError:
            self.confirm_mail(otp, source)


        


