# try out various datetime functions in python

import datetime

def PrintDateTime():
    print(datetime.datetime.now())
    print(datetime.datetime.today())
    print(datetime.datetime.today() - datetime.timedelta(1))
    today = datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.min.time())
    print(today)
    yesterday = datetime.datetime.combine(datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time())
    print(yesterday)
    print(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
    print(__name__)

if __name__ == '__main__':
    PrintDateTime()



