import time
from pywinauto.application import Application

# 连接到进程的方法

# 1. 重新开启一个新的进程
# app = Application().start("notepad.exe")

# 2. 连接到已有的进程
# 2.1 使用进程ID (PID)进行绑定
# app = Application().connect(process=6020)

# 2.2 使用窗口句柄绑定
# app = Application().connect(handle=0x001201BE)

# 2.3 使用程序路径绑定
# app = Application().connect(path=r"C:\Windows\System32\notepad.exe")

# 2.4 使用标题、类型等匹配
app = Application().connect(title_re=".*记事本.*", class_name="Notepad")

# 3. 工具栏选择
dlg_spec = app.window(title='无标题 - 记事本')

# 3.1 文件
"""
['新建(&N)', '打开(&O)...', '保存(&S)', '另存为(&A)...', '', '页面设置(&U)...', '打印(&P)...', '退出(&X)']
"""
# dlg_spec.menu_select("文件->页面设置(&U)...")

# 3.2 编辑
"""
['撤消(&U)', '', '剪切(&T)', '复制(&C)', '粘贴(&P)', '删除(&L)', '查找(&F)...', 
'查找下一个(&N)', '替换(&R)...', '转到(&G)...', '3', '全选(&A)', '时间/日期(&D)']
"""
# dlg_spec.menu_select("编辑->替换(&R)...")

# 3.3 格式
"""
['自动换行(&W)', '字体(&F)...'
"""
# dlg_spec.menu_select("格式->字体(&F)")

# 3.4 查看
# dlg_spec.menu_select("查看->状态栏")

# 3.5 帮助
# dlg_spec.menu_select("帮助->关于记事本")

# 使用快捷键  Ctrl + H
dlg_spec.type_keys("^H")

time.sleep(2)
app["替换"]["取消"].click()

# window = app["无标题 - 记事本"]
# edit = window["Edit"]
# edit.type_keys("hello world")

# dlg_spec.type_keys("hello world")
