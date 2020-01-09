from os.path import expanduser
import os


home= expanduser('~')
hely=home+'\Appdata\Roaming\Microsoft\Windows\Start Menu\Programs\helo.txt'   #\a hangszórót akarja megszólaltatni
print(hely)
os.startfile(hely)
os.write(hely,#mit írsz be)

