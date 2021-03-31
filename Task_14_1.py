from time import sleep
from datetime import datetime

def timer(fn, ln, hour, mint, sec):
    all_time = sec + mint*60 + hour*3600
    for b in range(all_time):
        if sec == 0 and mint == 0 and hour > 0:
            sec = 60
            mint = 59
            hour -= 1
        if sec == 0 and mint > 0 and hour == 0:
           sec = 60
           mint = 59

        sec -= 1
        sleep(1)
        yield f'{hour}:{mint}:{sec}'

if __name__ == '__main__':
    fn = input('Name: ')
    ln = input('Last name: ')
    h = int(input('Insert hours: '))
    m = int(input('Insert Minutes: '))
    s = int(input('Insert Seconds: '))
    a = timer(fn, ln, h, m, s)
    time = datetime.now()
    with open('text.txt', 'a') as logs_of_start:
        logs_of_start.write(str(time.strftime("%d %B %Y %H:%M program used ")))
        logs_of_start.write(f'{fn} {ln} \n')
    for i in a:
        if i != '0:0:0':
            print(i)
        else:
            print('ALARM')
