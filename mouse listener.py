import time
from pynput import mouse





def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    #if not pressed:
         #Stop listener
        #return False


def on_scroll(x, y, dx, dy):
    pass
    #print('Scrolled {0} at {1}'.format(
        #'down' if dy < 0 else 'up',
        #(x, y)))

def on_move(x, y):
    pass
    #print('Pointer moved to {0}'.format(
        #(x, y)))

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
