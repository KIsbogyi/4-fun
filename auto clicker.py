import time
from pynput.mouse import Button, Controller
from pynput import keyboard
is_running = True
import pygetwindow as gw
click_speed = int(input('click speed:'))
def Start_time():
    time.sleep(10)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    #if key == keyboard.Key.shift:                  #special keys: shift, esc etc.
    if key == keyboard.KeyCode(char = 'a'):        # normal keys: a,s,d,f,g etc.
    
        global is_running
        is_running = False
        # Stop listenere
        return False


listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()

mouse = Controller()
while is_running:
    time.sleep(click_speed)

    #mouse.press(Button.right)
    mouse.press(Button.left)
    mouse.release(Button.left)

mouse.release(Button.right)
