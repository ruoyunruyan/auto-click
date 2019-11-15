from PIL import Image, ImageGrab


def get_screen_xy_from_bmp(main_bmp, son_bmp):
    img_main = Image.open(main_bmp)
    img_son = Image.open(son_bmp)
    datas_a = list(img_main.getdata())
    print("image_main", img_main.size, len(datas_a))
    datas_b = list(img_son.getdata())
    print("image_son", img_son.size, len(datas_b))
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
                return yx[1], yx[0], img_son.size[0], img_son.size[1]
    return False


print(get_screen_xy_from_bmp("1.bmp", "weixin.bmp"))

image = Image.open("1.bmp")
print(image.size)
