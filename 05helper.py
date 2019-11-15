import time
from pywinauto.application import Application
from PIL import ImageGrab, Image


def get_screenxy_from_bmp(main_bmp, son_bmp):
    from PIL import Image
    img_main = Image.open(main_bmp)
    img_son = Image.open(son_bmp)
    datas_a = list(img_main.getdata())
    datas_b = list(img_son.getdata())
    for i, item in enumerate(datas_a):
        if datas_b[0] == item and datas_a[i + 1] == datas_b[1]:
            yx = divmod(i, img_main.size[0])
            main_start_pos = yx[1] + yx[0] * img_main.size[0]

            match_test = True
            for n in range(img_son.size[1]):
                main_pos = main_start_pos + n * img_main.size[0]
                son_pos = n * img_son.size[0]

                if datas_b[son_pos:son_pos + img_son.size[0]] != datas_a[main_pos:main_pos + img_son.size[0]]:
                    match_test = False
                    break
            if match_test:
                return yx[1], yx[0]
    return False


# 链接打开的软件
app = Application().connect(handle=0x000108BC)

# 将软件窗口移动到左上角
app.window(title="邢台学院 - TeamViewer", class_name="TV_CClientWindowClass").move_window(0, 0)

time.sleep(0.5)

# 截图 943 * 728
image = ImageGrab.grab((0, 0, 943, 728))
image.save("page.bmp")

# 获取进样的坐标
jinyang = get_screenxy_from_bmp("page.bmp", "in.bmp")

while 1:
    app.window(title="邢台学院 - TeamViewer", class_name="TV_CClientWindowClass").click_input(coords=(jinyang[0] + 10, jinyang[1] + 5))
    time.sleep(1.5)

