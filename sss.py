# coding:utf-8

import time
import win32con
import win32gui
from pywinauto.application import Application

handle = 0x00070924

# 链接打开的软件
app = Application().connect(handle=handle)

# 将软件窗口移动到左上角
# app.window(title_re=".*记事本.*", class_name="Notepad").move_window(0, 0)

time.sleep(0.5)

win32gui.ShowWindow(handle, 3)

# 窗口置顶

win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 0, 0, 1366, 728, win32con.SWP_SHOWWINDOW)
