import time
import os
from multiprocessing import Process, Queue
import win32api
import win32gui
import win32con
import tkinter

from PIL import Image, ImageGrab
from pywinauto.application import Application

# 电脑的桌面路径
DESKTOP = os.path.join(os.path.expanduser('~'), "Desktop")

# 桌面创建文件夹
if not os.path.exists(os.path.join(DESKTOP, "screen_short")):
    os.mkdir(os.path.join(DESKTOP, "screen_short"))


def get_screen_size():
    """
    获取电脑屏幕的尺寸
    :return:
    """
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return x, y


def get_task_bar_height():
    """
    获取任务栏高度
    :return:
    """
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    left, top, right, bottom = win32gui.GetWindowRect(taskbar)
    return bottom - top


def get_screen_xy_from_bmp(main_bmp, son_bmp):
    """
    获取要点击目标的相对位置
    :param main_bmp:  程序运行时的截图
    :param son_bmp:  目标位置的截图
    :return:  目标位置的相对坐标
    """
    img_main = Image.open(main_bmp)
    img_son = Image.open(son_bmp)
    data_main = list(img_main.getdata())
    data_son = list(img_son.getdata())

    for i, item in enumerate(data_main):
        if data_son[0] == item and data_main[i + 1] == data_son[1]:
            yx = divmod(i, img_main.size[0])
            main_start_pos = yx[1] + yx[0] * img_main.size[0]
            match_test = True
            for n in range(img_son.size[1]):
                main_pos = main_start_pos + n * img_main.size[0]
                son_pos = n * img_son.size[0]
                if data_son[son_pos:son_pos + img_son.size[0]] != data_main[main_pos:main_pos + img_son.size[0]]:
                    match_test = False
                    break
            if match_test:
                return yx[1], yx[0]
    return False


def set_position():
    """
    获取脚本窗口的运行位置
    :return:
    """
    screen_x, screen_y = get_screen_size()
    task_bar_height = get_task_bar_height()
    position = "150x30+%d+%d" % (screen_x - 200, screen_y - task_bar_height - 80)
    return position


def screen_short():
    pass


def begin():
    pass


def end():
    pass


def work():
    pass


def main():
    win = tkinter.Tk()
    win.title("auto")

    # 设置程序运行时的位置
    win.geometry(set_position())

    start = tkinter.Button(win, text="开 始")
    start.place(x=30, y=0)

    stop = tkinter.Button(win, text="暂 停")
    stop.place(x=80, y=0)

    win.mainloop()


if __name__ == '__main__':
    handle = win32gui.FindWindow("TV_CClientWindowClass", None)
    if handle:
        # 通过句柄连接软件
        app = Application().connect(handle=handle)

        x, y = get_screen_size()
        height = y - get_task_bar_height()

        # 将程序最大化并置顶
        win32gui.ShowWindow(handle, 3)
        win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, x, height, win32con.SWP_SHOWWINDOW)

        # 截图
        image = ImageGrab.grab((0, 0, x, height))
        image.save(os.path.join(DESKTOP, "page.bmp"))

        # 获取坐标
        axis = get_screen_xy_from_bmp(os.path.join(DESKTOP, "page.bmp"), os.path.join(DESKTOP, "in.bmp"))

        window = app.window(title_re=".*TeamViewer.*", class_name="TV_CClientWindowClass")

        window.click_input(coords=(axis[0] + 10, axis[1] + 5))
