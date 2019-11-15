import time
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
import psutil


# 如果程序已经 , 则

def get_process_id(name="WeChat.exe"):
    """
    获取程序运行的 process id
    :param name:  程序名称 , 默认为微信
    :return:  程序运行的进程ID
    """
    for process in psutil.process_iter():
        if process.name() == name:
            return process.pid


def create_app():
    """
    创建app的工厂函数
    :return:  pswinauto.application.Application()实例化对象
    """


# app = Application().connect(process=3044)
#
# wind = app["微信"]
#
# wind.print_control_identifiers()
try:
    app = Application().connect(title_re="微信", class_name="WeChatMainWndForPC")
except ElementNotFoundError as e:
    print("Flase")
else:
    # print(app.is_process_running())
    # print(app.windows())
    app.window(title=u"微信", class_name="WeChatMainWndForPC").move_window(0, 0)
    time.sleep(2)
    app.window(title=u"微信", class_name="WeChatMainWndForPC").type_keys("{DOWN}")

