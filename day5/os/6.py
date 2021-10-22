import os
import datetime

path = "/Users/shobhit/Desktop/qti_panda/day5/os/4.py"

objs = os.stat(path)

creation_time = datetime.datetime.fromtimestamp(objs.st_ctime)
print(creation_time)
