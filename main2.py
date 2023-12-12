import numpy as np
from PIL import Image


def crop_and_save(input_path, output_path, left, top, right, bottom):
    # 打开原始BMP文件
    with Image.open(input_path) as img:
        # 使用crop方法截取指定区域
        cropped_img = img.crop((left, top, right, bottom)).convert("RGB")

        # 保存截取的图像为新的BMP文件
        cropped_img.save(output_path, "BMP")


fenlan = np.zeros(3460, dtype=int)
def is_fenlan(bmp_file_path):
    with Image.open(bmp_file_path) as img:
        # 获取图像的宽度和高度
        width, height = img.size
        print(width, height)

        for x1 in range(1246, 1290):
            for start_y in range(1, height - 20):
                pixel = img.getpixel((x1, start_y))
                if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y)) != (255, 255, 255):
                    pixel = img.getpixel((x1, start_y + 1))
                    if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 1)) != (255, 255, 255):
                        pixel = img.getpixel((x1, start_y + 2))
                        if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 2)) != (255, 255, 255):
                            pixel = img.getpixel((x1, start_y + 3))
                            if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 3)) != (255, 255, 255):
                                pixel = img.getpixel((x1, start_y + 4))
                                if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 4)) == (255, 255, 255):
                                    pixel = img.getpixel((x1, start_y + 5))
                                    if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 5)) == (
                                    255, 255, 255):
                                        pixel = img.getpixel((x1, start_y + 6))
                                        if pixel == (255, 255, 255) and img.getpixel((x1 + 1, start_y + 6)) == (
                                                255, 255, 255):
                                            pixel = img.getpixel((x1, start_y + 7))
                                            if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 7)) != (
                                                    255, 255, 255):
                                                pixel = img.getpixel((x1, start_y + 8))
                                                if pixel != (255, 255, 255) and img.getpixel((x1 + 1, start_y + 8)) != (
                                                        255, 255, 255):
                                                    pixel = img.getpixel((x1, start_y + 9))
                                                    if pixel != (255, 255, 255) and img.getpixel(
                                                            (x1 + 1, start_y + 9)) != (
                                                            255, 255, 255):
                                                        pixel = img.getpixel((x1, start_y + 10))
                                                        if pixel != (255, 255, 255) and img.getpixel(
                                                                (x1 + 1, start_y + 10)) != (255, 255, 255):
                                                            pixel = img.getpixel((x1, start_y + 11))
                                                            if pixel == (255, 255, 255) and img.getpixel(
                                                                    (x1 + 1, start_y + 11)) == (255, 255, 255):
                                                                pixel = img.getpixel((x1, start_y + 12))
                                                                if pixel == (255, 255, 255) and img.getpixel(
                                                                        (x1 + 1, start_y + 12)) == (255, 255, 255):
                                                                    pixel = img.getpixel((x1, start_y + 13))
                                                                    if pixel == (255, 255, 255) and img.getpixel(
                                                                            (x1 + 1, start_y + 13)) == (255, 255, 255):
                                                                        fenlan[start_y] = 1



def is_title():
    pass


is_ok = 0
zylan = 0
num = 1
def locate_all_brackets_coordinates(bmp_file_path):
    global is_ok, zylan, num, fenlan
    with Image.open(bmp_file_path) as img:
        # 获取图像的宽度和高度
        width, height = img.size
        print(width, height)

    is_fenlan(bmp_file_path)

    print(fenlan[376])  # ???这个地方是文字，但是判断成了分割线
    temp = 0

    this_fenlan = [0]
    for i in range(1,height):
        if fenlan[i] != temp:
            this_fenlan.insert(len(this_fenlan), i)
            temp = fenlan[i]

    print(this_fenlan)








# 示例用法
# for i in range(10,459):
#     fenlan = np.zeros(5000, dtype=int)
#     bmp_file_path = "D:\zhuomian\新高考生物真题全刷：基础1000题 含扉页_00\新高考生物真题全刷：基础1000题 含扉页_"+str(i)+".bmp"
#     output_bmp_path = "D:\zhuomian\end\ "
#     locate_all_brackets_coordinates(bmp_file_path)

bmp_file_path = "D:\zhuomian\新高考生物真题全刷：基础1000题 含扉页_25.bmp"
output_bmp_path = "D:\zhuomian\end1\ "
locate_all_brackets_coordinates(bmp_file_path)


# D:\zhuomian\新高考生物真题全刷：基础1000题 含扉页_05.bmp