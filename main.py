import os, time
from register import Facebook

os.system('clear')
while True:
    Facebook().register()
    print()
    for i in range(120, 0, -1):
        if i < 100 and i > 10: print(f'Countdown 0{i}', end='\r')
        elif i < 10: print(f'Countdown 00{i}', end='\r')
        else: print(f'Countdown {i}', end='\r')
        time.sleep(1)
