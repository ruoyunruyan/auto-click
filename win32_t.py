import win32gui
import win32api
import win32con

# 获取电脑的屏幕尺寸
x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# 获取任务栏的尺寸
taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
left, top, right, bottom = win32gui.GetWindowRect(taskbar)

# 获取程序运行的句柄
handler = win32gui.FindWindow("Notepad", None)

# 获取窗口的位置
# left, top, right, bottom = win32gui.GetWindowRect(handler)

# 获取句柄的标题和类名
title = win32gui.GetWindowText(handler)
class_name = win32gui.GetClassName(handler)

# 获取子窗口
hwndChildList = []
win32gui.EnumChildWindows(handler, lambda hwnd, param: param.append(hwnd), hwndChildList)

"""
FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None)
父窗口句柄若不为0, 则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体, 否则从第一个子窗体开始搜索. 子窗口类名, 子窗口标题
"""
# subHandle = win32gui.FindWindowEx(handler, 0, "EDIT", None)
subHandle = win32gui.FindWindowEx(handler, 0, "msctls_statusbar32", None)

# 获得窗口的菜单句柄
menuHandle = win32gui.GetMenu(subHandle)

# 检查窗口是否最小化，如果是最大化
"""
1   最小化
0   未最小化
"""
# res = win32gui.IsIconic(handler)

"""
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

SW_HIDE:           隐藏窗口并激活其他窗口nCmdShow=0
SW_MAXIMIZE:       最大化指定的窗口nCmdShow=3
SW_MINIMIZE:       最小化指定的窗口并且激活在Z序中的下一个顶层窗口nCmdShow=6
SW_RESTORE:        激活并显示窗口如果窗口最小化或最大化，则系统将窗口恢复到原来的尺寸和位置在恢复最小化窗口时，应用程序应该指定这个标志nCmdShow=9
SW_SHOW:           在窗口原来的位置以原来的尺寸激活和显示窗口nCmdShow=5
SW_SHOWDEFAULT:    依据在STARTUPINFO结构中指定的SW_FLAG标志设定显示状态，STARTUPINFO 结构是由启动应用程序的程序传递给CreateProcess函数的nCmdShow=10
SW_SHOWMAXIMIZED:  激活窗口并将其最大化nCmdShow=3
SW_SHOWMINIMIZED:  激活窗口并将其最小化nCmdShow=2
SW_SHOWMINNOACTIVE:窗口最小化，激活窗口仍然维持激活状态nCmdShow=7
SW_SHOWNA:         以窗口原来的状态显示窗口激活窗口仍然维持激活状态nCmdShow=8
SW_SHOWNOACTIVATE: 以窗口最近一次的大小和状态显示窗口激活窗口仍然维持激活状态nCmdShow=4
SW_SHOWNORMAL:     激活并显示一个窗口如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小应用程序在第一次显示窗口的时候应该指定此标志nCmdShow=1
"""
win32gui.ShowWindow(handler, 3)

# 窗口置顶
"""
函数原型:               SetWindowPos(hWnd, hWndlnsertAfter, X, Y, cx, cy, Flags)
hWnd:                   窗口句柄

hWndlnsertAfter:        在z序中的位于被置位的窗口前的窗口句柄该参数必须为一个窗口句柄，或下列值之一:
HWND_BOTTOM:            将窗口置于Z序的底部如果参数hWnd标识了一个顶层窗口，则窗口失去顶级位置，并且被置在其他窗口的底部
HWND_DOTTOPMOST:        将窗口置于所有非顶层窗口之上（即在所有顶层窗口之后）如果窗口已经是非顶层窗口则该标志不起作用
HWND_TOP:               将窗口置于Z序的顶部
HWND_TOPMOST:           将窗口置于所有非顶层窗口之上即使窗口未被激活窗口也将保持顶级位置

x:                      以客户坐标指定窗口新位置的左边界
Y:                      以客户坐标指定窗口新位置的顶边界
cx:                     以像素指定窗口的新的宽度
cy:                     以像素指定窗口的新的高度

Flags:                  窗口尺寸和定位的标志该参数可以是下列值的组合
SWP_ASNCWINDOWPOS:      如果调用进程不拥有窗口，系统会向拥有窗口的线程发出需求这就防止调用线程在其他线程处理需求的时候发生死锁
SWP_DEFERERASE:         防止产生WM_SYNCPAINT消息
SWP_DRAWFRAME:          在窗口周围画一个边框（定义在窗口类描述中）
SWP_FRAMECHANGED:       给窗口发送WM_NCCALCSIZE消息，即使窗口尺寸没有改变也会发送该消息如果未指定这个标志，只有在改变了窗口尺寸时才发送WM_NCCALCSIZE
SWP_HIDEWINDOW;         隐藏窗口
SWP_NOACTIVATE:         不激活窗口如果未设置标志，则窗口被激活，并被设置到其他最高级窗口或非最高级组的顶部（根据参数hWndlnsertAfter设置）
SWP_NOCOPYBITS:         清除客户区的所有内容如果未设置该标志，客户区的有效内容被保存并且在窗口尺寸更新和重定位后拷贝回客户区
SWP_NOMOVE:             维持当前位置（忽略X和Y参数）
SWP_NOOWNERZORDER:      不改变z序中的所有者窗口的位置
SWP_NOREDRAW:           不重画改变的内容如果设置了这个标志，则不发生任何重画动作适用于客户区和非客户区（包括标题栏和滚动条）和任何由于窗回移动而露出的父窗口的所有部分如果设置了这个标志，应用程序必须明确地使窗口无效并区重画窗口的任何部分和父窗口需要重画的部分
SWP_NOREPOSITION:       与SWP_NOOWNERZORDER标志相同
SWP_NOSENDCHANGING:     防止窗口接收WM_WINDOWPOSCHANGING消息
SWP_NOSIZE:             维持当前尺寸（忽略cx和Cy参数）
SWP_NOZORDER:           维持当前Z序（忽略hWndlnsertAfter参数）
SWP_SHOWWINDOW:         显示窗口
"""
win32gui.SetWindowPos(handler, win32con.HWND_TOPMOST, 0, 0, 1366, 728, win32con.SWP_SHOWWINDOW)
