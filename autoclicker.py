import time
import random
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

rorl = input('Type r for Right mouse button\nor l for left->')
if rorl == 'r':
    button = Button.right
elif rorl == 'l':
    button = Button.left
else:
    print("Invalid button type")
    exit()
print(button)
mincps = int(input('Insert minCPS>'))
maxcps = int(input('Insert maxCPS>'))
delay = mincps
button = Button.left
start_stop_key = KeyCode(char=input("on/off key(for example e,f...)->"))
exit_key = KeyCode(char=input("exit/turn off key (example e,f...)->"))


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
                self.delay = random.randint(int(mincps / 1000), int(maxcps / 1000))


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
