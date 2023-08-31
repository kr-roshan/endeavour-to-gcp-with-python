# try out various datetime functions in python

import datetime

def PrintDateTime():
    print(datetime.datetime.now())
    print(datetime.datetime.today())
    print(datetime.timedelta(1))
    print(datetime.timedelta(days=1).__class__)
    print("datetime.__class__: ")
    print(datetime.__class__)
    print(datetime.datetime.__class__)
    print(datetime.datetime.today() - datetime.timedelta(1))
    today = datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.min.time())
    print(today)
    print(today.__class__)
    yesterday = datetime.datetime.combine(datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time())
    print(yesterday)
    print(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))

if __name__ == '__main__':
    PrintDateTime()



