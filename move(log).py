from pynput import mouse
import logging

logging.basicConfig(
    filename=r"C:\Users\62417\Desktop\a.txt", 
    filemode="a", 
    format="%(asctime)s : %(message)s",
    level=logging.INFO
)
log = logging.getLogger(__name__)

def on_move(x,y):
    log.info("鼠标移动({},{})".format(x,y))
    print("鼠标移动({},{})".format(x,y))

def on_click(x,y,button,pressed):
    log.info("点击x,y,button,pressed({},{},{},{})".format(x,y,button,pressed))
    print("点击x,y,button,pressed({},{},{},{})".format(x,y,button,pressed))

def on_scroll(x, y, dx, dy):
    log.info("scroll x, y, dx, dy({},{},{},{})".format(x, y, dx, dy))
    print("scroll x, y, dx, dy({},{},{},{})".format(x, y, dx, dy))

while True:
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as ls:
        ls.join()
    