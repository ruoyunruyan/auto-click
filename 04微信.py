import time
from pywinauto.application import Application
from PIL import Image, ImageGrab

app = Application().connect(process=15296)

# app.window(title=u"微信", class_name="WeChatMainWndForPC").move_window(0, 0)

# app.window(title="微信", class_name="WeChatMainWndForPC").type_keys("hello world")
time.sleep(0.5)
# pic = ImageGrab.grab((60, 0, 305, 622))
# pic.save('2.bmp')

app.window(title="微信", class_name="WeChatMainWndForPC").click_input(coords=(200, 280))
