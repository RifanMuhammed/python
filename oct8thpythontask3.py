from datetime import datetime
from os import PRIO_PGRP


currenttime=(datetime.now())
print(currenttime)
format2=currenttime.strftime("%Y-%m-%d %H:%M:%S")
print(format2)
format3=currenttime.strftime("%M/%D/%Y")
print(format3)
format4=currenttime.strftime("%d,%m %D,%Y")
print(format4)
format5=currenttime.strftime("%d,%m %D,%Y %H:%M:%S %p")
print(format5)
format6=currenttime.strftime("%a-%b-%d %H:%M:%S IST %Y")
print(format6)
format7=currenttime.strftime("%a-%b-%D %H:%M:%S IST %Y")
print(format7)
format8=currenttime.isoformat()
print(format8)
format9=currenttime.strftime("%d")
print(format9)
format10=currenttime.strftime("%I:%M:%S")
print(format10)
format11=currenttime.strftime("%b")
print(format11)
format12=currenttime.strftime("%Y")
print(format12)
