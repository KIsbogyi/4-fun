import time
from pynput.mouse import Button, Controller

mouse = Controller()
    

def Mzlego0():
    fbe = open('koordinata.txt', 'r')
    for data in fbe:
        data = data.strip().split(',')
        print(data[0], data[1])
        mouse.position = (int(data[0]), int(data[1]))
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
    
    

while True:
    time.sleep(10)
    Mzlego0()
    print('done')
    time.sleep(600)
    
