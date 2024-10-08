from datetime import datetime
from os import PRIO_PGRP

currenttime=(datetime.now())
print(currenttime)
format1=currenttime.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=currenttime.strftime("%M/%D/%Y")
print(format2)
print(currenttime.strftime("%d,%m %D,%Y"))
print(currenttime.strftime("%d,%m %D,%Y %H:%M:%S %p"))
print(currenttime.strftime("%a-%b-%d %H:%M:%S IST %Y"))
print(currenttime.strftime("%a-%b-%D %H:%M:%S IST %Y"))
print(currenttime.isoformat())
print(currenttime.strftime("%d"))
print(currenttime.strftime("%I:%M:%S"))
print(currenttime.strftime("%b"))
print(currenttime.strftime("%Y"))