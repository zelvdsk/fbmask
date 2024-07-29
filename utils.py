from bs4 import BeautifulSoup

bs4 = lambda src: BeautifulSoup(src, 'html.parser')
form_requirements = lambda form: {x['name']: x['value'] for x in form.find_all('input', {'name': True, 'value': True})}
host = lambda patch, h='https://mbasic.facebook.com/':  patch if h in patch else h + patch
save = lambda src: open('/sdcard/src.htm', 'w').write(str(src))
