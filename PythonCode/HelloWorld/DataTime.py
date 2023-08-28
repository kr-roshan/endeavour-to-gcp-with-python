
import datetime
import os
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())

print(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
print(os.sep)
